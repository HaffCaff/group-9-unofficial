#Harcoded scripts to create tables
CREATE_STUDENT_TABLE = ("CREATE TABLE IF NOT EXISTS students (id SERIAL PRIMARY KEY, fname TEXT, lname TEXT);")

ADD_STUDENT = ("INSERT INTO students (fname, lname) VALUES (%s, %s) RETURNING id;")

GET_ALL = ("SELECT * FROM students;")