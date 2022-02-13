from flask import Flask
from markupsafe import escape

# test
app = Flask(__name__)

@app.route("/<name>")
def hello_world(name):
    return f"Hello {escape(name)}!"