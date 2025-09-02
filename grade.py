from db import execute_update, fetch_all

def assign_grade(student_id, course_id, grade):
    query = """
        INSERT INTO grades(student_id, course_id, grade)
        VALUES (%s, %s, %s)
    """
    return execute_update(query, (student_id, course_id, grade))

def get_all_grades():
    query = """
        SELECT g.id, s.name AS student, c.course_name AS course,
               g.grade, g.graded_at
        FROM grades g
        JOIN students s ON g.student_id = s.id
        JOIN courses c ON g.course_id = c.id
        ORDER BY g.graded_at DESC
    """
    return fetch_all(query)
