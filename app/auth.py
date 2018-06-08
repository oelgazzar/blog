from . import app, db
from .models import User
from flask import render_template, redirect, url_for, request, Blueprint, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        identical_user = User.query.filter(User.username == username).first()
        error = None

        if not username:
            error = 'Username field is qequired'
        elif identical_user is not None:
            error = 'This username is already registered'
        elif not password:
            error = 'password field is required'

        if error is not None:
            return render_template('auth/register.html', error=error)
        else:
            new_user = User(username=username, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('auth.login'))
        # flash(error)
    else:
        return render_template('auth/register.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        all_identical_users = User.query.filter(User.username == username).first()
        error = None

        if not username:
            error = 'USERNAME is required Ya Dog :) '
        # To check if the password not correct ???
        # elif username not in
        elif all_identical_users is None:
            error = 'User Not Registered'
        elif not check_password_hash(user.password, password):
            error = 'Incorrect password Ya Animal :) '

        if error is not None:
            flash(error)
            return render_template('auth/login.html', error=error,
                                   all_identical_users=all_identical_users)
        else:
            # create new session
            session.clear()
            session['user-id'] = user.id
            return redirect(url_for('index'))

    return render_template('auth/login.html')
