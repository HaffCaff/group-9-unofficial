import os
import psycopg2
import queries
from dotenv import load_dotenv
from flask import Flask, render_template, request

#Load .env variables
load_dotenv()

#set database connection url using .env
db_url = os.getenv('POSTGRES_URL')
connection = psycopg2.connect(db_url)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/testing')
def testing():
    return render_template('testing.html')


@app.route('/about_us')
def about_us():
    return render_template('about_us.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/endpoints')
def endpoints():
    return render_template('endpoints.html')


@app.post("/api/students")
def create_students():
    data = request.get_json()
    fname = data["fname"] 
    lname = data["lname"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(queries.CREATE_STUDENT_TABLE)
            cursor.execute(queries.ADD_STUDENT, (fname,lname,))
            student_id = cursor.fetchone()[0]
    return {"id": student_id, "message": f"Student {fname} {lname} added to database"}, 201


@app.get("/api/students/all")
def get_students():
    students = {}
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(queries.GET_ALL)
            students = cursor.fetchall()
    return students


if __name__ == "__main__":
    app.run(debug=True)