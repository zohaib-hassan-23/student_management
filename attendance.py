from db import get_connection
import psycopg2.extras

VALID_STATUSES = {"Present", "Absent", "Late"}

def insert_attendance(student_id, course_id, date, status):
    if status not in VALID_STATUSES:
        print("Invalid status. Use Present/Absent/Late.")
        return False
    conn = get_connection()
    if not conn: return False
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO attendance (student_id, course_id, date, status) VALUES (%s, %s, %s, %s)",
            (student_id, course_id, date, status)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"insert_attendance error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()
        
def get_all_attendance():
    conn = get_connection()
    if not conn: return []
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            SELECT a.id, a.student_id, a.course_id, a.date, a.status, a.marked_at,
                   s.name AS student_name, c.course_name
            FROM attendance a
            JOIN students s ON s.id = a.student_id
            JOIN courses c ON c.id = a.course_id
            ORDER BY a.id
        """)
        return cur.fetchall()
    except Exception as e:
        print(f"get_all_attendance error: {e}")
        return []
    finally:
        conn.close()

def find_attendance_by_student(student_id):
    conn = get_connection()
    if not conn: return []
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            SELECT a.*, s.name AS student_name, c.course_name
            FROM attendance a
            JOIN students s ON s.id = a.student_id
            JOIN courses c ON c.id = a.course_id
            WHERE a.student_id = %s
            ORDER BY a.date DESC, a.id DESC
        """, (student_id,))
        return cur.fetchall()
    except Exception as e:
        print(f"find_attendance_by_student error: {e}")
        return []
    finally:
        conn.close()

def update_attendance(attendance_id, status=None, date=None):
    if status is not None and status not in VALID_STATUSES:
        print("Invalid status. Use Present/Absent/Late.")
        return False
    conn = get_connection()
    if not conn: return False
    try:
        cur = conn.cursor()
        fields, values = [], []
        if status is not None: fields.append("status=%s"); values.append(status)
        if date is not None: fields.append("date=%s"); values.append(date)
        if not fields:
            print("No fields to update.")
            return False
        values.append(attendance_id)
        cur.execute(f"UPDATE attendance SET {', '.join(fields)} WHERE id=%s", tuple(values))
        conn.commit()
        return True
    except Exception as e:
        print(f"update_attendance error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def update_all_attendance(new_status=None):
    if new_status is not None and new_status not in VALID_STATUSES:
        print("Invalid status. Use Present/Absent/Late.")
        return False
    conn = get_connection()
    if not conn: return False
    try:
        if new_status is None:
            print("No bulk fields to update.")
            return False
        cur = conn.cursor()
        cur.execute("UPDATE attendance SET status=%s", (new_status,))
        conn.commit()
        return True
    except Exception as e:
        print(f"update_all_attendance error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def delete_attendance(attendance_id):
    conn = get_connection()
    if not conn: return False
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM attendance WHERE id=%s", (attendance_id,))
        conn.commit()
        return True
    except Exception as e:
        print(f"delete_attendance error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def delete_all_attendance():
    conn = get_connection()
    if not conn: return False
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM attendance")
        conn.commit()
        return True
    except Exception as e:
        print(f"delete_all_attendance error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()
