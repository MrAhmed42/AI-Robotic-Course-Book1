# Tasks: Integrated RAG Chatbot Development (Hackathon Scope)

## Tools
- **MCP Context7** → Lookup for Cohere, Qdrant, OpenAI Agents SDK, and FastAPI documentation.
- **MCP GitHub** → Repo operations, file creation, commits.

---

## Phase 1: RAG Backend Setup (FastAPI)

- [x] Use **MCP Context7** to:
  - Fetch the latest installation and usage guide for **FastAPI**.
  - Fetch setup guides for **Cohere Python SDK** and **Qdrant Python Client**.
  - Fetch setup guide for **OpenAI Agents SDK** with examples.
- [x] Create Python project structure for the FastAPI server (e.g., `rag-api/`).
- [x] Define environment variables:
  - `COHERE_API_KEY`
  - `QDRANT_URL`
  - `QDRANT_API_KEY`
  - `OPENAI_API_KEY`
- [x] Create core RAG functions:
  - `embed_text_cohere()`
  - `query_qdrant()`
  - `generate_answer_with_openai()`

---

## Phase 2: Data Ingestion & Storage (Qdrant)

- [x] Use **MCP Context7** to:
  - Fetch best practices for **Markdown text chunking** for RAG.
  - Fetch Qdrant Client code for **creating a new collection** (`robotics_book_vectors`).
- [x] **Data Extraction:** Iterate over all Docusaurus Markdown files in the `docs/` folder.
- [x] **Chunking:** Implement text chunking logic (e.g., 500 tokens with overlap).
- [x] **Embedding:** Use the **Cohere Embed API** to generate vectors for all chunks.
- [x] **Ingestion:** Batch-ingest all vectors and metadata (text + source file) into the Qdrant collection.

---

## Phase 3: API Endpoints Implementation & Logic

- [x] Implement primary endpoint: **POST** `/api/chat/query`
  - [x] Receive user’s question and optional `selected_text`
  - [x] Vectorize question using Cohere
  - [x] Retrieve top-k context chunks from Qdrant
  - [x] Construct final RAG prompt (context + query)
  - [x] Call **OpenAI Agents SDK** to generate the response
- [x] **Implement Text Selection Priority**
  - [x] Update RAG prompt template:
    - If `selected_text` is provided → **answer ONLY from selected_text**
    - Else → use retrieved context

---

## Phase 4: Frontend Integration (Docusaurus/React)

- [x] Use **MCP Context7** to:
  - Fetch Docusaurus docs on **Theme Component Swizzling**
- [x] Create a React component: `ChatbotWidget.js` (inside Docusaurus theme folder)
- [x] Implement chat UI:
  - Message list
  - Input box
  - Send button
- [x] Add `fetch` or `axios` call to `/api/chat/query`
- [x] **Text Selection Listener**
  - Capture selected text: `window.getSelection().toString()`
  - Show floating **“Ask Chatbot”** button when text is selected
- [x] Embed the widget as a persistent floating component on all pages

---

## Phase 5: Testing & Deployment

- [ ] Unit test and integration test the FastAPI endpoints (locally with `uvicorn`)
- [ ] Test RAG grounding with sample book queries
- [ ] Test text-selection priority (answer must come ONLY from selected text when provided)
- [ ] Deploy FastAPI backend (Render / Fly.io / Railway)
- [ ] Update Docusaurus config to use the live API URL

