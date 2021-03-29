import os
import datetime
import sqlite3
import mysql.connector

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import create_engine

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response



# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
# db = sqlite3.connect("recipes.db")


mydb = mysql.connector.connect(
  host="us-cdbr-east-03.cleardb.com",
  database="heroku_c5f47ec692770a7",
  user="b238a65c3214e0",
  passwd="dd6a246a"
  )


mycursor = mydb.cursor(buffered=True)

if mydb.is_connected():
        db_Info = mydb.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = mydb.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)


# Make sure API key is set
# if not os.environ.get("API_KEY"):
#   raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show current recipes"""
    if request.method == "GET":
        return render_template("index.html")
    else:
        return apology("TODO", code=400)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)
        username=request.form.get("username")
        # Query database for username
        query = "SELECT * FROM users WHERE username = %s OR username = %s"
        mycursor.execute(query, (username, username))
        rows = mycursor.fetchone()
        #print(rows)  
        print(rows[0])  # user id
        print(rows[1])  # login
        print(rows[2])  # password hash  
        password = request.form.get("password")  
        novo_hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8) 
        #print(len(rows))   
        print(novo_hash)
        print(check_password_hash(rows[2], request.form.get("password")))       
            
        # Ensure username exists and password is correct
        if len(rows) == 0 or not check_password_hash(rows[2], password):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]
        
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/recipe", methods=["GET", "POST"])
@login_required
def recipe():
    """Show current recipes"""
    if request.method == "GET":
        return render_template("recipe.html")
    else:
        return apology("TODO", code=400)


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # in this method we prevent the user from leaving any field empty
    # Also we require that the "password" field and the "password confirmation" fields are the same
    # The database is verified for the same username being taken

    if request.method == "GET":
        return render_template("register.html")
    else:
        name = request.form.get("username")
        if not name:
            return apology("must provide name", code=400)
        password = request.form.get("password")
        if not password:
            return apology("must provide password", code=400)
        password2 = request.form.get("confirmation")
        if not password2:
            return apology("must provide password confirmation", code=400)
        if password != password2:
            return apology("passwords must match", code=400)

        # Check if the username already exists on the database
        check = """SELECT username FROM users WHERE username=%s OR username=%s"""
        mycursor.execute(check, (name, name))
        if mycursor.fetchone() is not None:
            return apology("username already taken", code=400)
               
        else:
            hash_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
            sql = "INSERT INTO users (username, hash) VALUES (%s, %s)"
            val = (name, hash_password)
            mycursor.execute(sql, val)
            mydb.commit()

        return redirect("/")
            

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
