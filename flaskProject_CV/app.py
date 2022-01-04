from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from flask import session



app = Flask(__name__)
app.secret_key = '123'


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


@app.route('/logout')
def logout_func():
    session['user_name'] = ''
    return redirect('/assignment9')


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():

    users = {'user1': {'First Name': 'Dana', 'Last name': 'Elias', 'Email': 'danaElias@gmail.com'},
             'user2': {'First Name': 'Alon', 'Last name': 'Keidar', 'Email': 'alonKeidar@gmail.com'},
             'user3': {'First Name': 'Naama', 'Last name': 'Elia', 'Email': 'naamaElias@gmail.com'},
             'user4': {'First Name': 'Yael', 'Last name': 'Cohen', 'Email': 'yaelCohen@gmail.com'},
             'user5': {'First Name': 'Daniel', 'Last name': 'Avraham', 'Email': 'danielAvraham@gmail.com'}}

    if request.method == 'GET':
        if 'userKey' in request.args:
            if request.args.get('userKey') != '':
                print('true')
                user_key = request.args['userKey']
                print(user_key)
                for key in users:
                    print(key)
                    if users[key]['First Name'] == user_key or users[key]['Last name'] == user_key\
                            or users[key]['Email'] == user_key:
                        first_name = users[key]['First Name']
                        last_name = users[key]['Last name']
                        email = users[key]['Email']

                        return render_template('assignment9.html', firstName=first_name, last_name=last_name,
                                               email=email)
                return render_template('assignment9.html', inTheList='not')
            return render_template('assignment9.html', userList=users)
        return render_template('assignment9.html')

    if request.method == 'POST':
        user_name = request.form['user_name']
        password = request.form['password']
        # DB
        found = True
        if found:
            print('true')
            session['user_name'] = user_name
            return render_template('assignment9.html')
        else:
            return render_template('assignment9.html')


# Assignment 10
from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

if __name__ == '__main__':
    app.run()
