import MySQLdb

def get_connection():
    return MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="anita123",
        db="student_db"
    )
    
"""
if __name__ == "__main__":
    try:
        conn = get_connection()
        print("✅ Connected using get_connection()")
        conn.close()
    except MySQLdb.Error as e:
        print("❌ Connection failed")
        print(e)
"""