from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import json
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(150), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"{self.book_name} - {self.author} ^ {self.publisher}"

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return 'Hello!'

@app.route('/books')
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        bookData = {'id': book.id, 'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher }
        output.append(bookData)
    return {'books': output}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {'id': book.id, 'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher}  #don't have to jsonify because dictionaries are instantly serializable

@app.route('/books/', methods=['POST'])
def add_book():
    book = Book(book_name=request.json['book_name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

@app.route('/books/<id>', methods=['DELETE'])
def delete_drink(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "book not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": f"entry under id {id} has been deleted"}