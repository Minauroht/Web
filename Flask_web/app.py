from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
import os
from models import database, bookreview, db
from flask_sqlalchemy import SQLAlchemy
import json
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)#

basdir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basdir, "bookdata.db")#'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookdata.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'jqiowejrojzxcovnklqnweiorjqwoijroi'
engine = create_engine('sqlite:///bookdata.db')
Session = sessionmaker(bind=engine)
session = Session()

db.init_app(app)
db.app = app


# 목록에 리뷰 저장
reviews = []

@app.route('/')
def index():
    # 리뷰 양식을 렌더링
    return render_template('review_form.html')

@app.route('/submit_review', methods=['GET', 'POST'])
def submit_review():
    if request.method == 'POST':
    #양식 데이터 가져오기
        title = request.form['title']
        author = request.form['author']
        review = request.form['review']
        book = bookreview(title=title, author=author, review=review)
        db.session.add(book)
        db.session.commit()
    # 리뷰를 목록에 추가
        reviews.append({'title': title, 'author': author, 'review': review})
    #리뷰 목록 페이지로 리디렉션
        return redirect(url_for('review_list'))

    # 요청 방법이 GET인 경우 검토 양식 렌더링
    return render_template('review_form.html')

@app.route('/reviews', methods=['GET', 'POST'])
def review_list():
        # 데이터베이스에서 모든 리뷰 검색
    reviews = bookreview.query.all()

    # 리뷰 데이터로 리뷰 목록 템플릿 렌더링
    return render_template('review_list.html', reviews=reviews)

@app.route('/topic')
def topic():
    return render_template('topic.html')

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        topic = request.form['topic']
        return render_template('post.html', topic=topic)
    return render_template('post.html')

@app.route('/reply', methods=['GET', 'POST'])
def reply():
    if request.method == 'POST':
        answer = request.form['answer']
        return render_template('reply.html', answer=answer)
    return render_template('reply.html')

@app.before_first_request
def create_database():
     db.create_all()
     #db.session.query(bookreview).delete() #<--이거 켜면 데이터 다 날아감. 주석 취소할 때 주의할 것.
     db.session.commit()


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port=5000)