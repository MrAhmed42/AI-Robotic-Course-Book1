from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import rag # Imports the updated rag.py

app = FastAPI()

# CORS CONFIGURATION
origins = [
    "http://localhost",
    "http://localhost:3000",  # Allow Docusaurus dev server
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# END CORS CONFIGURATION

# --- INPUT MODEL ---
class Query(BaseModel):
    question: str
    selected_text: str | None = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

# --- MAIN RAG ENDPOINT ---
@app.post("/api/chat/query")
def query(query: Query):
    print(f"Attempting to run RAG Agent with question: {query.question}")
    
    final_answer = None
    
    try:
        # 1. CRITICAL FIX: Pass BOTH question and selected_text to the rag function
        final_answer = rag.run_rag_agent(
            question=query.question, 
            selected_text=query.selected_text
        )
        
    except Exception as e:
        # 2. Log the detailed crash message for server-side debugging
        error_message = f"CRASH DETECTED IN RAG LOGIC: {e}"
        print(error_message)
    
    # --- CRITICAL FIX: Ensure final_answer is a string and not None ---
    if final_answer is None or final_answer.strip() == "":
        # This handles both RAG failure and a crash (Exception e)
        final_answer = "Sorry, I couldn't find a relevant answer or the RAG agent failed to generate a response. Please rephrase your question."
        print("DEBUG: Final answer was None/empty, sending fallback message.")
        
    # 3. Return a successful 200 OK response with the message
    return {
        "message": final_answer, 
        "question": query.question, 
        "selected_text": query.selected_text
    }