import unittest 
from config import app, db
from sqlalchemy import func
import json
from models import Book, Author, Genre
import os
import pytest

@pytest.fixture
def setup():
    #create testing environment
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
    app.config["TESTING"]=True

    with app.app_context():
        db.create_all() 
    yield db

def test_addanddeletebook(setup):
    new_book = Book(
        title="sample title", 
        author_id=1, 
        pages=100, 
        genre_id=1,
        rating=5, 
        publicationyear=2021, 
        audience="adult", 
        imagepath="imagepath", 
        status="available", 
        summary="summary"
    )
    with app.app_context():
        db.session.add(new_book)
        db.session.commit()

        book=Book.query.filter_by(title="sample title").first()
        assert book.title=="sample title"
        db.session.delete(new_book)
        db.session.commit()

def test_borrow_book():
    with app.app_context():
        book=Book.query.filter_by(title="sample title").first()
        book.status="borrowed"
        db.session.commit()
        assert book.status=="borrowed"
    
def test_return_book():
    with app.app_context():
        book=Book.query.filter_by(title="sample title").first()
        book.status="returned"
        db.session.commit()
        assert book.status=="returned"

def test_addanddeleteauthor(setup):
    new_author = Author(name="sample author")
    with app.app_context():
        db.session.add(new_author)
        db.session.commit()

        author=Author.query.filter_by(name="sample author").first()
        assert author.name=="sample author"
        db.session.delete(new_author)
        db.session.commit()

def test_addanddeletegenre(setup):
    new_genre = Genre(genre="sample genre", description="sample description")
    with app.app_context():
        db.session.add(new_genre)
        db.session.commit()

        genre=Genre.query.filter_by(genre="sample genre").first()
        assert genre.genre=="sample genre"
        db.session.delete(new_genre)
        db.session.commit()