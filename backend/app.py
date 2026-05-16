from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="08680868",
    database="portfolio"
)

@app.route('/')
def home():
    return "Portfolio Backend Running"

@app.route('/projects')
def get_projects():

    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM projects")

    projects = cursor.fetchall()

    return jsonify(projects)

if __name__ == '__main__':
    app.run(debug=True)