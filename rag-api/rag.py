from dotenv import load_dotenv
import os
import cohere
from qdrant_client import QdrantClient
from agents import (
    Agent, Runner, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel,
    function_tool
)

# ========== INITIALIZATION - Clients are now synchronous and passed to the tool function ==========

load_dotenv()

# Initialize Cohere and Qdrant clients globally or within the tool. 
# Global is simpler for a single-file script.
qdrant_client = QdrantClient(
    url=os.getenv("QDRANT_URL"), 
    api_key=os.getenv("QDRANT_API_KEY"),
    prefer_grpc=False
)
co = cohere.Client(os.getenv("COHERE_API_KEY"))
COLLECTION_NAME = "robotics_book_vectors"

# --- RAG UTILITY FUNCTIONS (Simplified/Retained) ---

def embed_text_cohere(text: str) -> list[float]:
    """Embeds text using Cohere for vector search."""
    print("-> Embedding text with Cohere...")
    response = co.embed(texts=[text], model='embed-english-v3.0', input_type='search_query')
    return response.embeddings[0]

def query_qdrant(vector: list[float]) -> list[str]:
    """
    Query Qdrant to retrieve context.
    """
    print("-> Querying Qdrant...")
    
    # The result is a QueryResponse object
    search_response = qdrant_client.query_points( 
        collection_name=COLLECTION_NAME,
        query=vector, 
        limit=3,
        with_payload=True,
    )
    
    search_results = search_response.points
    return [hit.payload["text"] for hit in search_results]

# --- AGENT TOOL DEFINITION ---

@function_tool
def robotics_rag_search(query: str) -> str:
    """
    Search the robotics book knowledge base to retrieve relevant context.
    Use this tool ONLY when the user asks a specific question about robotics, 
    the book, or technical concepts.
    
    :param query: The user's question or the search phrase for retrieval.
    :return: A string containing the retrieved context chunks.
    """
    print(f"\n[TOOL CALLED: robotics_rag_search] Query: '{query}'")
    try:
        vector = embed_text_cohere(query)
        context_chunks = query_qdrant(vector)
        
        if not context_chunks:
            return "No relevant context found in the robotics knowledge base."
            
        context_str = "\n---\n".join(context_chunks)
        
        print("-> Retrieval successful. Passing context back to Agent.")
        return f"CONTEXT RETRIEVED:\n{context_str}"
        
    except Exception as e:
        return f"RAG Tool Error: Could not perform search. Details: {e}"


# ========== AGENT SETUP (Using Your Working Configuration) ==========

# --- 1. Load API Key (Already done above)
gemini_api_key = os.getenv("GEMINI_API_KEY")

# --- 2. Setup Gemini client (AsyncOpenAI)
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# --- 3. Setup Model
model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

# --- 4. Setup RunConfig
config = RunConfig(
    model=model,
    tracing_disabled=True 
)

# --- 5. Setup Agent with the RAG Tool and Instructions (Updated for Urdu bonus) ---
RAG_AGENT_INSTRUCTIONS = (
    "You are an expert RAG system for a robotics book. "
    "Your first step is ALWAYS to use the `robotics_rag_search` tool "
    "to find context for the user's question, unless the question is trivial (like 'hello'). "
    "Use the retrieved context to generate a concise, accurate answer. "
    "If the context is insufficient, state politely that you cannot answer based on the documents. "
    "CRITICAL MULTILINGUAL RULE: Detect the language of the user's question. If the user asks in Urdu, you MUST translate and provide the entire answer in fluent Urdu. If the question is in English, answer in English."
)

agent = Agent(
    name="Robotics RAG Assistant",
    instructions=RAG_AGENT_INSTRUCTIONS,
    tools=[robotics_rag_search] # Register the tool here
)

# Define a simpler Agent for the explanation task (no tools)
EXPLAINER_AGENT_INSTRUCTIONS = (
    "You are an expert explanation bot. Your sole task is to analyze the text provided in the prompt "
    "and provide a concise, easy-to-understand explanation or summary. "
    "Do NOT use external knowledge. Do NOT use any tools. You must base your answer ONLY on the provided text. "
    "If the user asks to explain, provide the explanation. If the user asks a question, answer it based on the text."
)

explainer_agent = Agent(
    name="Text Explainer Bot",
    instructions=EXPLAINER_AGENT_INSTRUCTIONS,
    tools=[] # No tools needed for simple text explanation
)


# ========== RUN THE AGENT SYNCHRONOUSLY (Modified) ==========

def run_rag_agent(question: str, selected_text: str | None = None) -> str:
    """
    Runs the agent. Uses the RAG agent for search, or the Explainer agent for selected text.
    """
    print(f"\n--- Running Agent with Question: '{question}' ---")
    
    local_agent = agent         # Default to the RAG Agent
    input_prompt = question     # Default to the user's question

    # --- CRITICAL FIX: LOGIC TO HANDLE SELECTED TEXT ---
    if selected_text and selected_text.strip():
        print("DETECTED: User has selected text. Switching to Explainer Agent.")
        
        # 1. Use the simple explainer agent (no tools)
        local_agent = explainer_agent
        
        # 2. Re-frame the input as a command + context for the LLM
        input_prompt = (
            f"User's request: '{question}'. "
            f"Text to be explained:\n---\n{selected_text}\n---"
        )
        
    else:
        print("DETECTED: Standard query. Using RAG Agent (with Qdrant tool).")
        # local_agent and input_prompt remain the defaults (agent and question)
    # ---------------------------------------------------

    try:
        result = Runner.run_sync(
            local_agent,
            input=input_prompt,
            run_config=config
        )
        
        final_answer = result.final_output

        print("\n--- FINAL AGENT OUTPUT ---")
        print(final_answer)
        print("--------------------------")
        
        return final_answer
        
    except Exception as e:
        print(f"\n❌ Agent Run Failed: {e}")
        return None 

if __name__ == "__main__":
    # Test 1: Standard RAG Question
    print("\n\n--- TEST 1: STANDARD RAG QUERY ---")
    answer_rag = run_rag_agent("What are the key components of a PID controller used in robotics?")
    print(f"\nTest 1 Result Returned: {answer_rag}")
    
    # Test 2: Selected Text Explanation
    print("\n\n--- TEST 2: SELECTED TEXT EXPLANATION ---")
    selected_block = "CPU: Intel Core i7 (13th Gen+) or AMD Ryzen 9. RAM: 64 GB DDR5 is strongly recommended. While 32 GB is the absolute minimum, it will likely lead to crashes during complex scene rendering."
    question_explain = "explain this in simple words"
    answer_explain = run_rag_agent(question_explain, selected_block)
    print(f"\nTest 2 Result Returned: {answer_explain}")
    