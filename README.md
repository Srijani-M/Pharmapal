# PharmaPal - AI-Powered Healthcare Assistant

A prescription management system with AI-powered medical assistance and medication reminders.

---

## Features

### User Authentication
- Secure login and registration
- Password validation (uppercase, lowercase, numbers, special characters)
- Session management

### Prescription Management
- Upload prescriptions (PDF, PNG, JPG)
- Store medicine name, dosage, and RX number
- Track remaining refills
- Set expiry dates
- View and download stored prescriptions

### Medicine Reminders
- Set daily reminders for medications
- Custom time selection (AM/PM format)
- Email notifications at reminder times

### AI Medical Assistant
- Powered by Google Gemini AI
- Answers medical and pharmaceutical questions
- Provides information about medicines, symptoms, and treatments
- Includes a disclaimer for medical advice

### Email Notifications
- Medicine reminder emails
- Basic alerting system for medication tracking
- Gmail SMTP integration

### Dashboard
- Overview of prescriptions
- Active reminders count
- Quick access to core features

---

## Project Structure

Pharmapal/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
├── prescription_storage/
└── logs/

---

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Srijani-M/Pharmapal.git
cd Pharmapal

### 2. Create Virtual Environment
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Set Up Environment Variables
Create a .env file (do not commit this file):
GOOGLE_API_KEY=your_gemini_api_key_here
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_app_password_here

### 5. Run the Application

streamlit run app.py


Application runs at: http://localhost:8501

Tech Stack
Python 3.8+

Streamlit

Google Gemini AI

SQLite

SMTP

Google Cloud Platform (GCP)

How to Use
1. Register/Login
Create an account with a secure password.

2. Upload Prescriptions
Enter medicine details

Upload prescription file

Store and manage records

3. Set Medicine Reminders
Choose medicine

Select reminder time

Receive email notifications

4. Use AI Assistant
Ask medical-related questions

Get informational responses

Not a substitute for professional advice

5. Dashboard
View stored prescriptions

Monitor reminders

Important Disclaimer
Not a substitute for professional medical advice

Always consult healthcare professionals

AI responses are informational only

Planned Features
SMS reminders

Automated refill alerts

Medication interaction checker

Mobile app version

License
MIT License

Made with ❤️ for better healthcare management
