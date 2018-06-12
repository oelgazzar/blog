from . import app, db
from .models import Post, Comment
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required


@app.route('/')
def index():
    posts = Post.query.all()
    posts.sort(key=lambda p: p.pub_date, reverse=True)
    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>', methods=['GET', 'POST'])
def detail(post_id):
	post = Post.query.get(post_id)
	if request.method == 'POST': # add comment
		c = Comment(name=request.form.get('name'),
			body=request.form.get('body'), post=post)
		db.session.commit()
		return redirect(url_for('detail', post_id=post_id))
	return render_template('detail.html', post=post, comments=post.comments)

@app.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        new_post = Post(title=title, body=body)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('detail', post_id=new_post.id))
    else:  # GET
        return render_template('new.html')


@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit(post_id):
    post = Post.query.get(post_id)
    if request.method == 'POST':
        post.title = request.form.get('title')
        post.body = request.form.get('body')
        db.session.commit()
        return redirect(url_for('detail', post_id=post_id))
    else:  # GET
        return render_template('edit.html', post=post)


@app.route('/delete/<int:post_id>')
@login_required
def delete(post_id):

    post_del = Post.query.filter(Post.id == post_id).delete()
    db.session.commit()
    msg = 'Post Has been Deleted'

    return redirect(url_for('index'))
