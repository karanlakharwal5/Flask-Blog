
from FlaskBlog import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)  # now can be run via cmd as: python FlaskBlog.py
