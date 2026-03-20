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

## Project Structure

```text
Pharmapal/
├── app.py                 # Main application script
├── requirements.txt       # List of dependencies
├── .env                   # Environment variables (Internal)
├── .gitignore             # Files to exclude from Git
├── README.md              # Project documentation
├── prescription_storage/  # Folder for uploaded documents
└── logs/                  # System activity logs
```
---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone [https://github.com/Srijani-M/PharmaPal.git](https://github.com/Srijani-M/PharmaPal.git)
cd PharmaPal
```

### 2. Create a Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
**Mac/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

**Bash:**
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

**Config:**
Create a `.env` file in the root directory and add your credentials:
```env
GOOGLE_API_KEY=your_gemini_api_key_here
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_app_password_here
```

### 5. Run the Application

**Bash:**
```bash
streamlit run app.py
```
Note: The application will be available at http://localhost:8501

---

## How To Use

* **Register/Login:** Create a secure account to protect your medical data.
* **Upload Prescriptions:** Digitally store medicine details and RX files.
* **Set Reminders:** Choose a medicine and time to receive automated email alerts.
* **AI Assistant:** Consult the Gemini-powered chat for pharmaceutical info.

---

## Contributing

**Join Us:**
Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## License & Disclaimer

* **License:** Distributed under the **MIT License**.
* **Disclaimer:** PharmaPal provides informational content only and is **not** a substitute for professional medical advice, diagnosis, or treatment.

---

*Developed by **[Srijani M](https://github.com/Srijani-M)***
