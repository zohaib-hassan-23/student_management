from db import get_connection

def init_db():
    commands = [
        "DROP TABLE IF EXISTS attendance CASCADE",
        "DROP TABLE IF EXISTS grades CASCADE",
        "DROP TABLE IF EXISTS enrollments CASCADE",
        "DROP TABLE IF EXISTS courses CASCADE",
        "DROP TABLE IF EXISTS students CASCADE",

        '''
        CREATE TABLE students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            address VARCHAR(255),
            dob DATE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''',
        '''
        CREATE TABLE courses (
            id SERIAL PRIMARY KEY,
            course_name VARCHAR(100) NOT NULL,
            credit_hours INT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''',
        '''
        CREATE TABLE enrollments (
            id SERIAL PRIMARY KEY,
            student_id INT REFERENCES students(id) ON DELETE CASCADE,
            course_id INT REFERENCES courses(id) ON DELETE CASCADE,
            enrolled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''',
        '''
        CREATE TABLE grades (
            id SERIAL PRIMARY KEY,
            student_id INT REFERENCES students(id) ON DELETE CASCADE,
            course_id INT REFERENCES courses(id) ON DELETE CASCADE,
            grade VARCHAR(5),
            graded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''',
        '''
        CREATE TABLE attendance (
            id SERIAL PRIMARY KEY,
            student_id INT REFERENCES students(id) ON DELETE CASCADE,
            course_id INT REFERENCES courses(id) ON DELETE CASCADE,
            date DATE NOT NULL,
            status VARCHAR(20) CHECK (status IN ('Present', 'Absent', 'Late')),
            marked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        '''
    ]

    conn = get_connection()
    if not conn:
        print("Could not get DB connection.")
        return False

    try:
        cur = conn.cursor()
        for sql in commands:
            cur.execute(sql)
        conn.commit()
        cur.close()
        print("Database initialized (dropped & recreated tables).")
        return True
    except Exception as e:
        print(f"Error initializing DB: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

if __name__ == "__main__":
    init_db()
