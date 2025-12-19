# Implementation Plan: Integrated RAG Chatbot

**Branch**: `2-rag-chatbot-feature` (New branch for feature isolation)
**Input Spec**: Requirement 2 (RAG Chatbot Development)
**Goal**: Build and integrate a RAG Chatbot using FastAPI, Qdrant, Cohere, and Openai Agents SDK into the Docusaurus book.

---

## 🎨 Architecture Sketch

The system uses a **three-tier architecture** with two distinct pipelines: **Indexing** (one-time data load) and **Query** (live chat).



### Technical Stack Summary
* **Generation (LLM):** Openai Agents SDK 
* **Embeddings:** Cohere Embed v3
* **Vector DB:** Qdrant Cloud Free Tier
* **Backend API:** FastAPI
* **Frontend/UI:** React (Docusaurus Custom Component)

---

## 🏗️ Section Structure: RAG Implementation Phases

| Phase | Key Tasks | Key Deliverables |
| :--- | :--- | :--- |
| **I. Data & Storage** | Chunk and embed all Docusaurus Markdown files using Cohere. | Qdrant Collection populated with vectors and metadata (text content, source page). |
| **II. Backend API** | Set up FastAPI server with RAG logic. Define asynchronous endpoints for Query and Text Selection. | `/api/chat/query` endpoint accepting user text and returning a Gemini-generated, context-aware response. |
| **III. Frontend Integration**| Create a Docusaurus/React chat widget. Implement the user text selection event listener. | Floating Chat Widget embedded on all documentation pages for easy access. |

---

## 🧐 Research Approach

* **Research Focus:** Optimizing the **RAG prompt** to ensure Gemini strictly adheres to the retrieved context and the user-selected text, minimizing hallucinations.
* **Tool Setup:** Confirming asynchronous client usage (`AsyncQdrantClient`) and batch ingestion methods for the initial Cohere data load.
* **Docusaurus Integration:** Researching the most non-intrusive method for injecting a custom, site-wide React component (e.g., using swizzling on the Docusaurus `Layout` component).

---

## ✅ Quality Validation

| Acceptance Criteria | Validation Check |
| :--- | :--- |
| **RAG Grounding** | The chatbot must refuse to answer questions *outside* the book's scope (e.g., "What is the capital of France?"). |
| **Text Selection Priority** | If a user selects a paragraph and asks a conflicting question, the answer must **exclusively** use the context from the selected text. |
| **Performance** | API response time must be under **5 seconds** for standard queries. |
| **UX Integrity** | The chat widget must not interfere with Docusaurus navigation, scrolling, or mobile responsiveness. |

---

## 📝 Decisions Needing Documentation

| Decision | Options & Tradeoffs |
| :--- | :--- |
| **Embedding Model** | **Cohere Embed v3:** High quality, state-of-the-art semantic search. **Tradeoff:** Adds a separate API dependency (Cohere). |
| **Frontend State** | **useState/useReducer:** Simple, fast for hackathon. **Tradeoff:** Chat history is lost on page refresh. (Acceptable for hackathon scope). |
| **API Deployment** | **FastAPI on Render/Fly.io:** Simple PaaS. **Tradeoff:** Introduces recurring costs beyond free tiers. (Vercel is not ideal for Python APIs). |

---

## 🧪 Testing Strategy

| Strategy | Description |
| :--- | :--- |
| **Unit Tests (FastAPI)** | Test the Cohere embedding function to ensure the correct vector dimension is returned. Test the prompt construction to verify retrieved context is correctly inserted. |
| **Integration Tests (API)**| Deploy the FastAPI app. Query with a known phrase (e.g., "RTX 4070 Ti VRAM") and confirm the response is derived from the "Hardware Requirements" chapter. |
| **End-to-End (E2E) Test** | **Manual Test:** On the live Docusaurus site, select the paragraph about the **Jetson Orin Nano**, ask, "What is its role?", and verify the answer confirms it's the "Physical AI Edge Kit Brain." |

---

## 📦 Technical Details (Required Libraries)

* **Python Dependencies:** `fastapi`, `uvicorn`, `cohere`, `qdrant-client`, `google-genai`, `python-dotenv`
* **JavaScript/React Dependencies:** Native `fetch` or `axios` for API calls from the Docusaurus component.