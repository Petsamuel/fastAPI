
from fastapi import FastAPI


app= FastAPI (
    
    title="BOOK API",
    description="simple",
    docs_url="/"
)


@app.get("/books")
async def fetch_user():
    pass

@app.post("/books")
async def register_user():
    pass

@app.put("/books/{book_id}")
async def register_user(book_id):
    pass

@app.delete("/books/{book_id}")
async def register_user(book_id):
    pass

