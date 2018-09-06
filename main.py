#! /usr/bin/env python

from flask import Flask, render_template, send_from_directory, flash, request, redirect, url_for, g, Response
import sqlite3 as sql
import hashlib

app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/")
def index():
    return redirect("/home")

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/bill")
def bill():
    return render_template('bill.html')

@app.route("/payment")
def payment():
    return render_template('payment.html')
	
@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')


	
	
	
	
	
@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         firstname = request.form['firstname']
         lastname = request.form['lastname']
         email = request.form['email']
         password1 = request.form['password']
         password = hashlib.md5(password1.encode())
         password = (password.hexdigest())
         with sql.connect("test.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO user (firstname,lastname,email,password) VALUES (?,?,?,?)",(firstname,lastname,email,password) )
            
            con.commit()
            msg = "Record added succesfully"
      except:
         con.rollback()
         msg = "error in record"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/fetch')
def list():
   con = sql.connect("test.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select firstname,lastname,email from user")
   rows = cur.fetchall();
   return render_template("fetch.html",rows = rows)


"""
	
@app.route('/loginuser',methods = ['POST', 'GET'])
def loginuser():
   if request.method == 'POST':
      try:
         email = request.form['email']
         password1 = request.form['password']
         email = request.form['email']
         password = hashlib.md5(password1.encode())
         password = (password.hexdigest())
         with sql.connect("test.db") as con:
            cur = con.cursor()
            
            cur.execute("SELECT email,password from user WHERE email=(?) AND password=(?)",(email,password,))
            for row in cursor:
                if(row[0]==email):
                    msg = "logged in succesfully"
                else:
                    msg = "email or password wrong"
      except:
         con.rollback()
         msg = "error in record"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

"""

	
	

@app.route('/loginuser',methods = ['POST', 'GET'])
def loginuser():
    email = request.form['email']
    password1 = request.form['password']
    password = hashlib.md5(password1.encode())
    password = (password.hexdigest())
    conn = sql.connect('test.db')
    cursor = conn.execute("SELECT email,password from user WHERE email=(?) AND password=(?)",(email,password,))
    for row in cursor:
       if(row[0]==email):
          return render_template("result.html",msg="Logged in")
       else:
          return render_template("login.html")
    conn.close()
    return render_template("result.html",msg="Wrong email or password")

if __name__ == '__main__':
    app.debug = True
    app.run()
