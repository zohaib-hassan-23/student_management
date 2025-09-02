from db import execute_update, fetch_all

def mark_attendance(student_id, course_id, date, status):
    query = """
        INSERT INTO attendance(student_id, course_id, date, status)
        VALUES (%s, %s, %s, %s)
    """
    return execute_update(query, (student_id, course_id, date, status))

def get_all_attendance():
    query = """
        SELECT a.id, s.name AS student, c.course_name AS course,
               a.date, a.status, a.marked_at
        FROM attendance a
        JOIN students s ON a.student_id = s.id
        JOIN courses c ON a.course_id = c.id
        ORDER BY a.date DESC
    """
    return fetch_all(query)
