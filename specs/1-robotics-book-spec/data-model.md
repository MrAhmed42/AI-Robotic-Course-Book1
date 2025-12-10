# Data Model: AI/Spec-Driven Technical Book with Integrated RAG Chatbot

## Entities

### 1. Module
- **Name**: Module (e.g., "The Robotic Nervous System (ROS 2)")
- **Description**: Represents a major section of the book, containing multiple chapters.
- **Fields**:
    - `id`: Unique identifier (string)
    - `title`: Title of the module (string)
    - `description`: Brief description of the module's content (string)
    - `chapters`: List of Chapter IDs (list of strings)

### 2. Chapter
- **Name**: Chapter
- **Description**: A specific topic within a module, containing detailed content.
- **Fields**:
    - `id`: Unique identifier (string)
    - `module_id`: ID of the parent module (string)
    - `title`: Title of the chapter (string)
    - `content`: Markdown content of the chapter (string)
    - `outcomes`: List of learning outcomes (list of strings)
    - `keywords`: List of keywords for search/RAG (list of strings)
    - `urdu_translation`: Optional Urdu translation of the chapter content (string)
    - `personalization_enabled`: Boolean, indicates if personalization is active for this chapter (boolean)

### 3. User Profile
- **Name**: User Profile
- **Description**: Stores user-specific information for authentication and personalization.
- **Fields**:
    - `id`: Unique user identifier (string, e.g., from better-auth)
    - `email`: User's email address (string)
    - `username`: User-chosen username (string)
    - `software_background`: User's software development experience/background (string)
    - `hardware_background`: User's hardware experience/background (string)
    - `preferences`: JSON object for other user preferences (e.g., UI theme, language defaults) (JSON)

### 4. RAG Document Chunk
- **Name**: RAG Document Chunk
- **Description**: Smaller, embeddable sections of book content for the RAG pipeline.
- **Fields**:
    - `id`: Unique chunk identifier (string)
    - `chapter_id`: ID of the source chapter (string)
    - `module_id`: ID of the source module (string)
    - `content`: Text content of the chunk (string)
    - `embedding`: Vector embedding of the content (vector/list of floats)
    - `metadata`: Additional context (e.g., page number, section title) (JSON)

### Relationships

- **Module has Chapters**: A Module contains multiple Chapters (one-to-many).
- **Chapter is part of Module**: A Chapter belongs to one Module (many-to-one).
- **User Profile personalizes Chapter**: User Profile influences how Chapter content is presented (many-to-many, via personalization logic).
- **RAG Document Chunk derived from Chapter**: RAG Document Chunks are generated from Chapter content (one-to-many).

### Validation Rules (from requirements)

- All content (modules, chapters) must align with Physical AI, Robotics, ROS 2, Simulation, and VLA concepts.
- RAG responses must be strictly grounded in book content.
- Selected-text RAG mode must only use user-selected content.
- Personalization must adapt explanations based on user background.
- Urdu translation must preserve technical meaning without oversimplification.
- English remains the primary source of truth for content.