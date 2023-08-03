# database.py
import sqlite3

# Create a connection to the database
conn = sqlite3.connect('patients.db')
cursor = conn.cursor()

# Create the table to store patient details
cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telephone TEXT NOT NULL,
        name TEXT NOT NULL,
        date_of_birth TEXT NOT NULL,
        id_number TEXT NOT NULL,
        address TEXT NOT NULL,
        county TEXT NOT NULL,
        sub_county TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,  -- Add UNIQUE constraint to ensure no duplicate emails
        gender TEXT NOT NULL,
        marital_status TEXT NOT NULL
    )
''')

# Create the table to store Next of Kin details
cursor.execute('''
    CREATE TABLE IF NOT EXISTS next_of_kin (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        date_of_birth TEXT NOT NULL,
        id_number TEXT NOT NULL,
        gender TEXT NOT NULL,
        relationship TEXT NOT NULL,
        telephone TEXT NOT NULL,
        FOREIGN KEY (patient_id) REFERENCES patients (id)
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
