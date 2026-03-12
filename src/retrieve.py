import faiss    
import numpy as np

def build_faiss_index(embeddings: np.ndarray) -> faiss.IndexFlatL2:
    """Build a FAISS index from the given embeddings."""
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

def search_faiss_index(index, query_embedding: np.ndarray, top_k: int = 5) -> list[int]:
    """Search the FAISS index for the nearest neighbors of the query embedding."""
    distances, indices = index.search(query_embedding.reshape(1, -1), top_k)
    return indices[0].tolist()  