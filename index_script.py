import lancedb
import ollama
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import get_registry

#import lancedb
import os

db = lancedb.connect("/tmp/db")
func = get_registry().get("ollama").create(name="nomic-embed-text")

class CodeChunks(LanceModel):
    filename: str
    text: str = func.SourceField()
    # 1536 is the embedding dimension of the `voyage-code-2` model.
    vector: Vector(768) = func.VectorField()

table = db.create_table("code_chunks", schema=CodeChunks, mode="overwrite")
table.add([
    {"text": "print('hello world!')", "filename": "hello.py"},
    {"text": "print('goodbye world!')", "filename": "goodbye.py"}
])

query = "greetings"
actual = table.search(query).limit(1).to_pydantic(CodeChunks)[0]
print(actual.text)

query = "farewells"
actual = table.search(query).limit(1).to_pydantic(CodeChunks)[0]
print(actual.text)
