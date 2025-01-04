from flask import request, jsonify
from config import app, db
from models import Book
import json

@app.route("/", methods=["GET"])
def view_books():
    db.session.query(Book).delete()
    db.session.commit()
    with open('/Users/amrit/Desktop/MyCode/Backend /books.json', 'r') as file:
        books_data = json.load(file)
    
    for book in books_data:
        new_book = Book(
            id=book["id"],
            title=book["title"],
            author=book["author"],
            genre=book["genre"],
            pages=book["pages"],
            rating=book["rating"],
            publicationyear=book["publicationyear"],
            audience=book['audience'],
            imagepath=book["imagepath"]
        )
        db.session.add(new_book)
        db.session.commit()

    books = Book.query.all()
    json_books = [book.to_json() for book in books]
    return jsonify(json_books)

@app.route("/filter-by-genre", methods=["GET"])
def view_by_genre():
    genre = request.args.get('genre')
    genrelist = Book.query.filter_by(genre=genre).all()
    json_genre = [book.to_json() for book in genrelist]
    return jsonify({genre: json_genre})

@app.route("/delete-book", methods=["POST"])
def delete_book():
    userrequest = request.get_json()
    title = userrequest.get("title")
    book_to_delete = Book.query.filter_by(title=title).first()
    if book_to_delete:
        db.session.delete(book_to_delete)
        db.session.commit()
        return jsonify({"message": f"Book '{title}' deleted successfully."}), 200
    else:
        return jsonify({"error": "Book not found."}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5000)


'''#CRUD- routes (API) #create,read, update and delete 
from flask import request, jsonify #request is the data sent from the frontend 
from config import app, db
from models import Book
import json

if __name__ == '__main__':
    app.run(debug=True, port=5000)

#endpoints 
@app.route("/", methods= ["GET"])
def view_books():
    with open ('./Backend/books.json','r') as file:
        books_data= json.load(file)
    
    for book in books_data:
        book= Book(id=book["id"],title=Book["title"], author=Book["author"], genre=Book["genre"], pages= Book["pages"], rating=Book["rating"], publicationyear= book["publicationyear"], audience=Book['audience'], imagepath=Book["imagepath"]) #add the rest attributes 
        db.session.add(book)
        db.session.commit()

    # Query all books
    books = Book.query.all()  # List of Book instances - rows
    # Convert each book to JSON
    json_books = [book.to_json() for book in books]
    # Return as JSON response
    return jsonify(json_books)

@app.route("/filter-by-genre")
def view_by_genre():
    genrerequest = request.get_json()
    genre=genrerequest.get('genre')
    genrelist= Book.query.filter_by(genre).all()
    json_genre =[book.to_json() for book in genrelist]
    return jsonify({genre: json_genre})

@app.route("/delete-book")
def delete_book():
    userrequest= request.to_json()
    delete= userrequest.query.get("title")
    db.session.delete(delete)
    db.session.commit()'''

'''@app.route('/add_user')

def add_user():
    # Get the data sent from the frontend
    data = request.get_json()  # Parse the incoming JSON data

    # Get the name and email from the request body
    name = data.get('name')
    email = data.get('email')

    # Ensure the required fields are present
    if not name or not email:
        return jsonify({"error": "Missing required fields"}), 400

    # Create a new user instance
    new_user = User(name=name, email=email)

    # Add the new user to the database session
    db.session.add(new_user)

    # Commit the transaction (save to the database)
    db.session.commit() '''


'''querying data using Python syntax 
(Book.query.all(), Book.query.filter_by(author="JK Rowling").all(), etc.).'''



'''
@app.route("/add-book", methods= "")
    def add_book()

@app.route("/delete-book", methods="")
    def delete_book ()

@app.route("/filter-by-genre") #to_json converts into dictionary and jsonfiy takes dcitionary and formats in json response '''

