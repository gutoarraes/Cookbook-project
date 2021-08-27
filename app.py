import os
import datetime
import sqlite3
import mysql.connector
import json
<<<<<<< HEAD
import sys
import requests
=======
>>>>>>> 9eff7feb08c991945b6bae7e89203dd73ba29b9d

from urllib.request import urlopen  
from xml.etree import ElementTree
from lxml import etree
from cs50 import SQL
<<<<<<< HEAD
from flask import Flask, flash, jsonify, redirect, render_template, request, session, make_response
=======
from flask import Flask, flash, jsonify, redirect, render_template, request, session
>>>>>>> 9eff7feb08c991945b6bae7e89203dd73ba29b9d
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

<<<<<<< HEAD
=======
# Configure CS50 Library to use SQLite database
# db = sqlite3.connect("recipes.db")


>>>>>>> 9eff7feb08c991945b6bae7e89203dd73ba29b9d
mydb = mysql.connector.connect(
  host="us-cdbr-east-03.cleardb.com",
  database="heroku_c5f47ec692770a7",
  user="b238a65c3214e0",
  passwd="dd6a246a"
  )


mycursor = mydb.cursor(buffered=True)

<<<<<<< HEAD
=======
if mydb.is_connected():
        db_Info = mydb.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = mydb.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

>>>>>>> 9eff7feb08c991945b6bae7e89203dd73ba29b9d

@app.route("/")
@login_required
def index():
    """Show current recipes"""
<<<<<<< HEAD
    query = """SELECT * FROM recipes WHERE user = %s OR user = %s""" # Adicionar verificacao de usuario (provavelmente criar uma foreign key)
    usuario = session["user_id"]
    print(usuario)
    mycursor.execute(query, (usuario, usuario))
    recipes1 = mycursor.fetchall()
    

    print(recipes1)
    return render_template("index.html", recipes=recipes1) 

=======
    # username = session["user_id"]
    # query_database = "SELECT * FROM users WHERE id = %s or id = %s"
    # values = (username, username)
    # recipes = mycursor.execute(query_database, values)
    # mydb.commit()

    # sql = "INSERT INTO recipes (id, recipe_name, ingredients, preparation) VALUES (%s, %s, %s, %s)"
    # val = (id, recipe_name, ingredients, preparation)
    # mycursor.execute(sql, val)
    # mydb.commit()

    return render_template("index.html") #, recipes=recipes
    

>>>>>>> 9eff7feb08c991945b6bae7e89203dd73ba29b9d

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
<<<<<<< HEAD
        rows = mycursor.fetchone() 
        password = request.form.get("password")  
        novo_hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8) 
=======
        rows = mycursor.fetchone()
        #print(rows)  
        # print(rows[0])  # user id
        # print(rows[1])  # login
        # print(rows[2])  # password hash  
        password = request.form.get("password")  
        novo_hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8) 
        # print(len(rows))   
        # print(novo_hash)
        # print(check_password_hash(rows[2], request.form.get("password")))       
>>>>>>> 9eff7feb08c991945b6bae7e89203dd73ba29b9d
            
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
<<<<<<< HEAD
        titulo = request.form.get("title1")
        preparo = request.form.get("preparation")
        ingredientes = request.form.get("ingredients1")
        user = session["user_id"]

        statement = """INSERT INTO recipes (user, recipe_name, preparation, ingredients) VALUES (%s, %s, %s, %s)"""
        mycursor.execute(statement, (user, titulo, preparo, ingredientes))
        mydb.commit()

        return redirect("/")
=======
        # add to table "recipe" on database the new recipe (title, JSON of ingredients, preparation)
        recipe_title = request.form.get("title")
        ingredients = request.form.get("username")
        preparation = request.form.get("preparation")
        
        url = "http://127.0.0.1:5000/recipe"
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        table = html.find("tbody")
        print(table)
        table2 = html.find("tr")
        print(table2)
        table3 = html.find("Ingredients")
        print(table3)
        table4 = html.find("<table>")
        print(table4)

        # hash_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        # sql = "INSERT INTO recipes (recipe_title, ingredients, preparation) VALUES (%s, %s, %s)"
        # val = (recipe_title, ingredients, preparation)
        # mycursor.execute(sql, val)
        # mydb.commit()

        # html_file = open("templates/recipe.html")
        # html_content = html_file.read()
        # parsed_html = etree.HTML(html_content)
        # print(html_content)
        # html_tables = parsed_html.findall("table/tbody")
        # html_content3 = parsed_html.findall("table")
        # html_content4 = parsed_html.find('tbody')
        # print(html_content3)
        # print(html_content4)
        
        # first_table = html_tables[0]
        # table_as_list = list(first_table)
        # table_headers = [col.text for col in table_as_list[0]]
        # table_list_dict = [dict(zip(table_headers, [col.text for col in row])) for row in table_as_list[1:]]
        # print(table_list_dict)
        
        
        return redirect("index.html")
>>>>>>> 9eff7feb08c991945b6bae7e89203dd73ba29b9d


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
<<<<<<< HEAD
        # There was an error happening when submitting the query below, so I used the brazilian problem solving technique called "gambiarra" to fix it.
=======
>>>>>>> 9eff7feb08c991945b6bae7e89203dd73ba29b9d
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
<<<<<<< HEAD
        print(e)
=======
>>>>>>> 9eff7feb08c991945b6bae7e89203dd73ba29b9d
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
<<<<<<< HEAD


=======
>>>>>>> 9eff7feb08c991945b6bae7e89203dd73ba29b9d
