import os
from importlib import import_module
from flask import Flask, redirect, url_for
from flask_cors import CORS #pip install flask_cors

app = Flask(__name__)
CORS(app) #enables requests from mtg api

# Dynamically import and register all routes from the routes package
# Must run 'python main.py' INSIDE the ShopTCG directory
for root, dirs, files in os.walk("routes"):
    for file in files:
        if file.endswith(".py") and file != "__init__.py":
            module_name = f"routes.{file[:-3]}"  # Convert file path to module path
            module = import_module(module_name)

            bp = getattr(module, 'bp', None)
            if bp:
                app.register_blueprint(bp)

@app.route('/')
def index():
    return redirect(url_for('register_bp.register'))

if __name__ == "__main__":
    app.run(debug=True)