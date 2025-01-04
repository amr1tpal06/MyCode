'''from config import db #instance of database 

class Book(db.Model): 
    id=db.Column(db.Integer, primary_key= True)
    title=db.Column(db.String(100), unique=False,nullable=False )
    author=db.Column(db.String(100), unique=False,nullable=False )
    genre=db.Column(db.String(100), unique=False,nullable=False )
    pages=db.Column(db.String(100), unique=False,nullable=False )
    rating=db.Column(db.String(100), unique=False,nullable=False )
    publicationyear=db.Column(db.String(100), unique=False,nullable=False )
    audience=db.Column(db.String(100), unique=False,nullable=False )
    imagepath=db.Column(db.String(100), unique=False,nullable=False )

    def to_json(self): #take object and convert to python dictionary -->json(for API)
        return {
            "id":self.id,
            "title":self.title,
            "author":self.author,
            "genre":self.genre,
            "pages":self.pages,
            "rating":self.rating, 
            #"language":self.language,
            "publicationyear":self.publicationyear,
            "audience":self.audience,
            "format":self.format, 
            #"duedate":self.duedate,
            #"borrower":self.borrower, 
            #"borrower":False,
            #"borroweddate":self.borroweddate,
            #"returndate":self.returndate
        }'''


from config import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    pages = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.String(100), nullable=False)
    publicationyear = db.Column(db.String(100), nullable=False)
    audience = db.Column(db.String(100), nullable=False)
    imagepath = db.Column(db.String(100), nullable=False)

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
            "imagepath": self.imagepath
        }

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname= db.Column(db.String(100), nullable=False)
    surname= db.Column(db.String(100), nullable=False)
    books= db.Column(db.String(100), nullable=False)

