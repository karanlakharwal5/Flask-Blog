from flask import render_template, url_for, flash, redirect
from FlaskBlog import app
from FlaskBlog.forms import RegistrationForm, LoginForm
from FlaskBlog.models import User, Post


posts = [
    {
        'author': 'Karan Lakharwal',
        'title': 'The Gutsy Ninja',
        'content': 'First Content',
        'data_posted': 'September 10, 2020'
    },
    {
        'author': 'Joey Tribbiani',
        'title': 'How you Doin!',
        'content': 'Regular Content',
        'data_posted': 'January 15, 2020'
    }
]


@app.route('/')  # home page for our website
@app.route('/home')  # set / and /home link to go to home page
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')  # home page for our website
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])  # register for our website
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])  # login route  for our website
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
