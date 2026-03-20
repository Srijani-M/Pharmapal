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

## 🛠 Tech Stack

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

Quick Start
1. Clone the Repository
git clone [https://github.com/Srijani-M/PharmaPal.git](https://github.com/Srijani-M/PharmaPal.git)
cd PharmaPal

2. Create a Virtual Environment
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Set Up Environment Variables
Create a .env file in the root directory and add your credentials:
GOOGLE_API_KEY=your_gemini_api_key_here
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_app_password_here

5. Run the Application
streamlit run app.py
Your app should now be running at: http://localhost:8501

How To Use
Register/Login: Create a secure account to start managing your health.

Upload Prescriptions: Enter medicine details and upload a file for digital record-keeping.

Set Reminders: Choose your medicine and preferred time to receive email alerts.

Ask the AI: Use the AI Assistant tab for quick answers to medical queries.

Contributing
Contributions are welcome! If you have suggestions for improvements or want to add new features, feel free to:

Fork the repository.

Create a new Branch (git checkout -b feature/NewFeature).

Commit your changes (git commit -m 'Add some NewFeature').

Push to the Branch (git push origin feature/NewFeature).

Open a Pull Request.

License
Distributed under the MIT License. This allows others to use and modify your code freely as long as they credit you.

Disclaimer
PharmaPal is an informational tool. The AI Assistant provides general information and is not a substitute for professional medical advice, diagnosis, or treatment.

Developed by Srijani M

