from flask import Blueprint, render_template, request, redirect
from flask import flash
from interact_with_DB import interact_db


# about blueprint definition
assignment10 = Blueprint('assignment10', __name__, static_folder='static', template_folder='templates')


# Routes
@assignment10.route('/assignment10')
def users_func():
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=users)


@assignment10.route('/insert_user', methods = ['POST'])
def insert_user_func():
    # Get DATA from form
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']

    # Insert Data to DB
    query = "INSERT INTO users(first_name, last_name, email) values ('%s','%s','%s')" % (first_name, last_name, email)
    interact_db(query=query, query_type='commit')

    # Return to assignment10
    flash('Form submitted Successfully!')
    return redirect('/assignment10')


@assignment10.route('/delete_user', methods = ['POST'])
def delete_user_func():
    user_id = request.form['id']

    # Delete DATA from DB
    query = "DELETE FROM users WHERE id='%s';" % user_id
    interact_db(query=query, query_type='commit')

    # Return to assignment10
    flash('User deleted successfully!')
    return redirect('/assignment10')


@assignment10.route('/update', methods = ['POST'])
def update_user():
    # Get DATA from form
    user_id = request.form['id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']

    # Update DATA
    query = "select * FROM users WHERE id = '%s';" % user_id
    query_result = interact_db(query=query, query_type='fetch')
    if len(query_result) > 0:
        query = "UPDATE users SET first_name = '%s', last_name = '%s', email = '%s' WHERE id = '%s';" % (first_name, last_name, email,user_id )
        interact_db(query=query, query_type='commit')
        flash("The user has been update!")
        return redirect('/assignment10')
    else:
        flash(f'user {id} does not exist')
        return redirect('/assignment10')
