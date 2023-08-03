# HIS Interview Application


This repository contains the code for the HIS Interview Application. It is a web-based application for patient registration and management.

In the media directory contains a simple demo of the working system


**Instructions**


To use the HIS Interview Application, follow the steps below:

**Clone this repository to your local machine:**


git clone https://github.com/kintokeanu/HISinterview.git

**Navigate into the project directory:**

cd HISinterview

**Create a new virtual environment and activate it:**

# On Windows (using Command Prompt)
python -m venv venv
venv\Scripts\activate

# On macOS and Linux
python3 -m venv venv
source venv/bin/activate
Install the required dependencies:


pip install -r requirements.txt


**Run the application:**

python3 app.py

Once the application is running, open your web browser and go to:


http://localhost:5000


You will now see the Patients Registration Form. Fill in the required details and submit the form to register a patient. If the email provided is not already registered, the patient details will be saved to the database, and an email with a patient reference number will be sent to the provided email address.

Please note that the application uses a SQLite database to store patient information, and it sends emails using a Gmail account. You can modify the app.py file to use your email credentials for sending emails.

If you encounter any issues or have questions, feel free to contact me or raise an issue in the repository. 