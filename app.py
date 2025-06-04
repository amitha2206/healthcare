from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json
import os
 
#deployment
app = Flask(__name__)
CORS(app)
 
DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "appointments.json")
 
# Ensure data folder exists
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
 
@app.route("/")
def serve_frontend():
    return render_template("index.html")
 
@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
 
    try:
        with open(DATA_FILE, "a") as f:
            json.dump(data, f)
            f.write("\n")
        return jsonify({"message": "Appointment saved successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)