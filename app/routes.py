from . import app, db
from .models import Post, Comment
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required
from .forms import PostForm, images


@app.route('/')
def index():
    posts = Post.query.all()
    posts.sort(key=lambda p: p.pub_date, reverse=True)
    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>', methods=['GET', 'POST'])
def detail(post_id):
    post = Post.query.get(post_id)
    if request.method == 'POST':  # add comment
        c = Comment(name=request.form.get('name'),
                    body=request.form.get('body'), post=post)
        db.session.commit()
        return redirect(url_for('detail', post_id=post_id))
    return render_template('detail.html', post=post, comments=post.comments)


@app.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    form = PostForm()
    if request.method == 'POST' and form.validate():

        title = form.title.data
        body = form.body.data
        filename = images.save(request.files['image'])
        file_url = images.url(filename)
        new_post = Post(title=title, body=body, filename=filename, file_url=file_url)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('detail', post_id=new_post.id))
    else:  # GET
        return render_template('new.html', form=form)


@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit(post_id):
    form = PostForm()
    post = Post.query.get(post_id)
    if request.method == 'POST':
        post.title = form.title.data
        post.body = form.body.data
        db.session.commit()
        return redirect(url_for('detail', post_id=post_id))
    else:  # GET
        return render_template('edit.html', post=post, form=form)


@app.route('/delete/<int:post_id>')
@login_required
def delete(post_id):

    post_del = Post.query.filter(Post.id == post_id).delete()
    db.session.commit()
    msg = 'Post Has been Deleted'

    return redirect(url_for('index'))
