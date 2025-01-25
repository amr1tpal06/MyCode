from flask import request, jsonify
from config import app, db
from models import Book, Author
import json
from sqlalchemy import func 

@app.route("/borrowed", methods=["GET"])
def get_borrowed_books():
    borrowed_books=Book.query.filter_by(status="borrowed").all()   
    return jsonify([book.to_json() for book in borrowed_books])

@app.route("/add-book", methods=["POST"])
def add_book():
    # Log incoming data
    print("Incoming form data:", request.form)

    # Retrieve form data
    title = request.form.get("title")
    author = request.form.get("author")
    genre = request.form.get("genre")
    pages = request.form.get("pages")
    rating = request.form.get("rating")
    publicationyear = request.form.get("publicationyear")
    audience = request.form.get("audience")
    imagepath = request.form.get("imagepath")
    status= "available"
    summary= "summary"
    #onyl want to enter some of the fields and not all of them though

    # Validate form data
    if not all([title, author, genre, pages, rating, publicationyear, audience, imagepath, status, summary]):
        print("Missing fields detected!")
        return jsonify({"error": "All fields are required"}), 400

    # Log data after validation
    print("Validated data:", title, author, genre, pages, rating, publicationyear, audience, imagepath, status, summary)

    # Create a new Book instance
    try:
        book = Book(
            title=title,
            author=author,
            genre=genre,
            pages=pages,
            rating=rating,
            publicationyear=publicationyear,
            audience=audience,
            imagepath=imagepath,
            status= status,
            summary=summary
        )
        
        # Add the book to the database
        db.session.add(book)
        db.session.commit()
        print("Book added successfully!")
        return jsonify({"message": "Book added successfully!"}), 201
    except Exception as e:
        # Catch and log database errors
        print("Error while adding book:", str(e))
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/delete-book/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": f"Book with id {book_id} deleted successfully!"}), 200

@app.route("/borrow-book/<int:book_id>", methods=["PATCH"])
def borrow_book(book_id):
    book = Book.query.get(book_id)
    book.status = "borrowed"
    db.session.commit()
    return jsonify({"message": f"Book with id {book_id} borrowed successfully!"}), 200

@app.route("/return-book/<int:book_id>", methods=["PATCH"])
def return_book(book_id):
    book = Book.query.get(book_id)
    book.status = "available"
    db.session.commit()
    return jsonify({"message": f"Book with id {book_id} returned successfully!"}), 200

@app.route("/least-pages", methods=["GET"])
def least_pages():
    leastpages= db.session.query(Book).order_by(Book.pages.desc()).first()

    if leastpages:
        return jsonify({
            'title': leastpages.title,
            'author': leastpages.author,
            'rating': leastpages.rating
        })
    else:
        return jsonify({'message': 'No books found in the database'})

@app.route("/most-pages", methods=["GET"])
def most_pages():
    mostpages= db.session.query(Book).order_by(Book.pages.asc()).first()

    if mostpages:
        return jsonify({
            'title': mostpages.title,
            'author': mostpages.author,
            'rating': mostpages.rating
        })
    else:
        return jsonify({'message': 'No books found in the database'})

@app.route("/lowest-rated", methods=["GET"])
def get_lowest():
    lowest = db.session.query(Book).order_by(Book.rating.asc()).first()
    
    if lowest:
        return jsonify({
            'title': lowest.title,
            'author': lowest.author,
            'rating': lowest.rating
        })
    else:
        return jsonify({'message': 'No books found in the database'})

@app.route("/highest-rated", methods=["GET"])
def get_highest():
    highest = db.session.query(Book).order_by(Book.rating.desc()).first()  
    if highest:
        return jsonify({
            'title': highest.title,
            'author': highest.author,
            'rating': highest.rating
        }) 
    else:
        return jsonify({'message': 'No books found in the database'})

@app.route("/books-by-genre", methods=["GET"])
def books_by_genre():
    genre_count = db.session.query(Book.genre, func.count(Book.id)).group_by(Book.genre).all()
    genre_list = [{genre: count} for genre, count in genre_count]
    return jsonify(genre_list)

@app.route ("/books-by-author", methods =["GET"])
def books_by_author():
    author_count= db.session.query(Book.author, func.count(Book.id)).group_by(Book.author).all()
    author_list= [{author: count} for author, count in author_count]
    return jsonify (author_list)

@app.route("/attributes", methods=["GET"])
def get_attributes():
    attributes = [column.name for column in Book.__table__.columns]
    return jsonify(attributes)

@app.route("/<string:category>", methods=["GET"])
def get_values(category):
    column = getattr(Book, category)
    values = db.session.query(column).distinct().all()
    values_list = [getattr(value, category) for value in values]
    return jsonify(values_list)

@app.route("/filter-by/<string:category>/<string:encodedUserinput>", methods=["GET"])
def filter_by(category, encodedUserinput):
   filter_condition = getattr(Book, category) == encodedUserinput
   items = Book.query.filter(filter_condition).all()
   return jsonify([item.to_json() for item in items]) 

@app.route("/", methods=["GET"])
def view_books():
    with open('/Users/amrit/Desktop/MyCode/Backend /books.json', 'r') as file:
        data = json.load(file)

    author_data=data["authors"]
    books_data=data["books"]
    
    for author in author_data:
        new_author= Author(name=author)
        db.session.add(new_author)
    db.session.commit()

    for book in books_data:
        # Check if a book with the same title and author already exists
        
        existing_book = Book.query.filter_by(title=book["title"]).first()
        if existing_book:
            print(f"Book '{book['title']}' already exists.")
            continue 
        author = Author.query.filter_by(name=book["author"]).first()

        # Add new book if it doesn't already exist
        new_book = Book(
            title=book["title"],
            author=author, #author
            genre=book["genre"],
            pages=book["pages"],
            rating=book["rating"],
            publicationyear=book["publicationyear"],
            audience=book["audience"],
            imagepath=book["imagepath"],
            status=book["status"],
            summary=book["summary"]
        )
        db.session.add(new_book)
    db.session.commit()

    # Fetch all books to display
    books = Book.query.filter_by(status="available").all()
    json_books = [book.to_json() for book in books]
    return jsonify(json_books)

@app.route("/<int:book_id>", methods =["GET"])
def getbook(book_id):
    #code to get specific book by id 
    book= Book.query.get(book_id)
    if book:
        return book.to_json()

@app.route("/test-post", methods=["POST"])
def test_post():
    return jsonify({"message": "POST request received!"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)

