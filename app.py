from flask import Flask, render_template, request, jsonify
import json, os

app = Flask(__name__)  # Create Flask web application

dataFile = "userData.json"

def load_data():   # Load data from JSON File
    if os.path.exists(dataFile):
        with open(dataFile, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_data(new):  # Save data to JSON file
    data = load_data()  # Load existing data
    data.append(new)  # Add new data to existing data
    
    with open(dataFile, "w") as file:
        json.dump(data, file, indent=2) # Save updated data

@app.route("/")  # Map root route to render webpage
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"]) 
def submit():
    try:
        new_data = request.json # Get JSON data from the request
        save_data(new_data) # Save data
        return jsonify({"message": "Data saved successfully!"})
    except Exception as e:
        return jsonify({"message": f"Failed to save data: {str(e)}"})

@app.route("/get_data", methods=["GET"]) # Fetch and return stored data
def get_data():
    return jsonify(load_data())

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False) # Prevents duplicate execution             