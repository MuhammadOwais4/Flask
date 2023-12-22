
from flask import Flask, jsonify, request

app = Flask(__name__)

# Simple data of books
books = [
    {"id": 1, "title": "book 1", "Author": "Author1"},
    {"id": 2, "title": "book 2", "Author": "Author2"},
    {"id": 3, "title": "book 3", "Author": "Author3"},
]

# Get a specific book by id
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
    return jsonify({'error': "Book not found"})

# Create a book
@app.route('/books', methods=['POST'])
def create_book():
    new_book = {'id': len(books) + 1, 'title': request.json['title'], 'Author': request.json['Author']}
    books.append(new_book)
    return jsonify(new_book)

# Update a book
@app.route("/books/update/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    for book in books:
        if book['id'] == book_id:
            book['title'] = request.json['title']  
            book['Author'] = request.json['Author']  
            return jsonify(book)
    return jsonify({'error': 'Book not found'})
#  delete a book
@app.route("/books/delete/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    global books
    books = list(filter(lambda x: x['id'] != book_id, books))
    return jsonify({"message":"Book deleted successfully!"})

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

if __name__ == '__main__':
    app.run(
        port=3000,
        debug=True
    )
