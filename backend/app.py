from flask import Flask, request, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'users'

mysql = MySQL(app)

@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('home.html')

@app.route('/hello', methods=['POST', 'GET'])
def hello():
    return "Hello World!"

@app.route('/users', methods=['POST', 'GET'])
def users():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM users')
    data = cur.fetchall()
    cur.close()
    return render_template('users.html', data=data)

@app.route('/new_users', methods=['POST', 'GET'])
def new_users():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, email, role) VALUES (%s, %s, %s)", (name, email, role))
        mysql.connection.commit()
        cur.close()
        return render_template('confirmation.html', name=name)
    else:
        return render_template('input_user.html')
    
@app.route('/users/<id>')
def user_details(id):
    user_id = int(id)
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user_data = cur.fetchone()
    cur.close()

    if user_data:
        return render_template('users_details.html', user=user_data)
    else:
        return "User not found", 404


if __name__ == '__main__':
    app.run(debug=True)