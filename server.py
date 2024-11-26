"""
This is an example of a server that can be used with the "http" context provider.
"""

from fastapi import FastAPI
from pydantic import BaseModel


class ContextProviderInput(BaseModel):
    query: str
    fullInput: str


app = FastAPI()


@app.post("/retrieve")
async def create_item(item: ContextProviderInput):
    results = [] # TODO: Query your vector database here.

    # Construct the "context item" format expected by Continue
    context_items = []
    for result in results:
        context_items.append({
            "name": result.filename,
            "description": result.filename,
            "content": result.text,
        })

    return context_items

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)