from flask import Flask, jsonify
import json
import random

app = Flask(__name__)

# Load quotes from JSON
with open("motivation.json", "r", encoding="utf-8") as file:
    quotes = json.load(file)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Motivation API!"})

@app.route("/random")
def random_quote():
    quote = random.choice(quotes)
    return jsonify(quote)

@app.route("/quote/<int:quote_id>")
def get_quote_by_id(quote_id):
    quote = next((q for q in quotes if q["id"] == quote_id), None)
    if quote:
        return jsonify(quote)
    return jsonify({"error": "Quote not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
