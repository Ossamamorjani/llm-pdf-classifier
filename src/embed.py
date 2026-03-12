import os
import numpy as np
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

def embed_texts(texts: list[str], model: str = "text-embedding-3-small") -> np.ndarray:
    """Embed a list of texts using OpenAI's embedding API."""
    embeddings = []

    for text in texts:
        response = client.embeddings.create(input=[text], model=model)
        embeddings.append(response.data[0].embedding)

    return np.array(embeddings)