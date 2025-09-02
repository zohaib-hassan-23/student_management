from db import execute_update, fetch_all

def insert_course(course_name, credit_hours):
    query = """
        INSERT INTO courses(course_name, credit_hours)
        VALUES (%s, %s)
    """
    return execute_update(query, (course_name, credit_hours))

def get_all_courses():
    query = """
        SELECT id, course_name, credit_hours, created_at
        FROM courses ORDER BY id
    """
    return fetch_all(query)

def delete_course(course_id):
    query = "DELETE FROM courses WHERE id = %s"
    return execute_update(query, (course_id,))
