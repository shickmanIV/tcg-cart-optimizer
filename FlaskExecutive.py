from flask import Flask
from flask import request
from flask import render_template
import os

app = Flask(__name__)

@app.route("/")
def registerpage():
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)
