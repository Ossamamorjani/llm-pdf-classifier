def chunk_text(text: str, chunk_size: int = 800, overlap: int = 100) -> list[str]:
    """Chunk text into smaller pieces with optional overlap."""
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks