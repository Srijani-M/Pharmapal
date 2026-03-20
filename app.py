import streamlit as st
import sqlite3
import hashlib
import os
import time
import threading
import re
from datetime import datetime
import google.generativeai as genai
import smtplib
from email.mime.text import MIMEText
import pytz

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="PharmaPal - Pharmaceutical Assistant",
    page_icon="💊",
    layout="wide"
)

# -----------------------------
# CUSTOM UI STYLE - Pastel Theme
# -----------------------------

st.markdown("""
<style>
    /* Main background with soft pastel gradient */
    .stApp {
        background: linear-gradient(135deg, #f8f0ff 0%, #e6f0fa 50%, #f0f5e8 100%);
    }

    /* Main content area background - soft white with transparency */
    .main > div {
        background: rgba(255, 255, 255, 0.85);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem;
        box-shadow: 0 8px 32px 0 rgba(156, 180, 209, 0.2);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.6);
    }

    /* Headers styling - soft colors */
    h1, h2, h3 {
        color: #6b7b8e;
        font-weight: 600;
        letter-spacing: 0.5px;
    }

    h1 {
    color: #000000;
    padding: 0.5rem 0;
    }

    /* Button styling - pastel gradient */
    .stButton > button {
        background: linear-gradient(135deg, #b8b5ff 0%, #a7c5eb 50%, #b5d3b5 100%);
        color: #4a5568;
        border: none;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        font-weight: 500;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px 0 rgba(184, 181, 255, 0.3);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px 0 rgba(184, 181, 255, 0.4);
        color: #2d3748;
    }

    /* Sidebar styling - soft pastel */
    .css-1d391kg, .css-163ttbj, [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #ffe9f4 0%, #e5e9ff 50%, #e0f0e0 100%);
        border-right: 1px solid rgba(255,255,255,0.3);
    }

    /* Sidebar text */
    .css-1d391kg .stMarkdown, .css-163ttbj .stMarkdown {
        color: #6b7b8e;
    }

    .css-1d391kg .stButton > button {
        background: rgba(255,255,255,0.7);
        backdrop-filter: blur(4px);
        border: 1px solid rgba(255,255,255,0.8);
        color: #6b7b8e;
    }

    /* Card styling - soft pastel */
    .card {
        background: linear-gradient(135deg, #ffffff 0%, #fcf5ff 100%);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(184, 181, 255, 0.1);
        border-left: 5px solid #b8b5ff;
        transition: all 0.3s ease;
    }

    .card:hover {
        transform: translateX(5px);
        box-shadow: 0 6px 12px rgba(184, 181, 255, 0.15);
    }

    /* Input fields styling - soft borders */
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #e8e1f0;
        background: rgba(255, 255, 255, 0.9);
        transition: all 0.3s ease;
    }

    .stTextInput > div > div > input:focus {
        border-color: #b8b5ff;
        box-shadow: 0 0 0 2px rgba(184, 181, 255, 0.2);
    }

    /* Select box styling */
    .stSelectbox > div > div {
        border-radius: 10px;
        border: 2px solid #e8e1f0;
        background: rgba(255, 255, 255, 0.9);
    }

    /* Success/Warning/Info messages - pastel colors */
    .stAlert {
        border-radius: 10px;
        border-left: 5px solid;
        animation: slideIn 0.3s ease;
    }

    /* Success message */
    .stAlert[data-baseweb="notification"] {
        background: linear-gradient(135deg, #e0f0e0 0%, #f0f5e8 100%);
        color: #4a6b4a;
    }

    /* Warning message */
    .stAlert[data-baseweb="notification"][kind="warning"] {
        background: linear-gradient(135deg, #fff4e5 0%, #ffe9d4 100%);
        color: #8b6b4a;
    }

    /* Error message */
    .stAlert[data-baseweb="notification"][kind="error"] {
        background: linear-gradient(135deg, #ffe5e5 0%, #ffd4d4 100%);
        color: #8b4a4a;
    }

    @keyframes slideIn {
        from {
            transform: translateX(-10px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }

    /* Metrics styling - pastel */
    [data-testid="stMetricValue"] {
        background: linear-gradient(135deg, #b8b5ff 0%, #a7c5eb 50%, #b5d3b5 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem !important;
        font-weight: 700 !important;
    }

    [data-testid="stMetricLabel"] {
        color: #8b9ab0;
        font-weight: 500;
    }

    /* Divider styling */
    hr {
        background: linear-gradient(90deg, transparent, #b8b5ff, #a7c5eb, #b5d3b5, transparent);
        height: 2px;
        border: none;
        margin: 2rem 0;
    }

    /* Radio button styling - pastel */
    .stRadio > div {
        background: rgba(255, 255, 255, 0.5);
        backdrop-filter: blur(4px);
        border-radius: 15px;
        padding: 1rem;
        border: 1px solid rgba(255, 255, 255, 0.8);
    }

    .stRadio > div > label {
        color: #6b7b8e !important;
        font-weight: 500;
        padding: 0.5rem;
        border-radius: 10px;
        transition: all 0.3s ease;
    }

    .stRadio > div > label:hover {
        background: rgba(184, 181, 255, 0.1);
    }

    /* File uploader styling - pastel */
    .stFileUploader > div {
        border: 2px dashed #b8b5ff;
        border-radius: 15px;
        padding: 2rem;
        background: rgba(184, 181, 255, 0.05);
    }

    /* Chat message styling - pastel */
    .stChatMessage {
        background: white;
        border-radius: 15px;
        padding: 1rem;
        margin: 0.5rem 0;
        box-shadow: 0 2px 5px rgba(184, 181, 255, 0.1);
        border-left: 5px solid #b8b5ff;
    }

    /* User chat message */
    .stChatMessage[data-testid="chatMessageUser"] {
        background: linear-gradient(135deg, #f0f5ff 0%, #faf0ff 100%);
        border-left-color: #a7c5eb;
    }

    /* Assistant chat message */
    .stChatMessage[data-testid="chatMessageAssistant"] {
        background: linear-gradient(135deg, #fff5f0 0%, #fff0fa 100%);
        border-left-color: #b5d3b5;
    }

    /* Scrollbar styling - soft pastel */
    ::-webkit-scrollbar {
        width: 10px;
        background: linear-gradient(180deg, #f8f0ff, #e6f0fa);
    }

    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #b8b5ff, #a7c5eb);
        border-radius: 5px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #a7a3ff, #96b4e0);
    }

    /* Info box styling */
    .stAlert[data-baseweb="info"] {
        background: linear-gradient(135deg, #e8f0fe 0%, #f0e8fe 100%);
        color: #5a6b8c;
        border-left-color: #b8b5ff;
    }

    /* Date input styling */
    .stDateInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #e8e1f0;
        background: rgba(255, 255, 255, 0.9);
    }

    /* Number input styling */
    .stNumberInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #e8e1f0;
        background: rgba(255, 255, 255, 0.9);
    }

    /* Time input styling */
    .stTimeInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #e8e1f0;
        background: rgba(255, 255, 255, 0.9);
    }

    /* Expander styling */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #f8f0ff 0%, #e6f0fa 100%);
        border-radius: 10px;
        color: #6b7b8e;
        font-weight: 500;
    }

    /* Table styling */
    .stTable {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        padding: 1rem;
    }

    /* DataFrame styling */
    .stDataFrame {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        padding: 1rem;
    }

    /* Markdown text */
    .stMarkdown {
        color: #5a6b8c;
    }

    /* Success text */
    .stSuccess {
        background: linear-gradient(135deg, #e0f0e0 0%, #d0e8d0 100%);
        color: #2d4a2d;
        border-radius: 10px;
        padding: 1rem;
    }

    /* Warning text */
    .stWarning {
        background: linear-gradient(135deg, #fff4e0 0%, #ffe8d0 100%);
        color: #8b6b4a;
        border-radius: 10px;
        padding: 1rem;
    }

    /* Error text */
    .stError {
        background: linear-gradient(135deg, #ffe0e0 0%, #ffd0d0 100%);
        color: #8b4a4a;
        border-radius: 10px;
        padding: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# TIMEZONE FIX FOR INDIA
# -----------------------------
ist = pytz.timezone('Asia/Kolkata')

def get_ist_now():
    """Get current Indian time"""
    return datetime.now(ist)

# -----------------------------
# GEMINI AI
# -----------------------------

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-pro")

# -----------------------------
# CREATE PRESCRIPTION FOLDER
# -----------------------------

UPLOAD_FOLDER = "prescription_storage"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# -----------------------------
# DATABASE
# -----------------------------

conn = sqlite3.connect("pharmapal.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
username TEXT PRIMARY KEY,
password TEXT,
email TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS prescriptions(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
medicine TEXT,
dosage TEXT,
rx_number TEXT,
remaining_refills INTEGER,
file_path TEXT,
upload_date TEXT,
expiry_date TEXT,
refill_reminder_days INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS reminders(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
medicine TEXT,
reminder_time TEXT,
last_sent TEXT,
is_active INTEGER DEFAULT 1
)
""")
try:
    cursor.execute("ALTER TABLE reminders ADD COLUMN email TEXT")
except:
    pass

conn.commit()

# -----------------------------
# EMAIL CONFIG
# -----------------------------

SENDER_EMAIL = ""
SENDER_PASSWORD = ""

def send_email(to_email, subject, body):
    """Send email using Gmail SMTP"""
    try:
        print(f"Sending email to {to_email}")

        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = SENDER_EMAIL
        msg["To"] = to_email

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        server.quit()

        print(f"Email sent to {to_email}")
        return True

    except Exception as e:
        print(f"Email failed: {str(e)}")
        return False

def send_refill_email(to_email, medicine, days_left, refills):
    """Send refill reminder email"""
    subject = f"PharmaPal Refill Reminder: {medicine}"

    if refills == 0:
        body = f"""
Your medicine {medicine} has NO refills remaining.

Please contact your pharmacy or doctor immediately.

- PharmaPal
"""
    else:
        body = f"""
Reminder from PharmaPal

Your medicine {medicine} will need a refill in {days_left} day(s).

Remaining refills: {refills}

Please restock before it runs out.
"""
    send_email(to_email, subject, body)

# -----------------------------
# REMINDER CHECKER (USING IST)
# -----------------------------

def check_reminders():
    """Check and send reminders using Indian time"""
    try:
        now_ist = get_ist_now()
        current_time = now_ist.strftime("%H:%M")
        today = now_ist.strftime("%Y-%m-%d")

        print(f"Checking at {current_time}")

        cursor.execute("SELECT id, email, medicine, reminder_time, last_sent FROM reminders WHERE is_active=1")
        rows = cursor.fetchall()

        for rid, email, med, r_time, last_sent in rows:
            reminder_minutes = r_time[:5]

            if reminder_minutes == current_time and last_sent != today:
                print(f"Sending reminder for {med}")

                subject = "PharmaPal Medicine Reminder"
                body = f"""
Hello,

This is your PharmaPal reminder.

Medicine: {med}
Time: {r_time}

Please take your medicine now.

Stay healthy,
PharmaPal AI Assistant
"""
                if send_email(email, subject, body):
                    cursor.execute("UPDATE reminders SET last_sent=? WHERE id=?", (today, rid))
                    conn.commit()
    except Exception as e:
        print(f"Error in check_reminders: {e}")

# -----------------------------
# SCHEDULER
# -----------------------------

def scheduler():
    """Run scheduler every 30 seconds"""
    print("Scheduler started")
    while True:
        try:
            check_reminders()
        except Exception as e:
            print(f"Scheduler error: {e}")
        time.sleep(30)

# Start scheduler thread
if 'scheduler_started' not in st.session_state:
    threading.Thread(target=scheduler, daemon=True).start()
    st.session_state.scheduler_started = True

# -----------------------------
# PASSWORD VALIDATION FUNCTION
# -----------------------------

def validate_password(password):
    """Validate password strength"""
    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters long")
    if not re.search(r"[A-Z]", password):
        errors.append("Password must contain at least one uppercase letter")
    if not re.search(r"[a-z]", password):
        errors.append("Password must contain at least one lowercase letter")
    if not re.search(r"\d", password):
        errors.append("Password must contain at least one number")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        errors.append("Password must contain at least one special character (!@#$%^&*)")

    return errors

# -----------------------------
# AUTH FUNCTIONS
# -----------------------------

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password, email):
    try:
        cursor.execute(
            "INSERT INTO users VALUES(?,?,?)",
            (username, hash_password(password), email)
        )
        conn.commit()
        return True
    except:
        return False

def login(username, password):
    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, hash_password(password))
    )
    return cursor.fetchone()

# -----------------------------
# AI MEDICAL RESTRICTION
# -----------------------------

def ask_medical_ai(question):
    # Medical keywords list
    medical_keywords = [
        "medicine", "medication", "drug", "pill", "tablet", "capsule",
        "dosage", "dose", "prescription", "rx", "refill", "pharmacy",
        "pharmacist", "doctor", "health", "medical", "symptom",
        "disease", "treatment", "therapy", "side effect", "interaction",
        "antibiotic", "vitamin", "supplement", "pain", "fever",
        "infection", "cold", "flu", "allergy", "headache", "nausea",
        "bp", "blood pressure", "sugar", "diabetes", "heart", "liver",
        "kidney", "stomach", "vomit", "diarrhea", "constipation",
        "inflammation", "swelling", "rash", "itch", "cough"
    ]

    question_lower = question.lower()
    is_medical = any(word in question_lower for word in medical_keywords)

    # Also check for question marks about health
    health_phrases = ["what is", "how to", "treatment for", "cure for", "symptoms of"]
    is_health_question = any(phrase in question_lower for phrase in health_phrases)

    if not is_medical and not is_health_question:
        return """
I can only answer medical or pharmaceutical questions.

Please ask about:
- Medicines and dosages
- Side effects and interactions
- Symptoms and treatments
- Prescriptions and refills
- General health concerns
"""

    prompt = f"""
You are PharmaPal AI, a professional pharmaceutical assistant.

IMPORTANT RULES:
1. ONLY answer medical, pharmaceutical, or health-related questions.
2. If question is NOT medical, politely refuse to answer.
3. Be accurate and helpful.
4. If unsure, advise consulting a doctor.

User Question: {question}

Answer:
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# -----------------------------
# SESSION STATE
# -----------------------------

if "page" not in st.session_state:
    st.session_state.page = "login"

if "user" not in st.session_state:
    st.session_state.user = None

if "email" not in st.session_state:
    st.session_state.email = None

# -----------------------------
# TITLE
# -----------------------------

st.title("PharmaPal AI Assistant")

# -----------------------------
# REGISTER PAGE (WITH PASSWORD CONSTRAINTS)
# -----------------------------

if st.session_state.page == "register":
    st.subheader("Create Account")

    with st.form("register"):
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password",
                                 help="Password must be at least 8 characters with uppercase, lowercase, number and special character")
        confirm = st.text_input("Confirm Password", type="password")

        # Show password requirements
        with st.expander("Password Requirements"):
            st.markdown("""
            - ✅ At least 8 characters long
            - ✅ At least one uppercase letter (A-Z)
            - ✅ At least one lowercase letter (a-z)
            - ✅ At least one number (0-9)
            - ✅ At least one special character (!@#$%^&*)
            """)

        if st.form_submit_button("Register"):
            if password != confirm:
                st.error("Passwords do not match")
            else:
                # Validate password
                password_errors = validate_password(password)
                if password_errors:
                    for error in password_errors:
                        st.error(error)
                elif register(username, password, email):
                    st.success("Account created successfully")
                    st.session_state.page = "login"
                    st.rerun()
                else:
                    st.error("Username already exists")

    if st.button("Back to Login"):
        st.session_state.page = "login"
        st.rerun()

# -----------------------------
# LOGIN PAGE
# -----------------------------

elif st.session_state.page == "login":
    st.subheader("Login")

    with st.form("login"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.form_submit_button("Login"):
            user = login(username, password)
            if user:
                st.session_state.user = username
                cursor.execute("SELECT email FROM users WHERE username=?", (username,))
                st.session_state.email = cursor.fetchone()[0]
                st.session_state.page = "dashboard"
                st.rerun()
            else:
                st.error("Invalid username or password")

    if st.button("Create Account"):
        st.session_state.page = "register"
        st.rerun()

# -----------------------------
# DASHBOARD
# -----------------------------

elif st.session_state.page == "dashboard":

    with st.sidebar:
        st.markdown(f"### Welcome, {st.session_state.user}")

        menu = st.radio(
            "Navigation",
            [
                "Dashboard",
                "Upload Prescription",
                "Prescription Vault",
                "Set Reminder",
                "AI Assistant"
            ]
        )

        if st.button("Logout"):
            st.session_state.user = None
            st.session_state.page = "login"
            st.rerun()

    # -----------------------------
    # DASHBOARD PAGE
    # -----------------------------

    if menu == "Dashboard":
        st.header("Dashboard")

        col1, col2 = st.columns(2)

        cursor.execute(
            "SELECT COUNT(*) FROM prescriptions WHERE username=?",
            (st.session_state.user,))
        pres_count = cursor.fetchone()[0]

        cursor.execute(
            "SELECT COUNT(*) FROM reminders WHERE username=?",
            (st.session_state.user,))
        rem_count = cursor.fetchone()[0]

        with col1:
            st.metric("Prescriptions", pres_count)
        with col2:
            st.metric("Reminders", rem_count)

        st.info("Follow your doctor's prescription for safe medication.")

        # REFILL ALERT SYSTEM (KEPT EXACTLY AS IT WAS)
        st.subheader("Refill Alerts")

        cursor.execute("""
        SELECT medicine, expiry_date, remaining_refills, refill_reminder_days
        FROM prescriptions
        WHERE username=?
        """, (st.session_state.user,))

        meds = cursor.fetchall()
        today = get_ist_now().date()
        alerts = []

        for med in meds:
            med_name = med[0]
            expiry_date = datetime.strptime(med[1], "%Y-%m-%d").date()
            refills = med[2]
            remind_days = med[3]
            days_left = (expiry_date - today).days

            if days_left <= remind_days:
                alerts.append((med_name, days_left, refills))

        if alerts:
            for a in alerts:
                if a[2] == 0:
                    st.error(f"{a[0]} has NO refills remaining! Contact pharmacy.")
                else:
                    st.warning(f"{a[0]} needs refill in {a[1]} day(s). Remaining refills: {a[2]}")

                send_refill_email(st.session_state.email, a[0], a[1], a[2])
        else:
            st.success("No refill alerts right now.")

    # -----------------------------
    # UPLOAD PRESCRIPTION
    # -----------------------------

    elif menu == "Upload Prescription":
        st.header("Upload Prescription")

        with st.form("upload_form"):
            uploaded_file = st.file_uploader(
                "Upload Prescription",
                type=["pdf", "png", "jpg", "jpeg"])

            medicine = st.text_input("Medicine Name *", placeholder="e.g., Amoxicillin")
            dosage = st.text_input("Dosage", placeholder="e.g., 500mg twice daily")
            rx_number = st.text_input("RX Number *", placeholder="e.g., RX123456")
            refills = st.number_input("Remaining Refills", min_value=0, max_value=12, value=3)
            expiry = st.date_input("Expiry Date", min_value=get_ist_now().date())
            reminder_days = st.number_input("Remind me before refill (days)", min_value=1, max_value=30, value=3)

            submitted = st.form_submit_button("Save Prescription")

            if submitted:
                if not uploaded_file:
                    st.error("Please upload a prescription file")
                elif not medicine:
                    st.error("Please enter medicine name")
                elif not rx_number:
                    st.error("Please enter RX number")
                else:
                    try:
                        # Create unique filename
                        timestamp = int(get_ist_now().timestamp())
                        filename = f"{st.session_state.user}_{timestamp}_{uploaded_file.name}"
                        file_path = os.path.join(UPLOAD_FOLDER, filename)

                        # Save file
                        with open(file_path, "wb") as f:
                            f.write(uploaded_file.getbuffer())

                        # Insert into database
                        cursor.execute("""
                        INSERT INTO prescriptions
                        (username, medicine, dosage, rx_number, remaining_refills, file_path,
                        upload_date, expiry_date, refill_reminder_days)
                        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """, (
                            st.session_state.user,
                            medicine,
                            dosage,
                            rx_number,
                            refills,
                            file_path,
                            get_ist_now().strftime("%Y-%m-%d %H:%M:%S"),
                            expiry.strftime("%Y-%m-%d"),
                            reminder_days
                        ))
                        conn.commit()

                        st.success("Prescription stored successfully!")

                    except Exception as e:
                        st.error(f"Error saving prescription: {str(e)}")

    # -----------------------------
    # PRESCRIPTION VAULT
    # -----------------------------

    elif menu == "Prescription Vault":
        st.header("PharmaPal Prescription Vault")

        search = st.text_input("Search medicine", placeholder="Type medicine name...")

        try:
            cursor.execute("""
            SELECT medicine, dosage, rx_number, remaining_refills, upload_date, file_path
            FROM prescriptions
            WHERE username=?
            ORDER BY upload_date DESC
            """, (st.session_state.user,))

            data = cursor.fetchall()

            if search:
                data = [d for d in data if search.lower() in d[0].lower()]

            if data:
                for med in data:
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.markdown(f"""
                        <div class="card">
                        <h4>{med[0]}</h4>
                        <p><b>Dosage:</b> {med[1] if med[1] else 'Not specified'}</p>
                        <p><b>RX Number:</b> {med[2]}</p>
                        <p><b>Refills Left:</b> {med[3]}</p>
                        <p><b>Uploaded:</b> {med[4]}</p>
                        </div>
                        """, unsafe_allow_html=True)
                    with col2:
                        if med[5] and os.path.exists(med[5]):
                            with open(med[5], "rb") as file:
                                st.download_button(
                                    "Download",
                                    file,
                                    file_name=os.path.basename(med[5]),
                                    key=med[5]
                                )
                        else:
                            st.error("File missing")
                    st.divider()
            else:
                st.info("No prescriptions found. Upload your first prescription!")

        except Exception as e:
            st.error(f"Error loading prescriptions: {str(e)}")

    # -----------------------------
    # SET REMINDER
    # -----------------------------

    elif menu == "Set Reminder":
        st.header("Set Medicine Reminder")

        email = st.text_input("Email", value=st.session_state.email)
        medicine = st.text_input("Medicine Name")

        # AM/PM Time Picker
        col1, col2, col3 = st.columns(3)
        with col1:
            hour = st.selectbox("Hour", list(range(1, 13)))
        with col2:
            minute = st.selectbox("Minute", [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
        with col3:
            ampm = st.selectbox("AM/PM", ["AM", "PM"])

        # Convert to 24-hour format
        if ampm == "AM":
            db_hour = 0 if hour == 12 else hour
        else:
            db_hour = 12 if hour == 12 else hour + 12

        if st.button("Save Reminder"):
            if email and medicine:
                reminder_time = f"{db_hour:02d}:{minute:02d}:00"

                cursor.execute("""
                INSERT INTO reminders
                (username, email, medicine, reminder_time, last_sent)
                VALUES(?, ?, ?, ?, ?)
                """, (
                    st.session_state.user,
                    email,
                    medicine,
                    reminder_time,
                    ""
                ))
                conn.commit()

                # Send confirmation email
                send_email(
                    email,
                    "Reminder Set",
                    f"""
Your reminder has been set!

Medicine: {medicine}
Time: {hour}:{minute:02d} {ampm}

You will receive a reminder at this time daily.

- PharmaPal
"""
                )

                st.success(f"Reminder set for {medicine} at {hour}:{minute:02d} {ampm}")

    # -----------------------------
    # AI ASSISTANT
    # -----------------------------

    elif menu == "AI Assistant":
        st.header("PharmaPal AI Assistant")

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

        if prompt := st.chat_input("Ask medical questions..."):
            st.session_state.chat_history.append({"role": "user", "content": prompt})

            with st.chat_message("user"):
                st.write(prompt)

            with st.chat_message("assistant"):
                with st.spinner("Analyzing medical information..."):
                    response = ask_medical_ai(prompt)
                    st.write(response)

            st.session_state.chat_history.append({"role": "assistant", "content": response})

# -----------------------------
# CLOSE CONNECTION
# -----------------------------

def close_connection():
    conn.close()

import atexit
atexit.register(close_connection)
