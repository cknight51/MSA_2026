import flask
from flask import request, jsonify
import student_generator_v2 as sg

# Create a flask object
app = flask.Flask(__name__)

# Tell the server to reload each time the code changes
app.config["DEBUG"] = True

'''
Function to query the list of student dictionaries based on a search key and value
Input: search_key - key in the dictionary we want to check the value of
       search_value - the value of the key we need to match
Output: list of student dictionaries that match the search criteria
'''
def search_dictionary_list(search_key, search_value):
    student_dictionaries = sg.get_student_dicitonaries()
    valid_students = []
    for student in student_dictionaries:
        if student[search_key] == search_value:
            valid_students.append(student)
    return valid_students

# Create a route for the home page of the application
@app.route("/")
def index():
    return "<h1>Student Data API</h1>"

# Create end points for the function we will create
# Create a route to return all student data 
@app.route("/api/students/all")
def api_all():
    # Get student dictionaries
    student_dictionaries = sg.get_student_dicitonaries()
    return jsonify(student_dictionaries)

# Create a route that returns students by a specific key-value pair
@app.route("/api/students/major")
def api_major():
    # Get student dictionaries
    student_major_dictionaries = search_dictionary_list("id", "184262")
    return jsonify(student_major_dictionaries)

# Run the application
app.run(debug=True)
