from flask import Flask, jsonify
import json
import random
import app_api

app = Flask(__name__)

# Load Shayari from JSON
with open("shayari.json", "r", encoding="utf-8") as f:
    data = json.load(f)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Love Shayari API"})

@app.route("/api/shayari", methods=["GET"])
def get_shayari():
    shayari = random.choice(data["shayaris"])
    return jsonify({"shayari": shayari})

if __name__ == "__main__":
    app.run(debug=True)
