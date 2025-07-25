from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "awWelcome to the Flask app!"