from db import get_connection
import psycopg2.extras

def insert_grade(student_id, course_id, grade):
    conn = get_connection()
    if not conn: return False
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO grades (student_id, course_id, grade) VALUES (%s, %s, %s)",
            (student_id, course_id, grade)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"insert_grade error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def get_all_grades():
    conn = get_connection()
    if not conn: return []
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            SELECT g.id, g.student_id, g.course_id, g.grade, g.graded_at,
                   s.name AS student_name, c.course_name
            FROM grades g
            JOIN students s ON s.id = g.student_id
            JOIN courses c ON c.id = g.course_id
            ORDER BY g.id
        """)
        return cur.fetchall()
    except Exception as e:
        print(f"get_all_grades error: {e}")
        return []
    finally:
        conn.close()

def find_grades_by_student(student_id):
    conn = get_connection()
    if not conn: return []
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            SELECT g.*, s.name AS student_name, c.course_name
            FROM grades g
            JOIN students s ON s.id = g.student_id
            JOIN courses c ON c.id = g.course_id
            WHERE g.student_id = %s
            ORDER BY g.id
        """, (student_id,))
        return cur.fetchall()
    except Exception as e:
        print(f"find_grades_by_student error: {e}")
        return []
    finally:
        conn.close()

def update_grade(grade_id, grade=None):
    conn = get_connection()
    if not conn: return False
    try:
        if grade is None:
            print(" No fields to update.")
            return False
        cur = conn.cursor()
        cur.execute("UPDATE grades SET grade=%s WHERE id=%s", (grade, grade_id))
        conn.commit()
        return True
    except Exception as e:
        print(f"update_grade error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def update_all_grades(new_grade=None):
    conn = get_connection()
    if not conn: return False
    try:
        if new_grade is None:
            print("No bulk fields to update.")
            return False
        cur = conn.cursor()
        cur.execute("UPDATE grades SET grade=%s", (new_grade,))
        conn.commit()
        return True
    except Exception as e:
        print(f"update_all_grades error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def delete_grade(grade_id):
    conn = get_connection()
    if not conn: return False
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM grades WHERE id=%s", (grade_id,))
        conn.commit()
        return True
    except Exception as e:
        print(f"delete_grade error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def delete_all_grades():
    conn = get_connection()
    if not conn: return False
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM grades")
        conn.commit()
        return True
    except Exception as e:
        print(f"delete_all_grades error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()
