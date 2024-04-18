# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return render_template('login.html')

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask
import os

app = Flask(__name__)

# No longer need to pre-read the HTML file
@app.route("/")
def hello_world():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    other_file_path = os.path.join(current_directory, 'homepage.html')
    with open(other_file_path, 'r') as file:
        htmlcode = file.read()
    return htmlcode

if __name__ == "__main__":
    app.run(debug=True)




# from flask import Flask
# import os
# #
# current_directory = os.path.dirname(os.path.abspath(__file__))
# other_file_path = os.path.join(current_directory, 'login.html')

# with open(other_file_path, 'r') as file:
#     htmlcode = file.read()


# app = Flask(__name__)
# @app.route("/")
# def hello_world():
#     return htmlcode
