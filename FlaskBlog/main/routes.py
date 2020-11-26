from flask import render_template, request, Blueprint
from FlaskBlog.models import Post
main = Blueprint('main',__name__)


@main.route('/')  # home page for our website
@main.route('/home')  # set / and /home link to go to home page
def home():
    page = request.args.get('page',1,type=int)
    posts =Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route('/about')  # home page for our website
def about():
    return render_template('about.html', title='About')
