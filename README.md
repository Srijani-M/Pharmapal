# PharmaPal - AI-Powered Healthcare Assistant

**PharmaPal** is a comprehensive prescription management system with AI-powered medical assistance and automated medication reminders. It is designed to help users stay on top of their healthcare routines with ease and security.

---

## Features

### User Authentication
* **Secure Access:** Robust login and registration system.
* **Password Validation:** Enforced security rules (uppercase, lowercase, numbers, and special characters).
* **Session Management:** Keeps your data private and secure.

### Prescription Management
* **Multi-format Uploads:** Support for PDF, PNG, and JPG files.
* **Data Tracking:** Store medicine names, dosages, and RX numbers.
* **Tracking:** Monitor remaining refills and set expiration dates.
* **Management:** View and download your stored prescriptions anytime.

### Medicine Reminders
* **Daily Alerts:** Set recurring reminders for your medications.
* **Custom Scheduling:** Select specific times using a user-friendly AM/PM format.
* **Email Notifications:** Receive alerts directly in your inbox at reminder times.

### AI Medical Assistant
* **Powered by Google Gemini AI:** Advanced AI integration for pharmaceutical questions.
* **Contextual Info:** Get details on symptoms, medicines, and treatments.
* **Safety First:** Includes a built-in disclaimer for medical advice.

### Dashboard
* **At-a-glance Overview:** See your stored prescriptions and active reminders count.
* **Quick Access:** Navigate easily to core system features.

---

## Tech Stack

* **Language:** Python 3.8+
* **Frontend/UI:** Streamlit
* **AI Model:** Google Gemini AI
* **Database:** SQLite
* **Communication:** SMTP (Gmail Integration)
* **Cloud Hosting:** Google Cloud Platform (GCP)

---

## 📁 Project Structure

```text
Pharmapal/
├── app.py                 # Main application script
├── requirements.txt       # List of dependencies
├── .env                   # Environment variables (Internal)
├── .gitignore             # Files to exclude from Git
├── README.md              # Project documentation
├── prescription_storage/  # Folder for uploaded documents
└── logs/                  # System activity logs
