from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

@app.route("/")
def home():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    other_file_path = os.path.join(current_directory, 'register.html')
    with open(other_file_path, 'r') as file:
        html_code = file.read()
    return html_code

@app.route("/register", methods=["POST"])
def register():
    # Retrieve data from form fields
    account_type = request.form.get('accountType')
    username = request.form.get('username')
    password = request.form.get('password')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')

    # Example processing: Print to console (or process and store in a database)
    print(f"Account Type: {account_type}, Username: {username}, Password: {password}, First Name: {first_name}, Last Name: {last_name}")

    # Return a simple confirmation message or redirect to another page
    return f"Registration Successful for {username}!"

if __name__ == "__main__":
    app.run(debug=True)


