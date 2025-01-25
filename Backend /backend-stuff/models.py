from config import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    #genres = db.relationship('Genre', backref='book', lazy=True)
    pages = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.String(100), nullable=False)
    publicationyear = db.Column(db.String(100), nullable=False)
    audience = db.Column(db.String(100), nullable=False)
    imagepath = db.Column(db.String(100), nullable=False)
    status= db.Column(db.String(100), nullable=True)
    summary= db.Column(db.String(100), nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False) #each book has an author

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author.name,
            "genre": self.genre,
            "pages": self.pages,
            "rating": self.rating,
            "publicationyear": self.publicationyear,
            "audience": self.audience,
            "imagepath": self.imagepath,
            "status": self.status,
            "summary":self.summary
        }

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100), nullable=False)
    books= db.relationship('Book', backref="author", lazy=True)

    def to_json(self):
        return {
            "name": self.name
        }

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    #book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)

#one book has one author, but one author can have many books - one to many (author to book)
#one genre can have many books, one book can have many genres - many to many (genre to book)
#many to many is linking table