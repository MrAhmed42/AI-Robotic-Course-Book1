from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import rag # Imports the updated rag.py

app = FastAPI()

# NEW CORS CONFIGURATION
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
# END NEW CORS CONFIGURATION

class Query(BaseModel):
    question: str
    selected_text: str | None = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/api/chat/query")
# FIX: Using the synchronous function (def) to match the synchronous LLM call
def query(query: Query):
    try:
        embedding = rag.embed_text_cohere(query.question)
        context = rag.query_qdrant(embedding)
        
        print("Attempting to generate answer...")
        
        # Call the synchronous RAG function
        answer = rag.generate_answer_with_gemini(context, query.question, query.selected_text)
        
        return {"message": answer, "question": query.question, "selected_text": query.selected_text}
        
    except Exception as e:
        # Debugging hook for silent errors
        print("CRASH DETECTED IN RAG LOGIC:")
        print(e)
        raise