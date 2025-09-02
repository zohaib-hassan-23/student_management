from db import execute_update, fetch_all

def insert_student(name, email, dob, address):
    query = """
        INSERT INTO students(name, email, dob, address)
        VALUES (%s, %s, %s, %s)
    """
    return execute_update(query, (name, email, dob, address))

def get_all_students():
    query = """
        SELECT id, name, email, dob, address, created_at
        FROM students ORDER BY id
    """
    return fetch_all(query)

def delete_student(student_id):
    query = "DELETE FROM students WHERE id = %s"
    return execute_update(query, (student_id,))
