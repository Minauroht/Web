from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
import os
from models import database, bookreview, db
from flask_sqlalchemy import SQLAlchemy
import json
import sqlite3

app = Flask(__name__)#

basdir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basdir, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookdata.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'jqiowejrojzxcovnklqnweiorjqwoijroi'

db.init_app(app)
db.app = app


# store reviews in a list
reviews = []

@app.route('/')
def index():
    # render the review form
    return render_template('review_form.html')

@app.route('/submit_review', methods=['GET', 'POST'])
def submit_review():
    if request.method == 'POST':
    # get the form data
        title = request.form['title']
        author = request.form['author']
        review = request.form['review']
        book = bookreview(title=title, author=author, review=review)
        db.session.add(book)
        db.session.commit()
    # add the review to the list
        reviews.append({'title': title, 'author': author, 'review': review})
    # redirect to the review list page
        return redirect(url_for('review_list'))

@app.route('/reviews')
def review_list():
    # render the review list template with the reviews data
    return render_template('review_list.html', reviews=reviews)

##########
"""@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = Post(title=title, content=content)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('view_post', post_id=post.id))
    else:
        return render_template('create_post.html')

@app.route('/post/<int:post_id>')
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('view_post.html', post=post)"""
##########

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
     db.session.commit()


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port=5000)