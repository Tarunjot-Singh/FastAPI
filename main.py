from fastapi import FastAPI, File, UploadFile, Query
from fastapi import FastAPI, Query
from embedding import validate_text, get_embedding

from validate_data import process_csv, validate_csv

app = FastAPI()


@app.post("/csv")
async def process_csv_route(file: UploadFile = File(...), equals: str = Query(None)):
    contents = await file.read()
    validate_csv(file)
    return process_csv(contents.decode(), equals)

@app.get("/embedding")
async def get_text_embedding(text: str = Query(...)):
    validate_text(text)
    return {"embedding": get_embedding(text)}