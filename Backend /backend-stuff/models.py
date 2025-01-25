from config import db
#author can have many books , book has one author , many-to-one relationship
#book can have many genres, one-to-many relationship
# create realtionships, loading from a file, and then finish off 

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname= db.Column(db.String(100), nullable=False)
    surname= db.Column(db.String(100), nullable=False)
    books = db.relationship('Book', backref='author', lazy=True)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genres = db.relationship('Genre', backref='book', lazy=True)
    pages = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.String(100), nullable=False)
    publicationyear = db.Column(db.String(100), nullable=False)
    audience = db.Column(db.String(100), nullable=False)
    imagepath = db.Column(db.String(100), nullable=False)
    status= db.Column(db.String(100), nullable=True)
    summary= db.Column(db.String(100), nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "pages": self.pages,
            "rating": self.rating,
            "publicationyear": self.publicationyear,
            "audience": self.audience,
            "imagepath": self.imagepath,
            "status": self.status,
            "summary":self.summary
        }

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)