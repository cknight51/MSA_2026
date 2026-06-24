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
    # Get the list of student dictinoaries
    student_dictionaries = sg.get_student_dicitonaries()
    valid_students = []

    # Iterate through the list of dicitonaries
    for student in student_dictionaries:
        # Determine if the search value matches the key value we are looking for
        if student[search_key].lower() == search_value.lower():
            # Add the student's dictionary to the valid list
            valid_students.append(student)

    # Return the valid list
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

# Create a route that returns students in a specific major
@app.route("/api/majors/<string:major>")
def api_major(major: str):
    # Call the search function to get students with this major
    major_students = search_dictionary_list("major", major)
    return jsonify(major_students)

# Create a route that returns students of a specific class
@app.route("/api/class/<string:student_class>")
def api_class(student_class: str):
    # Call the search function to get students of a specific class
    class_students = search_dictionary_list("class", student_class)
    return jsonify(class_students)

# Create a route that returns a student with a specific ID
@app.route("/api/students/id/<string:id>")
def api_id(id: str):
    # Call the search function to get a student with a specific ID
    id_student = search_dictionary_list("id", id)
    return jsonify(id_student)

# Run the application
app.run(debug=True)
