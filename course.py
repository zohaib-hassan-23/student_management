from db import get_connection
import psycopg2.extras

def insert_course(course_name, credit_hours):
    conn = get_connection()
    if not conn: return False
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO courses (course_name, credit_hours) VALUES (%s, %s)",
            (course_name, credit_hours)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"insert_course error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def get_all_courses():
    conn = get_connection()
    if not conn: return []
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM courses ORDER BY id")
        return cur.fetchall()
    except Exception as e:
        print(f"get_all_courses error: {e}")
        return []
    finally:
        conn.close()

def find_course_by_name(name_query):
    conn = get_connection()
    if not conn: return []
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM courses WHERE course_name ILIKE %s ORDER BY id", (f"%{name_query}%",))
        return cur.fetchall()
    except Exception as e:
        print(f"find_course_by_name error: {e}")
        return []
    finally:
        conn.close()

def update_course(course_id, course_name=None, credit_hours=None):
    conn = get_connection()
    if not conn: return False
    try:
        cur = conn.cursor()
        fields, values = [], []
        if course_name is not None: fields.append("course_name=%s"); values.append(course_name)
        if credit_hours is not None: fields.append("credit_hours=%s"); values.append(credit_hours)
        if not fields:
            print("No fields to update.")
            return False
        values.append(course_id)
        cur.execute(f"UPDATE courses SET {', '.join(fields)} WHERE id=%s", tuple(values))
        conn.commit()
        return True
    except Exception as e:
        print(f"update_course error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def update_all_courses(new_credit_hours=None):
    conn = get_connection()
    if not conn: return False
    try:
        if new_credit_hours is None:
            print("No bulk fields to update.")
            return False
        cur = conn.cursor()
        cur.execute("UPDATE courses SET credit_hours=%s", (new_credit_hours,))
        conn.commit()
        return True
    except Exception as e:
        print(f"update_all_courses error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def delete_course(course_id):
    conn = get_connection()
    if not conn: return False
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM courses WHERE id=%s", (course_id,))
        conn.commit()
        return True
    except Exception as e:
        print(f"delete_course error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def delete_all_courses():
    conn = get_connection()
    if not conn: return False
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM courses")
        conn.commit()
        return True
    except Exception as e:
        print(f"delete_all_courses error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()
