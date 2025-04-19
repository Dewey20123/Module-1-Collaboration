from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database"
books = []

# Home route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Book API!"})

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Get book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.json
    for book in books:
        if book['id'] == data['id']:
            return jsonify({'error': 'Book ID already exists'}), 400
    books.append(data)
    return jsonify(data), 201

# Update an existing book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    for index, book in enumerate(books):
        if book['id'] == book_id:
            books[index] = data
            return jsonify(data)
    return jsonify({'error': 'Book not found'}), 404

# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for index, book in enumerate(books):
        if book['id'] == book_id:
            deleted = books.pop(index)
            return jsonify({'message': 'Book deleted', 'book': deleted})
    return jsonify({'error': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)