import MySQLdb

def get_connection():
    return MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="anita123",
        db="student_db"
    )
