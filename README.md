# Attend-X — Smart Attendance Management System

Attend-X is an intelligent attendance management system designed to simplify classroom attendance using face recognition and voice recognition. Built with Python, Streamlit, and Supabase, it provides an interactive platform for teachers to manage subjects, enroll students, record attendance, and review attendance records.

## Features

- **Face Recognition:** Analyze classroom photos to identify enrolled students.
- **Voice Recognition:** Process classroom audio to identify students using registered voice profiles.
- **Student Management:** Register students and maintain their biometric profiles.
- **Subject Management:** Create and manage subjects and class enrollments.
- **Attendance Tracking:** Record and review attendance results.
- **QR Code Sharing:** Generate QR codes to help students access class enrollment links.
- **Interactive Dashboard:** Provide separate workflows for teachers and students.
- **Cloud Database:** Use Supabase to store and retrieve application data.

## Technology Stack

| Component | Technology |
|---|---|
| Frontend and dashboard | Streamlit |
| Programming language | Python |
| Database and backend services | Supabase |
| Face recognition | `face_recognition`, dlib |
| Voice processing | Librosa, Resemblyzer |
| Data handling | Pandas, NumPy |
| QR code generation | Segno |
| Image processing | Pillow |

## Project Structure

```text
Attend-X/
├── .gitignore
├── README.md
├── REPOSITORY_GUIDE.md
├── app.py
├── requirements.txt
├── src/
│   ├── components/
│   │   ├── dialog_add_photo.py
│   │   ├── dialog_attendance_result.py
│   │   ├── dialog_auto_enroll.py
│   │   ├── dialog_create_subject.py
│   │   ├── dialog_enroll.py
│   │   ├── dialog_share_subject.py
│   │   ├── dialog_voice_attendance.py
│   │   ├── footer.py
│   │   ├── header.py
│   │   └── subject_card.py
│   ├── database/
│   │   ├── config.py
│   │   └── db.py
│   ├── pipeline/
│   │   ├── face_pipeline.py
│   │   └── voice_pipeline.py
│   ├── screens/
│   │   ├── home_screen.py
│   │   ├── student_screen.py
│   │   └── teacher_screen.py
│   └── ui/
│       └── base_layout.py
└── streamlit/                 # Local ignored configuration, not committed
    └── secrets.toml           # Do not commit or publish secret values
```

The detailed file-by-file reference, function index, UI source map, and safe redesign guide is in [REPOSITORY_GUIDE.md](./REPOSITORY_GUIDE.md). Python package marker files (`__init__.py`) are omitted from this shortened tree.

## Getting Started

### Prerequisites

- Python 3.12 or newer
- A Supabase project
- Git

### 1. Clone the repository

```bash
git clone https://github.com/hamza5212/Attend-X.git
cd Attend-X
```

### 2. Create a virtual environment

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Some packages, particularly dlib and audio-processing libraries, may require additional system dependencies depending on your operating system.

### 4. Configure Supabase

Create a Supabase project and configure the required connection settings.

For local development, create the configuration file expected by the application, such as `streamlit/secrets.toml`, and add the keys required by `src/database/config.py`.

Example format:

```toml
SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your-publishable-key"
```

Use the exact key names expected by your configuration code. Never commit credentials, service-role keys, or other secrets to GitHub.

Create the database tables and relationships required by the application before running it.

### 5. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL printed in your terminal to access Attend-X.

## How It Works

1. Teachers access the dashboard and create subjects.
2. Students are registered and associated with the appropriate subjects.
3. Face images and voice profiles are used by the respective recognition pipelines.
4. Teachers initiate photo-based or audio-based attendance analysis.
5. Recognition results are presented for review and attendance recording.

Recognition accuracy depends on image quality, audio clarity, enrollment quality, and the matching thresholds implemented in the application.

## Database Overview

The application uses Supabase tables for its core data:

- `teachers` — teacher account information.
- `students` — student information and registered profiles.
- `subjects` — subjects created by teachers.
- `subject_students` — student enrollment relationships.
- `attendance_logs` — attendance records.

The actual database schema must match the queries and relationships used in the application.

## Security and Privacy

Attend-X processes biometric information, including face and voice profiles. Such data should be handled responsibly.

- Keep Supabase credentials out of version control.
- Apply appropriate database access policies and authentication.
- Restrict access to biometric data.
- Obtain appropriate consent before collecting or processing biometric information.
- Use test data during development and demonstrations whenever possible.

## Current Status

Attend-X is a student-developed project intended to demonstrate automated attendance workflows using face recognition, voice recognition, and cloud database integration. It should be tested thoroughly before being used for real-world attendance decisions.

## Future Improvements

- Improved recognition thresholds and confidence scoring.
- Attendance analytics and downloadable reports.
- Better handling of duplicate detections and repeated attendance submissions.
- More robust authentication and role-based access control.
- Session-based attendance tracking.
- Enhanced deployment configuration and automated testing.

## Author

**Hamza Selanawala**

GitHub: [@hamza5212](https://github.com/hamza5212)

---

*Attend-X — Making classroom attendance smarter and simpler.*
