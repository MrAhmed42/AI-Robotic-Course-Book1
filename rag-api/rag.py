from dotenv import load_dotenv
import os
import cohere
from qdrant_client import QdrantClient
from google import genai # Standard synchronous client

load_dotenv()

# --- INITIALIZATION ---

# Initialize the Synchronous Gemini Client (Picks up GEMINI_API_KEY automatically)
try:
    gemini_client = genai.Client() 
except Exception as e:
    print(f"Failed to initialize Gemini Client: {e}") 

# Initialize Cohere and Qdrant clients
# FIX: Added prefer_grpc=False to force REST API and potentially disable local Fastembed mixin
qdrant_client = QdrantClient(
    url=os.getenv("QDRANT_URL"), 
    api_key=os.getenv("QDRANT_API_KEY"),
    prefer_grpc=False # Use REST calls instead of gRPC, which is a more stable default
)
co = cohere.Client(os.getenv("COHERE_API_KEY"))
COLLECTION_NAME = "robotics_book_vectors"
# --- END INITIALIZATION ---


def embed_text_cohere(text: str):
    """Embeds text using Cohere for vector search."""
    print("Embedding text with Cohere...")
    response = co.embed(texts=[text], model='embed-english-v3.0', input_type='search_query')
    return response.embeddings[0]

def query_qdrant(vector: list[float]):
    """Query Qdrant to retrieve context. Uses the canonical search_points method."""
    print("Querying Qdrant...")
    # FIX: Using search_points(), which is the standard method for vector search
    search_result = qdrant_client.query_points( 
        collection_name=COLLECTION_NAME,
        query=vector, 
        limit=3,
        with_payload=True,
    )
    return [hit.payload["text"] for hit in search_result]

# --- SYNCHRONOUS GENERATION FUNCTION ---
def generate_answer_with_gemini(context: list[str], question: str, selected_text: str | None = None) -> str:
    """Generates an answer using the Gemini model with retrieved context."""
    print("Generating answer with Gemini...")
    
    # 1. Format the Context and System Instruction
    if selected_text:
        context_str = f"Selected Text: {selected_text}"
    else:
        context_str = "\n".join(context)
    
    system_instruction = (
        "You are a helpful RAG system for a robotics book. "
        "Use the following CONTEXT to answer the user's QUESTION. "
        "If the answer is not found in the CONTEXT, state clearly and politely that you cannot answer based on the provided documents. "
    )

    # 2. Create the Full Prompt
    full_prompt = (
        f"{system_instruction}\n\n"
        f"CONTEXT:\n{context_str}\n\n"
        f"QUESTION: {question}"
    )

    # 3. Call the Gemini API SYNCHRONOUSLY
    try:
        response = gemini_client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=full_prompt
        )
        return response.text
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return "Sorry, I encountered an error while communicating with the AI model."