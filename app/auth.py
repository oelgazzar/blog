# imports
from . import app, db
from .models import User
from flask import render_template, redirect, url_for, request, Blueprint, flash, session
from flask_login import current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.urls import url_parse

# define blueprint for urls related to authentication
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    a view for registering the user
    When GET: return the register page
    When POST: processing data after submitting and if valid save it to the database
    if there is any error return to register page and flash the error

    """
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
    else:
        return render_template('auth/register.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Check if the user is logged in, if logged in redirect to the index page
    If not logged in, validate the data entered, if valid redirect the user to the requested page or to the index
    """
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        all_identical_users = User.query.filter(User.username == username).first()
        error = None

        if not username:
            error = 'USERNAME is required Ya Dog :) '

        elif all_identical_users is None:
            error = 'User Not Registered'
        elif not check_password_hash(user.password, password):
            error = 'Incorrect password Ya Animal :) '

        if error is not None:
            flash(error)
            return render_template('auth/login.html', error=error,
                                   all_identical_users=all_identical_users)
        else:
            # login and remember the user
            login_user(user, remember=True)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)

    return render_template('auth/login.html')


@bp.route('/logout')
def logout():
    """
    Allow the user to logout
    """
    logout_user()
    return redirect(url_for('index'))
