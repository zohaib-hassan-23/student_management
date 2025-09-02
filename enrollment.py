from db import execute_update, fetch_all

def enroll_student(student_id, course_id):
    query = """
        INSERT INTO enrollments (student_id, course_id, enrolled_at)
        VALUES (%s, %s, CURRENT_TIMESTAMP)
    """
    return execute_update(query, (student_id, course_id))


def get_enrollments():
    query = """
        SELECT e.id,
               s.name AS student_name,
               c.course_name AS course_name,
               e.enrolled_at
        FROM enrollments e
        JOIN students s ON e.student_id = s.id
        JOIN courses c ON e.course_id = c.id
        ORDER BY e.id
    """
    return fetch_all(query)
