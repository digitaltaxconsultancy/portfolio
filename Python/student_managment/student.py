from db_config import get_connection


def add_student(name, email, course):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO students (name, email, course)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (name, email, course))
    conn.commit()

    print("✅ Student added successfully")

    cursor.close()
    conn.close()


def view_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print("\n--- Student List ---")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Course: {row[3]}")

    cursor.close()
    conn.close()


def update_student(student_id, name, email, course):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE students
    SET name=%s, email=%s, course=%s
    WHERE id=%s
    """
    cursor.execute(query, (name, email, course, student_id))
    conn.commit()

    print("✅ Student updated successfully")

    cursor.close()
    conn.close()


def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = "DELETE FROM students WHERE id=%s"
    cursor.execute(query, (student_id,))
    conn.commit()

    print("✅ Student deleted successfully")

    cursor.close()
    conn.close()
