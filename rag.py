import chromadb

from sentence_transformers import SentenceTransformer
from utils import chunk_text


class ResearchAssistant:

    def __init__(self):

        # Embedding model
        self.embedding_model = SentenceTransformer(
            "all-MiniLM-L6-V2"
        )

        # ChromaDB
        self.client = chromadb.PersistentClient(
            path="chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="research_documents"
        )

    def add_document(self, text, document_name):

        # Split text into chunks
        chunks = chunk_text(text)

        # Create embeddings
        embeddings = self.embedding_model.encode(
            chunks
        ).tolist()

        # Create IDs
        ids = [
            f"{document_name}_{i}"
            for i in range(len(chunks))
        ]

        # Store in ChromaDB
        self.collection.add(
            documents=chunks,
            embeddings=embeddings,
            ids=ids,
            metadatas=[
                {
                    "source": document_name,
                    "chunk": i
                }
                for i in range(len(chunks))
            ]
        )

        return chunks

    def search(self, question, n_results=5):

        # Convert question into embedding
        question_embedding = self.embedding_model.encode(
            question
        ).tolist()

        # Search ChromaDB
        results = self.collection.query(
            query_embeddings=[question_embedding],
            n_results=n_results
        )

        return results