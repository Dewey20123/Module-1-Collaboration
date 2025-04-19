from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Book Model
class Book(BaseModel):
    id: int
    book_name: str
    author: str
    publisher: str

# In-memory storage (like a mock database)
books = []

# Home route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API!"}

# Get all books
@app.get("/books")
def get_books():
    return books

# Get book by ID
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# Create a book
@app.post("/books")
def create_book(book: Book):
    for b in books:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail="Book ID already exists")
    books.append(book)
    return book

# Update a book
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books):
        if book.id == book_id:
            books[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

# Delete a book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            deleted_book = books.pop(index)
            return {"message": "Book deleted", "book": deleted_book}
    raise HTTPException(status_code=404, detail="Book not found")