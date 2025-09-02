import psycopg2
import psycopg2.extras

def get_connection():
    """Create and return a PostgreSQL connection. Update credentials as needed."""
    try:
        return psycopg2.connect(
            host="localhost",
            dbname="student_management",
            user="postgres",
            password="Admin123",
            port=5432
        )
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None
