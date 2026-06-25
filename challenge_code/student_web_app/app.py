from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests

#make a Flask app
app = Flask(__name__)
app.config["DEBUG"] = True

#set secret key
app.config["SECRET_KEY"] = "your secret key"

"""
Function to request student data from the api
Input: url
Output: JSON student data
"""
def get_student_data(url: str):
    return requests.get(url).json()

# Create a route for the website index/root/homepage, will display all student data
@app.route("/")
def index():
    # Make a request to the student data api for all students
    url = "http://127.0.0.1:5000/api/students/all"
    student_data = get_student_data(url)

    return render_template("index.html", student_data=student_data)

# Create a route for the major search page to respond to get requests
@app.route("/majors")
def majors_get():
    # Get the list of majors
    url = "http://127.0.0.1:5000/api/majors/all"
    majors = get_student_data(url)

    # Send the list of majors to the majors template to populate the menu
    return render_template("majors.html", majors=majors)

# Create a route for the major search page to respond to post requests after the form is submitted


#run the flask app
app.run(port=5001)
