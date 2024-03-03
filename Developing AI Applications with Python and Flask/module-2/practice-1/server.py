from flask import {insert module name here}
app = {insert module name here}(__name__)

@app.route("{insert root path here}")
def {insert method name}:
    return {insert message here}


from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"
a