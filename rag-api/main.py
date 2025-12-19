from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

# Ensure the 'app' directory is in the path so 'import rag' works correctly in Docker
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))
try:
    import rag 
except ImportError:
    # Fallback for different directory structures
    from . import rag

app = FastAPI()

# --- UPDATED CORS CONFIGURATION ---
# Setting allow_origins to ["*"] fixes the "Failed to Fetch" error on Vercel
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# --- END CORS CONFIGURATION ---

# --- INPUT MODEL ---
class Query(BaseModel):
    question: str
    selected_text: str | None = None

@app.get("/")
def read_root():
    return {"Hello": "World", "status": "Backend is live and accessible"}

# --- MAIN RAG ENDPOINT ---
@app.post("/api/chat/query")
def query(query: Query):
    print(f"Attempting to run RAG Agent with question: {query.question}")
    
    final_answer = None
    
    try:
        # Pass BOTH question and selected_text to the rag function
        final_answer = rag.run_rag_agent(
            question=query.question, 
            selected_text=query.selected_text
        )
        
    except Exception as e:
        error_message = f"CRASH DETECTED IN RAG LOGIC: {e}"
        print(error_message)
    
    # Ensure final_answer is a string and not None
    if final_answer is None or (isinstance(final_answer, str) and final_answer.strip() == ""):
        final_answer = "Sorry, I couldn't find a relevant answer or the RAG agent failed to generate a response. Please rephrase your question."
        print("DEBUG: Final answer was None/empty, sending fallback message.")
        
    return {
        "message": final_answer, 
        "question": query.question, 
        "selected_text": query.selected_text
    }