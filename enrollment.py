from db import get_connection
import psycopg2.extras

def insert_enrollment(student_id, course_id):
    conn = get_connection()
    if not conn: return False
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO enrollments (student_id, course_id) VALUES (%s, %s)",
            (student_id, course_id)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"insert_enrollment error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def get_all_enrollments():
    conn = get_connection()
    if not conn: return []
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            SELECT e.id, e.student_id, e.course_id, e.enrolled_at,
                   s.name AS student_name, c.course_name
            FROM enrollments e
            JOIN students s ON s.id = e.student_id
            JOIN courses c ON c.id = e.course_id
            ORDER BY e.id
        """)
        return cur.fetchall()
    except Exception as e:
        print(f"get_all_enrollments error: {e}")
        return []
    finally:
        conn.close()

def find_enrollments_by_student(student_id):
    conn = get_connection()
    if not conn: return []
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            SELECT e.*, s.name AS student_name, c.course_name
            FROM enrollments e
            JOIN students s ON s.id = e.student_id
            JOIN courses c ON c.id = e.course_id
            WHERE e.student_id = %s
            ORDER BY e.id
        """, (student_id,))
        return cur.fetchall()
    except Exception as e:
        print(f"find_enrollments_by_student error: {e}")
        return []
    finally:
        conn.close()

def update_enrollment(enrollment_id, student_id=None, course_id=None):
    conn = get_connection()
    if not conn: return False
    try:
        cur = conn.cursor()
        fields, values = [], []
        if student_id is not None: fields.append("student_id=%s"); values.append(student_id)
        if course_id is not None: fields.append("course_id=%s"); values.append(course_id)
        if not fields:
            print("No fields to update.")
            return False
        values.append(enrollment_id)
        cur.execute(f"UPDATE enrollments SET {', '.join(fields)} WHERE id=%s", tuple(values))
        conn.commit()
        return True
    except Exception as e:
        print(f"update_enrollment error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def update_all_enrollments(new_course_id=None):
    conn = get_connection()
    if not conn: return False
    try:
        if new_course_id is None:
            print("No bulk fields to update.")
            return False
        cur = conn.cursor()
        cur.execute("UPDATE enrollments SET course_id=%s", (new_course_id,))
        conn.commit()
        return True
    except Exception as e:
        print(f"update_all_enrollments error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def delete_enrollment(enrollment_id):
    conn = get_connection()
    if not conn: return False
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM enrollments WHERE id=%s", (enrollment_id,))
        conn.commit()
        return True
    except Exception as e:
        print(f"delete_enrollment error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def delete_all_enrollments():
    conn = get_connection()
    if not conn: return False
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM enrollments")
        conn.commit()
        return True
    except Exception as e:
        print(f"delete_all_enrollments error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()
