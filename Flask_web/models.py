from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Database(db.Model):
    __tablename__ = "database"  # 기본적으로 테이블 이름은 자동으로 정의되지만 이 처럼 명시적으로 정할 수 있다.

    id = db.Column(db.Integer, primary_key=True)
    shop = db.Column(db.String(30))
    address = db.Column(db.String(50))
    sector = db.Column(db.String(10))
    menu = db.Column(db.String(255))
    latitude = db.Column(db.String(30))
    longitude = db.Column(db.String(30))