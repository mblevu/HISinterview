import sqlite3

# Function to delete the tables in the database
def delete_tables():
    try:
        conn = sqlite3.connect('patients.db')
        cursor = conn.cursor()

        # Drop the "patients" table
        cursor.execute('DROP TABLE IF EXISTS patients')

        # Drop any other tables you want to delete, if applicable

        conn.commit()
        conn.close()
        print("Tables deleted successfully.")
    except Exception as e:
        print("Error deleting tables:", str(e))

if __name__ == '__main__':
    delete_tables()
