from flask import Flask
app = Flask(__name__)

@app.route('/')
def greet():
    return '<span style="color: blue;">Hello world!</span><br>' * 10
