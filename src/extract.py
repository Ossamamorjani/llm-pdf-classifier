import pypdf

def extract_text(path: str) -> str:
    reader = pypdf.PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text