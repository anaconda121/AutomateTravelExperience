from flask import Flask, render_template, request, json, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flaskext.mysql import MySQL
from flask_socketio import SocketIO, send
import MySQLdb.cursors
import sys
import os
from templates.travelSecurity.ticket import processTicket
from templates.travelSecurity.hotels import trip_planning
from templates.travelSecurity.city_tours import city_tours_planning
from templates.travelSecurity.sports import sports
from templates.travelSecurity.sightsee import sightsee
from templates.travelSecurity.trains import trains
from templates.travelSecurity.cars import cars
from templates.travelSecurity.buses import buses
from templates.travelSecurity.bike import bike
from subprocess import call
import pymysql

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'plmokn12'
app.config['MYSQL_DATABASE_DB'] = 'flaskapp'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['SECRET_KEY'] = 'tanish' 
app.config['MYSQL_DATABASE_PORT'] = 3308
mysql.init_app(app)
socketio = SocketIO(app)

#creating server route for app
@app.route("/")
def main():
    return render_template('signup.html')

#processing vals once form is submitted
#def showSignUp():

    #return render_template('signup.html')

@app.route('/signUp', methods= ['GET', 'POST'])
def signUp():
    try:
        #reading in vals from form
        name = request.form['username']
        email = request.form['mail']
        password = request.form['pwd']


        #creating connection
        conn = mysql.connect()
        cursor = conn.cursor()

        if name and email and password:
            #encrypting password
            #hashedPassword = generate_password_hash(password)

            #inserting data
            cursor.callproc('sp_createUser',(email, password))
            data = cursor.fetchall()

            if len(data) == 0:
                conn.commit()
                return json.dumps({'message':'User created successfully !'})
            else:
                return json.dumps({'error':str(data[0])})

        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error':str(e)})

    cursor.close()
    conn.close()

@app.route('/login', methods = ['GET', 'POST'])
def login():

    #request.form takes in name attribute of input field
    username = request.form['Username']
    print(username, file = sys.stderr)

    password = request.form['Password']
    print(password, file = sys.stderr)

    print(request.method, file = sys.stderr)
    conn = mysql.connect()
    cursor = conn.cursor()

    #checking to make sure form is filled out
    if request.method == 'POST' and username and password:

        #checking if account exists in db
        cursor.execute('SELECT * FROM users WHERE user_email = %s AND user_password = %s', (username, password))
        account = cursor.fetchone()

        print("account = ", account, file = sys.stderr)
        #redirecting based on outcome
        if account:
            return render_template('home.html')

        else:
            return render_template('signup.html')

    else:
        return render_template('signup.html')
        conn.close()
        cursor.close()

#file routes
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/stats')
def case():
    return render_template('stats.html')

@app.route('/forum')
def forum():
    return render_template('forum.html')

@app.route('/asteroids')
def game():
    return render_template('asteroids.html')

@app.route('/logout')
def logout():
    return render_template('signup.html')

@app.route('/snake')
def snake():
    return render_template('snake.html')

@app.route('/caseStudy')
def caseStudy():
    return render_template('predictor.html')

@app.route('/algo')
def algo():
    return render_template('algo.html')

@app.route('/ticket_vals', methods= ['GET', 'POST'])
def ticket_vals():
    processTicket()
    #better_airport()
    #call(["python", "templates/travelSecurity/airplane.py"])

    if processTicket() == False:
        return render_template('better.html')
    else:
        return render_template('good.html')

@app.route('/planner', methods= ['GET', 'POST'])
def planner():
    return render_template('planner.html')

@app.route('/planned_trip', methods= ['GET', 'POST'])
def planned_trip():
    trip_planning()
    city_tours_planning()
    sports()
    trains()
    cars()
    buses()
    bike()

    if trip_planning() == 1:
        print('1')
        return render_template('planner.html')
    elif trip_planning() == 2:
        print('2')
        return render_template('planner.html')

#socket io routes
def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


if __name__ == '__main__':
   #app.run() #debug = true makes it so change is auto reflected
    socketio.run(app, debug = True, host = '0.0.0.0', port = 5000)

#python airplane.py miami boston 6/15/2020 6/21/2020
