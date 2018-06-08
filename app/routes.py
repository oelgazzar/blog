from . import app, db
from .models import Post
from flask import render_template, redirect, url_for, request


@app.route('/')
def index():
    posts = Post.query.all()
    posts.sort(key=lambda p: p.pub_date, reverse=True)
    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>')
def detail(post_id):
    post = Post.query.get(post_id)
    return render_template('detail.html', post=post)


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        new_post = Post(title=title, body=body)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('index'))
    else:  # GET
        return render_template('new.html')


@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    post = Post.query.get(post_id)
    if request.method == 'POST':
        post.title = request.form.get('title')
        post.body = request.form.get('body')
        db.session.commit()
        return redirect(url_for('detail', post_id=post_id))
    else:  # GET
        return render_template('edit.html', post=post)
