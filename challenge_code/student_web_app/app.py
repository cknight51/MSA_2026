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
    return render_template("major.html", majors=majors)

# Create a route for the major search page to respond to post requests after the form is submitted
@app.route("/majors", methods=["POST"])
def majors_post():
    # Get the list of majors
    url = "http://127.0.0.1:5000/api/majors/all"
    majors = get_student_data(url)

    # Get the form data (the chosen major from the select menu)
    major = request.form.get("major")

    # If major input is invalid display error message and reload page
    if major == "":
        flash("ERROR: You must select a major")
        return redirect(url_for("majors_get"))

    # Get students from that major
    url = f"http://127.0.0.1:5000/api/majors/{major}"
    students = get_student_data(url)

    # Send the list of students in the requested major to the majors template to be displayed in the browser
    return render_template("major.html", majors=majors, students=students, major=major)

# Create a route for the class search page to respond to get requests
@app.route("/class")
def class_get():
    # Make a list of classes
    classes = ["Freshman", "Sophomore", "Junior", "Senior"]

    # Send the list of classes to the class template to populate the menu
    return render_template("class.html", classes=classes)

# Create a route for the class search page to respond to post requests after the form is submitted
@app.route("/class", methods=["POST"])
def class_post():
    # Make a list of classes
    classes = ["Freshman", "Sophomore", "Junior", "Senior"]

    # Get the form data (the chosen major from the select menu)
    class_level = request.form.get("class")

    # If class input is invalid display error message and reload page
    if class_level == "":
        flash("ERROR: You must select a class")
        return redirect(url_for("class_get"))

    # Get students from that major
    url = f"http://127.0.0.1:5000/api/class/{class_level}"
    students = get_student_data(url)

    # Send the list of classes to the class template to populate the menu
    return render_template("class.html", classes=classes, students=students, class_level=class_level)


#run the flask app
app.run(port=5001)
