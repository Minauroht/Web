from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class bookreview(db.Model):
    __tablename__ = "Book Review" 
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    review = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

class database(db.Model):
    __tablename__ = "database"  

    id = db.Column(db.Integer, primary_key=True)
    shop = db.Column(db.String(30))
    address = db.Column(db.String(50))
    sector = db.Column(db.String(10))
    menu = db.Column(db.String(255))
    latitude = db.Column(db.String(30))
    longitude = db.Column(db.String(30))
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    review = db.Column(db.Text, nullable=False)
    author = db.Column(db.Text, nullable=False)