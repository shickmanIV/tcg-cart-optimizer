import os
from importlib import import_module
from flask import Flask, request, redirect, render_template, url_for, Blueprint

app = Flask(__name__)

# Dynamically import and register all routes from the routes package
for root, dirs, files in os.walk("routes"):
    for file in files:
        if file.endswith(".py") and file != "__init__.py":
            module_name = f"routes.{file[:-3]}"  # Convert file path to module path
            module = import_module(module_name)
            app.register_blueprint(getattr(module, 'bp'))

@app.route('/')
def index():
    return redirect(url_for('testroutes_2.route2_method'))

if __name__ == "__main__":
    app.run(debug=True)