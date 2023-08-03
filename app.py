from flask import Flask, render_template, request, redirect
from send_mail import send_email
from utils import generate_reference_number
import sqlite3



app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('patients.db')
    conn.row_factory = sqlite3.Row
    return conn


# Route to display and handle the registration form
@app.route('/', methods=['GET', 'POST'])
def register_patient():
    if request.method == 'POST':
        # Get patient details from the form
        telephone = request.form['telephone']
        name = request.form['name']
        date_of_birth = request.form['date_of_birth']
        id_number = request.form['id_number']
        address = request.form['address']
        county = request.form['county']
        sub_county = request.form['sub_county']
        email = request.form['email']
        gender = request.form['gender']
        marital_status = request.form['marital_status']

        # Check if the email is already registered
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT email FROM patients WHERE email = ?', (email,))
        existing_email = cursor.fetchone()

        if existing_email:
            conn.close()
            return "Email is already registered. Please use a different email."

        # Insert patient details into the patients table
        cursor.execute('''
            INSERT INTO patients (telephone, name, date_of_birth, id_number, address, county, sub_county, email, gender, marital_status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (telephone, name, date_of_birth, id_number, address, county, sub_county, email, gender, marital_status))

        # Check if Next of Kin details were provided
        if 'next_of_kin_name' in request.form:
            next_of_kin_name = request.form['next_of_kin_name']
            next_of_kin_date_of_birth = request.form['next_of_kin_date_of_birth']
            next_of_kin_id_number = request.form['next_of_kin_id_number']
            next_of_kin_gender = request.form['next_of_kin_gender']
            next_of_kin_relationship = request.form['next_of_kin_relationship']
            next_of_kin_telephone = request.form['next_of_kin_telephone']

            # Insert Next of Kin details into the next_of_kin table
            cursor.execute('''
                INSERT INTO next_of_kin (patient_id, name, date_of_birth, id_number, gender, relationship, telephone)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (cursor.lastrowid, next_of_kin_name, next_of_kin_date_of_birth, next_of_kin_id_number, next_of_kin_gender, next_of_kin_relationship, next_of_kin_telephone))

        conn.commit()
        conn.close()

        # Generate a reference number and send the email to the patient
        reference_number = generate_reference_number()
        send_email(email, reference_number)

        return f"Patient registration successful. Your reference number is {reference_number}."

    return render_template('registration_form.html')

if __name__ == '__main__':
    app.run(debug=True)
