import os
import re
# from dotenv import load_dotenv
import cohere
from qdrant_client import QdrantClient, models
# from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, RunContextWrapper

# load_dotenv()

# gemini_api_key = os.getenv("GEMINI_API_KEY")

# # Setup Gemini as OpenAI-compatible client
# external_client = AsyncOpenAI(
#     api_key=gemini_api_key, 
#     base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
# )

# # Define Gemini model
# model = OpenAIChatCompletionsModel(
#     model="gemini-2.5-flash",
#     openai_client=external_client
# )

# # Run config
# config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True
# )

# Initialize clients
qdrant_client = QdrantClient(url=os.getenv("QDRANT_URL"), api_key=os.getenv("QDRANT_API_KEY"))
co = cohere.Client(os.getenv("COHERE_API_KEY"))

COLLECTION_NAME = "robotics_book_vectors"

def get_md_files(path):
    """Recursively get all markdown files from a directory."""
    md_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".md"):
                md_files.append(os.path.join(root, file))
    return md_files

def chunk_text(text, chunk_size=500, overlap=50):
    """Chunk text into smaller pieces."""
    tokens = re.split(r'(\s+)', text)
    chunks = []
    current_chunk = ""
    for token in tokens:
        if len(current_chunk) + len(token) > chunk_size:
            chunks.append(current_chunk)
            current_chunk = current_chunk[-overlap:]
        current_chunk += token
    chunks.append(current_chunk)
    return chunks

def embed_chunks(chunks):
    """Embed chunks using Cohere."""
    print("Embedding chunks...")
    response = co.embed(texts=chunks, model='embed-english-v3.0', input_type='search_document')
    return response.embeddings

def ingest_into_qdrant(vectors, chunks, metadatas):
    """Ingest vectors into Qdrant."""
    print("Ingesting into Qdrant...")
    qdrant_client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(size=len(vectors[0]), distance=models.Distance.COSINE),
    )
    qdrant_client.upload_points(
        collection_name=COLLECTION_NAME,
        points=[
            models.PointStruct(id=i, vector=vector, payload={"text": chunk, "metadata": metadata})
            for i, (vector, chunk, metadata) in enumerate(zip(vectors, chunks, metadatas))
        ],
    )

def main():
    """Main function to ingest data."""
    docs_path = "../docs"
    md_files = get_md_files(docs_path)
    
    all_chunks = []
    all_metadatas = []
    for file in md_files:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            chunks = chunk_text(content)
            all_chunks.extend(chunks)
            all_metadatas.extend([{"source": file}] * len(chunks))
            
    print(f"Found {len(md_files)} markdown files.")
    print(f"Created {len(all_chunks)} chunks.")
    
    embedded_chunks = embed_chunks(all_chunks)
    ingest_into_qdrant(embedded_chunks, all_chunks, all_metadatas)
    
    print("Ingestion complete.")

if __name__ == "__main__":
    main()
