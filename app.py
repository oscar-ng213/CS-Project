from flask import Flask, render_template, request, jsonify
import json, os

app = Flask(__name__)  # Will automatically use "templates" and "static"

dataFile = "userData.json"

def load_data():
    if os.path.exists(dataFile):
        with open(dataFile, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_data(new):
    data = load_data()
    data.append(new)
    
    with open(dataFile, "w") as file:
        json.dump(data, file, indent=2)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        new_data = request.json
        save_data(new_data)
        return jsonify({"message": "Data saved successfully!"})
    except Exception as e:
        return jsonify({"message": f"Failed to save data: {str(e)}"})

@app.route("/get_data", methods=["GET"])
def get_data():
    return jsonify(load_data())

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)                 