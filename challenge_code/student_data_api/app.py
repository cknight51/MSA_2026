import flask
from flask import request, jsonify
#import student_generator_v2 as sg

# Create a flask object
app = flask.Flask(__name__)

# Tell the server to reload each time the code changes
app.config["DEBUG"] = True

# Create a route for the home page of the application
@app.route('/', methods=['GET'])
def index():
    return "<h1>Student Data API</h1>"

# Create end points for the function we will create


# Run the application
app.run(debug=True)