# AI Research Assistant

An AI-powered research assistant that allows users to upload documents, 
process their content, and ask questions about the uploaded information using **Retrieval-Augmented Generation (RAG)**.
The project combines document processing, semantic search, vector databases, and a local LLM to provide answers
based on the user's documents.

##  Features

*  Upload research papers, PDFs, and documents
*  Extract and split documents into smaller chunks
*  Generate semantic embeddings for document chunks
*  Store and retrieve embeddings using ChromaDB
*  Use a local LLM through Ollama to generate answers
*  Ask questions about uploaded documents
*  Retrieve relevant document sections before generating an answer
*  Built with Streamlit for a simple interactive interface


##  How It Works

             ┌──────────────────┐
             │   Upload PDF     │
             └────────┬─────────┘
                      ↓
             ┌──────────────────┐
             │ Extract Text     │
             └────────┬─────────┘
                      ↓
             ┌──────────────────┐
             │  Chunk Document  │
             └────────┬─────────┘
                      ↓
             ┌──────────────────┐
             │ Generate         │
             │ Embeddings       │
             └────────┬─────────┘
                      ↓
             ┌──────────────────┐
             │    ChromaDB      │
             │ Vector Database  │
             └────────┬─────────┘
                      ↓
        ┌────────────────────────────┐
        │       User Question        │
        └─────────────┬──────────────┘
                      ↓
             ┌──────────────────┐
             │ Semantic Search  │
             └────────┬─────────┘
                      ↓
             ┌──────────────────┐
             │ Relevant Chunks  │
             └────────┬─────────┘
                      ↓
             ┌──────────────────┐
             │ Ollama LLM       │
             │ Answer Generation│
             └────────┬─────────┘
                      ↓
             ┌──────────────────┐
             │     Response     │
             └──────────────────┘


## 🛠️ Tech Stack
Python                
Streamlit             
ChromaDB              
Sentence Transformers 
Ollama              
PyPDF                
Git & GitHub          


## 🧠 RAG Pipeline
This project follows a basic Retrieval-Augmented Generation pipeline:

### 1. Document Ingestion
The user uploads a document through the Streamlit interface.

### 2. Text Extraction
Text is extracted from the uploaded PDF.

### 3. Chunking
The extracted text is divided into smaller chunks so that relevant sections can be retrieved efficiently.

### 4. Embedding Generation
Each chunk is converted into a numerical vector using a Sentence Transformer model.

### 5. Vector Storage
The embeddings are stored in ChromaDB.

### 6. Retrieval
When the user asks a question, the system searches the vector database for the most semantically relevant chunks.

### 7. Generation
The retrieved context is passed to the local LLM through Ollama, which generates the final response.

## 📁 Project Structure
ai-research-assistant/
│
├── app.py                 # Streamlit application
├── utils.py               # Document processing utilities
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
│
├── chroma_db/             # Local vector database (ignored by Git)
│
└── .gitignore             # Files excluded from Git

## ⚙️ Installation

### 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/ai-research-assistant.git
cd ai-research-assistant

### 2. Create a virtual environment
python -m venv .venv
Activate it on Windows:
.venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Install Ollama
Install Ollama and pull the model used by the project.
For example:
ollama pull llama3.2
Make sure Ollama is running before starting the application.

### 5. Run the application
streamlit run app.py

The application should open in your browser.

##  Example Use Case
A student can upload a research paper and ask questions such as:
"What is the main problem addressed in this paper?"
"What methodology was used?"
"What are the key findings?"
"Explain the proposed architecture."
"What are the limitations mentioned by the authors?"

The system retrieves relevant sections from the uploaded document and uses them as context for generating the answer.

##  Privacy
The project is designed around local processing where possible.
Documents can be processed locally and the LLM can run through Ollama instead of requiring a hosted LLM API.
**Do not commit API keys, `.env` files, virtual environments, or generated vector databases to GitHub.**

##  Future Improvements
*  Support multiple documents simultaneously
*  Display the exact chunks used to generate an answer
*  Show source/page references for every response
*  Add document-level analytics
*  Improve chunking and retrieval strategies
*  Add conversation history
* Support DOCX and other document formats
*  Add reranking for better retrieval accuracy
*  Deploy the application online
*  Add evaluation metrics for RAG quality



## 🎯 What I Learned
Building this project helped me understand the practical workflow behind Retrieval-Augmented Generation, including:
* Document processing
* Text chunking
* Embeddings
* Vector databases
* Semantic search
* Local LLM inference
* Prompt construction
* Building AI applications with Streamlit
* Managing Python dependencies
* Using Git and GitHub for project version control

## 👩‍💻 Author
**Vaishnavi Aakuthota**
B.Tech — Data Science
Interested in **AI/ML, software development, and building practical AI systems.**

## ⭐ If you found this project useful
Feel free to star ⭐ the repository and explore the code.
