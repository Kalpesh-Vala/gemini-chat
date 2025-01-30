from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Import CORS
import os
import google.generativeai as genai

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

print(GOOGLE_API_KEY)

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    response = model.generate_content(data["message"])
    return jsonify(response=response.text)

if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0")

