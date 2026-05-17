from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

projects = [
    {
        "title": "Expense Tracker",
        "description": "Track daily expenses and savings"
    },
    {
        "title": "AI Resume Builder using OpenAI API",
        "description": "Automatically creates ATS-friendly resumes"
    }
]

@app.route('/')
def home():
    return "Portfolio Backend Running"

@app.route('/projects')
def get_projects():
    return jsonify(projects)

if __name__ == '__main__':
    app.run(debug=True)