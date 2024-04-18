from flask import Flask
import os
#
current_directory = os.path.dirname(os.path.abspath(__file__))
other_file_path = os.path.join(current_directory, 'helloworld.html')

with open(other_file_path, 'r') as file:
    htmlcode = file.read()


app = Flask(__name__)
@app.route("/")
def hello_world():
    return htmlcode
