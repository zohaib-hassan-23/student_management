import psycopg2
import psycopg2.extras

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="student_management",
        user="postgres",
        password="Admin123",
        port=5432
    )

def execute_update(query, params=None):
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(query, params)
        conn.commit()
        cur.close()
        return True
    except Exception as e:
        print(f"Error executing update: {e}")
        return False
    finally:
        if conn:
            conn.close()

def fetch_all(query, params=None):
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute(query, params)
        rows = cur.fetchall()
        cur.close()
        return rows
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []
    finally:
        if conn:
            conn.close()
