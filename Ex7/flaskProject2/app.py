from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def main_func():
    return 'Welcome to the main page!'


@app.route('/about')
def about_func():
    return 'Welcome to the about page!'


@app.route('/contact us')
def contact_func():
    return redirect(url_for('about_func()'))


if __name__ == '__main__':
    app.run()
