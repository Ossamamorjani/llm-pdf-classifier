import numpy as np
from openai import OpenAI
from src.extract import extract_text
from src.chunk import chunk_text
from src.embed import embed_texts
from src.retrieve import build_faiss_index, search_faiss_index

client = OpenAI()

def main(pdf_path: str, question: str, top_k = 5) -> dict:
    # Step 1: Extract text from PDF
    text = extract_text(pdf_path)

    # Step 2: Chunk the text
    chunks = chunk_text(text)

    # Step 3: Embed the chunks
    embeddings = embed_texts(chunks)

    # Step 4: Build FAISS index
    index = build_faiss_index(embeddings)

    # Step 5: Embed the query
    query_embedding = embed_texts([question])[0]  

    # Step 6: Search FAISS index
    top_k_indices = search_faiss_index(index, query_embedding, top_k=top_k)
    
    # Step 7: Retrieve the top-k relevant chunks
    retrieved_chunks = [chunks[idx] for idx in top_k_indices]

    # Step 8: Build context for the LLM
    context = " ".join(retrieved_chunks)
    
    # Step 9: Generate answer using the LLM
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", 
             "content": "Answer the user's question using only the provided context. "
             "If the answer is not in the context, say 'I don't know.'"
             },
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{question}"
             } ]
    )
    return {
        "answer": response.choices[0].message.content,
        "sources": top_k_indices, 
        "retrieved_chunks": retrieved_chunks
    }