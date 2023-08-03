import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

from dotenv import load_dotenv

# Send an email to the patient
def send_email(email, reference_number):
    subject = "Patient Registration Successful"
    message = f"Thank you for registering. Your reference number is {reference_number}."
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = 'brianislevu@gmail.com' 
    msg['To'] = email

    # Set up the email server (e.g., Gmail)
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(os.getenv('EMAIL_ADDRESS'), os.getenv('EMAIL_PASSWORD'))
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
        server.quit()
    except Exception as e:
        print('Error sending email:', str(e))
