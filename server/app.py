from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/capitalize", methods=["POST"])
def capitalize_text():
    data = request.get_json()
    text = data.get("text", "")
    capitalized = text.upper()
    return jsonify({"result": capitalized})
