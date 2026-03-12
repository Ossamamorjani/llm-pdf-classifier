# PDF RAG Assistant

## Overview 

This project implements a modular Retrieval-Augmented Generation (RAG) system that allows users to ask questions about PDF documents.
Instead of relying solely on an LLM’s internal knowledge, the system retrieves relevant information directly from the source document and uses it to generate grounded answers.

The pipeline includes:
- PDF text extraction
- Semantic chunking
- Vector embeddings
- FAISS vector indexing
- Query embedding
- Semantic retrieval
- LLM grounded response generation

This architecture improves factual accuracy and reduces hallucinations by ensuring answers are based on the document content.


## Architecture 

The system follows a standard RAG pipeline:

1. PDF Document
2. Text Extraction
3. Chunking
4. Embeddings
5. FAISS Vector Index
6. Query Embedding
7. Semantic Retrieval (Top-k chunks)
8. Grounded LLM Answer

## Project Structure 

llm-pdf-classifier
data
- raw                # Input PDF files
- processed          # Generated embeddings / indexes

notebooks              # Development notebooks

src
- extract.py         # Extract text from PDF
- chunk.py           # Split text into chunks
- embed.py           # Generate embeddings
- retrieve.py        # FAISS vector retrieval
- app.py             # Main RAG pipeline

requirements.txt

README.md

.env.example

Each module is separated to keep the pipeline clean and maintainable.  
This modular design makes it easy to extend or swap components such as the embedding model or vector database.


## How It Works 

1. A PDF document is ingested and text is extracted.
2. The text is split into smaller chunks to improve retrieval precision.
3. Each chunk is converted into a vector embedding.
4. The embeddings are stored in a FAISS vector index.
5. When a user asks a question, the query is also embedded.
6. FAISS performs semantic similarity search to retrieve the most relevant chunks.
7. The retrieved chunks are passed to the LLM.
8. The LLM generates a grounded answer based on the retrieved context.


## Usage

Run the main pipeline:

- '''bash
- python src/app.py


## Example Output

Example Question:
> What is the main idea behind the Transformer architecture?

Example System Output:
The Transformer architecture introduces a mechanism called self-attention, whcih allows the model to weight the importance of different words in a sequence relative to each other. Unlike pervious sequence models such as RNNs or LSTMs, the Transformer processes all tokens in parallel, enabling greater computational efficiency and better performance on long-range dependencies.

Sources: [Chunk 3, Chunk 8]

## Future Improvements

Possible extensions include:

- Support for indexing multiple PDF documents  
- Metadata-aware retrieval (document title, section, page)  
- Hybrid retrieval combining semantic search and keyword search (BM25)  
- Streaming responses for faster interaction  
- Evaluation of retrieval quality using metrics such as recall@k  
- A simple web interface for document interaction  

Future versions of this project aim to evolve the system into a **multi-document AI research assistant** capable of comparing information across several academic papers.



