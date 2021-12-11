from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def main_func():  # put application's code here
    return 'Welcome to the main page!'


@app.route('/about')
def about_func():  # put application's code here
    return 'Welcome to about page!'


@app.route('/contact us')
def contact_func():  # put application's code here
    # print("contact us page is not available")
    return redirect('/about')


if __name__ == '__main__':
    app.run()
