
from flask import Flask, jsonify, render_template, request
import json
import os

from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


# MongoDB connection
mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)

db = client["flask_app"]

collection = db["users"]
todo_collection = db["todoitems"]

# Task 1 - JSON API
@app.route("/api", methods=["GET"])
def get_data():

    with open("data.json", "r") as file:
        data = json.load(file)

    return jsonify(data)


# Task 2 - Frontend Form
@app.route("/", methods=["GET", "POST"])
def form():

    if request.method == "POST":

        try:
            # Get form data
            name = request.form.get("name")
            email = request.form.get("email")

            # Validate form data
            if not name or not email:
                raise ValueError("Name and email are required.")

            # Insert into MongoDB
            user_data = {
                "name": name,
                "email": email
            }

            collection.insert_one(user_data)

            return "Data inserted successfully into MongoDB!"

        except Exception as error:

            return render_template(
                "form.html",
                error=str(error)
            )

    return render_template("form.html")

@app.route("/todo", methods=["GET"])
def todo_page():
    return render_template("todo.html")

# Task 3 - Submit To-Do Item API
@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():

    try:
        # Get form data
        item_name = request.form.get("itemName")
        item_description = request.form.get("itemDescription")

        # Validate input
        if not item_name or not item_description:
            return jsonify({
                "error": "Item Name and Item Description are required."
            }), 400

        # Create To-Do document
        todo_item = {
            "itemName": item_name,
            "itemDescription": item_description
        }

        # Insert into MongoDB
        result = todo_collection.insert_one(todo_item)

        return jsonify({
            "message": "To-Do item saved successfully.",
            "id": str(result.inserted_id)
        }), 201

    except Exception:
        app.logger.exception("Failed to save To-Do item")
        return jsonify({
            "error": "Unable to save To-Do item."
        }), 500


if __name__ == "__main__":
    app.run(debug=True)