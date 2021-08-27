# Cookbook

###### Video demo:
Please watch my YouTube demonstration of the [Cookbook](https://youtu.be/ROCB1KSDkc0)

###### Description: 
Final project of the Harvard's Introduction to computer science's course.
In this project I created a web portal for people to store their recipes. 
Once in the website, the user can register a new account and upload their own recipes (title, ingredient list and preparation).
After it is submitted, it will appear with all other recipes index page as an accordion component, from the bootstrap library.
I am still updating a couple of functionalities to this project such as an embedded button to delete individual recipes. 
In the future, I would like to also allow people to search for other users' recipes.
Finally, I will host this web app on Heroku for anyone who wishes to access it.

###### TAGs
1. Python
2. HTML
3. CSS
4. Flask Framework
5. Bootstrap
6. MySQL (database)
7. Heroku (hosting)

###### pages
Apology.html - In case something goes wrong, this apology page will display a message and the error code
Index.html - First page after a successful login (aka Homepage)
Layout.html - In the flask framework, the Layout page allows other pages to extend from it and bring all the elements in it to themselves without having to be copied every time
Login.html - First page on the website where the user will be prompted to log in
Recipe.html - This is the page where the user will add a new recipe. I worked for a long time on it while I tried to have the user input the ingredients and their respective quantities in a dynamic table.
    I managed to create the table using JavaScript funcions, but I coulnd't make work the capture of the information with Ajax or Python itself, so I switched to a textarea
Register.html - Page where the user would create a new username and password for themselves
app.py - Where all the functionatility is stored (user validation, connection with database and updating/retrieving of such database)
Helpers.py - file created by the CS50 staff to help with previous project, but I took advantage of its functionality on this one as well 
Database - There are 2 tables on my database, *users* (id, username, hash) and *recipes* (user = users.id, recipe_name, recipe_title, preparation)

###### Next steps
- [ ] Add button to delete or edit a recipe
- [ ] Add functionality to change password and delete account
- [ ] Allow users to search for recipes accross all users who choose to display their recipes publicly

###### Thanks
Please check out the [CS50 Introduction to computer science](https://cs50.harvard.edu/x/2021/) course on Edx. 
