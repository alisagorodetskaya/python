import sqlite3

class Database:
    def __init__(self, db_name="students.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                full_name TEXT,
                                group_number TEXT,
                                birth_date TEXT,
                                address TEXT,
                                real_avg REAL,
                                desired_avg REAL
                            )''')
        self.connection.commit()

    def insert_student(self, data):
        self.cursor.execute('''INSERT INTO students 
                               (full_name, group_number, birth_date, address, real_avg, desired_avg)
                               VALUES (?, ?, ?, ?, ?, ?)''',
                               (data["name"], data["group"], data["birth_date"],
                                data["address"], data["real_avg"], data["desired_avg"]))
        self.connection.commit()

    def update_student(self, student_id, new_avg):
        self.cursor.execute('''UPDATE students SET real_avg=? WHERE id=?''', (new_avg, student_id))
        self.connection.commit()

    def delete_student(self, student_id):
        self.cursor.execute('DELETE FROM students WHERE id=?', (student_id,))
        self.connection.commit()

    def fetch_all(self):
        self.cursor.execute('SELECT * FROM students')
        return self.cursor.fetchall()

    def __del__(self):
        self.connection.close()
