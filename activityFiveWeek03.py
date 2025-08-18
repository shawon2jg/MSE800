# Activity 5: update the sample code "Sample_code_SQLite3"
# You can add a new table named "Students" with three columns: Stu_ID, Stu_name, and Stu_address. Insert two sample records into Students, then display all rows from both the Users and Students tables.

import mysql.connector
from mysql.connector import errors

#region Connect Database
connection = mysql.connector.connect(user='root', password='root', host='localhost', database='edusysdb')
#endregion

def create_tables():
    try:
        connection._open_connection()
        cursor = connection.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS student (
                          student_id varchar(4) NOT NULL,
                          first_name varchar(50) NOT NULL,
                          last_name varchar(50) NOT NULL,
                          email varchar(100) NOT NULL,
                          dob date DEFAULT NULL,
                          address varchar(100) DEFAULT NULL,
                          contact_no varchar(15) DEFAULT NULL,
                          enrollment_date date NOT NULL,
                          major varchar(50) DEFAULT NULL,
                          PRIMARY KEY (student_id),
                          UNIQUE KEY email (email)
                        )
                       """)
        print("Table created successfully.")
        connection.commit()
    except errors as e:
        print("Print error messages", e)
    finally:
        connection.close()

def insert_rows():
    try:
        connection._open_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO student (student_id, first_name, last_name, email, dob, address, contact_no, enrollment_date, major) VALUES ('0001','S M','Shawon','shawon2jg@gmail.com','2000-05-15','Avondale','223788414','2025-07-28','Software Engineering')")
        cursor.execute("INSERT INTO student (student_id, first_name, last_name, email, dob, address, contact_no, enrollment_date, major) VALUES ('0002','Kamal Bin','Shafiq','shafiqkamalbin@gmail.com','2001-05-18','Avondale','221949987','2025-07-28','Business Informatics')")
        print("Data inserted successfully.")
        connection.commit()
    except errors as e:
        print("Print error messages", e)
    finally:
        connection.close()

def search_rows():
    try:
        connection._open_connection()
        cursor = connection.cursor()
        print("Students:")
        cursor.execute("SELECT t.* FROM student t")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print("Fetched all rows successfully.")
    except errors as e:
        print("Print error messages", e)
    finally:
        connection.close()

if __name__ == '__main__':
    create_tables()
    insert_rows()
    search_rows()