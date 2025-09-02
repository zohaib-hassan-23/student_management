from db import get_connection
import psycopg2.extras

def insert_student(name, email, address=None, dob=None):
    conn = get_connection()
    if not conn: return False
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO students (name, email, address, dob) VALUES (%s, %s, %s, %s)",
            (name, email, address, dob)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"insert_student error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def get_all_students():
    conn = get_connection()
    if not conn: return []
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM students ORDER BY id")
        rows = cur.fetchall()
        return rows
    except Exception as e:
        print(f"get_all_students error: {e}")
        return []
    finally:
        conn.close()

def find_student_by_email(email):
    conn = get_connection()
    if not conn: return None
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM students WHERE email = %s", (email,))
        return cur.fetchone()
    except Exception as e:
        print(f"find_student_by_email error: {e}")
        return None
    finally:
        conn.close()

def update_student(student_id, name=None, email=None, address=None, dob=None):
    conn = get_connection()
    if not conn: return False
    try:
        cur = conn.cursor()
        fields, values = [], []
        if name is not None: fields.append("name=%s"); values.append(name)
        if email is not None: fields.append("email=%s"); values.append(email)
        if address is not None: fields.append("address=%s"); values.append(address)
        if dob is not None: fields.append("dob=%s"); values.append(dob)
        if not fields:
            print("No fields to update.")
            return False
        values.append(student_id)
        cur.execute(f"UPDATE students SET {', '.join(fields)} WHERE id=%s", tuple(values))
        conn.commit()
        return True
    except Exception as e:
        print(f"update_student error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def update_all_students(new_address=None, new_dob=None):
    conn = get_connection()
    if not conn: return False
    try:
        cur = conn.cursor()
        fields, values = [], []
        if new_address is not None: fields.append("address=%s"); values.append(new_address)
        if new_dob is not None: fields.append("dob=%s"); values.append(new_dob)
        if not fields:
            print("No bulk fields to update.")
            return False
        cur.execute(f"UPDATE students SET {', '.join(fields)}", tuple(values))
        conn.commit()
        return True
    except Exception as e:
        print(f"update_all_students error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def delete_student(student_id):
    conn = get_connection()
    if not conn: return False
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM students WHERE id=%s", (student_id,))
        conn.commit()
        return True
    except Exception as e:
        print(f"delete_student error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def delete_all_students():
    conn = get_connection()
    if not conn: return False
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM students")
        conn.commit()
        return True
    except Exception as e:
        print(f"delete_all_students error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()
