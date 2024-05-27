from fastapi import HTTPException
from sentence_transformers import SentenceTransformer

def validate_text(text: str):
    # Validate that the text input contains more than 5 characters
    if len(text.strip()) <= 5:
        raise HTTPException(status_code=400, detail="Text must contain more than 5 characters")

def get_embedding(text: str):
    # Use an embedding model from Sentence Transformers library
    model = SentenceTransformer('bert-base-nli-mean-tokens')
    # Strip trailing and leading whitespace from the "text" value
    embedding = model.encode([text.strip()])[0]
    return embedding.tolist()
