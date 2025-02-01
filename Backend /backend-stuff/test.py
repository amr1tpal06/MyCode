import unittest 
from config import app, db
from sqlalchemy import func
import json
from models import Book, Author, Genre

#create testing environment 
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///:memory:"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["TESTING"]=True

with app.app_context():
        db.create_all()  
yield db
with app.app_context():
    db.session.remove()  
    db.drop_all()

def test_add_book():
    new_book=Book("sample title",1,1,100,5,2021,"adult","imagepath","available","summary")
    db.session.add(new_book)
    db.session.commit()

    book=Book.query.filter_by(title="sample title").first()
    assert book.title=="sample title"