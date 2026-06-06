"""
Pinecone Connector Skill
Handles connecting to Pinecone vector databases for semantic search,
upserting document embeddings, and querying context for RAG workflows.
"""

import os
import logging
from typing import List, Dict, Any, Optional

try:
    import pinecone
except ImportError:
    logging.warning("pinecone module not installed. Mocking behavior.")

class PineconeConnector:
    def __init__(self, api_key: str, environment: str, index_name: str):
        self.index_name = index_name
        self.connected = False
        
        try:
            pinecone.init(api_key=api_key, environment=environment)
            if self.index_name not in pinecone.list_indexes():
                raise ValueError(f"Index {self.index_name} does not exist.")
            self.index = pinecone.Index(self.index_name)
            self.connected = True
        except Exception as e:
            logging.error(f"Failed to initialize Pinecone: {e}")

    def upsert_vectors(self, vectors: List[Dict[str, Any]], namespace: str = "") -> bool:
        """Upserts a list of vector dicts (id, values, metadata) to the index."""
        if not self.connected:
            logging.warning("Not connected to Pinecone. Skipping upsert.")
            return False
            
        try:
            self.index.upsert(vectors=vectors, namespace=namespace)
            return True
        except Exception as e:
            logging.error(f"Upsert failed: {e}")
            return False

    def query(self, vector: List[float], top_k: int = 5, namespace: str = "") -> Dict:
        """Queries the index for the most similar vectors."""
        if not self.connected:
            return {"matches": []}
            
        try:
            results = self.index.query(
                vector=vector,
                top_k=top_k,
                include_metadata=True,
                namespace=namespace
            )
            return results
        except Exception as e:
            logging.error(f"Query failed: {e}")
            return {"matches": []}

if __name__ == "__main__":
    # Mock execution
    print("Pinecone connector initialized.")
