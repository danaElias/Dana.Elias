from flask import Flask, redirect, url_for
from flask import render_template

app = Flask(__name__)


@app.route('/main')
@app.route('/')
def cv_page():  # put application's code here
    return render_template('cv.html')


@app.route('/contact')
def contact_page():  # put application's code here
    return render_template('cv2.html')


@app.route('/assignment8')
def assignment8():

    return render_template('assignment8.html', hobbies=['Dance', 'Ski', 'Sewing', 'Travel'], user=True,
                           name='Dana Elias')


@app.route('/preferences')
def preferences_page():
    return render_template('preferences.html')


@app.route('/volunteer')
def volunteer_page():
    return render_template('volunteer.html')


if __name__ == '__main__':
    app.run()
