# 🧠 ATS System – AI-Powered Resume Analyzer

This is a web-based **Applicant Tracking System (ATS)** built using **Streamlit** and **Google Gemini (Generative AI)** that analyzes resumes against job descriptions. It evaluates resume content, identifies missing keywords, recommends improvements, and estimates job match percentages — all powered by AI.

---

## 🚀 Features

- 📄 **Upload Resume** (PDF format)
- 📋 **Enter Job Description**
- 🤖 **AI Capabilities:**
  - Summarize resume with strengths and weaknesses
  - Recommend skills to improve
  - Highlight missing keywords from the job description
  - Calculate and explain percentage match with job role

---

## 🧰 Tech Stack

- 🐍 Python
- ⚡ Streamlit (for frontend)
- 🌐 Google Generative AI (Gemini 1.5 Flash model)
- 📄 pdf2image (to process PDF resumes)
- 🖼 PIL (to convert PDF to image)

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ats-system.git
cd ats-system
```

### 2. Create and Activate Virtual Environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API key

Create a .env file in the root directory and add your Google Gemini API key:
```bash
GOOGLE_API=your_google_gemini_api_key_here
```

### 5. Run the app

```bash
streamlit run ats.py
```

📂 File Structure
```bash
├── ats.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── Flow.txt            # Telling flow of the application
├── .env                # API Key (not to be committed)
└── README.md           # This file
```


📝 Example Use Case
  - A user uploads a resume in PDF format.
  
  - Enters a job description for a Data Scientist role.
  
  - Chooses one of the following analysis options:
  
     - Tell about Resume
  
    - How can I improve my skills?
  
    - Missing Important Keywords
  
     - Percentage Match

AI processes the resume + JD and returns intelligent, actionable insights.


# 🛡️ Disclaimer
This project is for educational/demo purposes. It does not guarantee actual job application results or reflect the scoring system of real-world ATS software.


# 🤝 Contribution
Contributions, issues, and feature requests are welcome!
Feel free to fork and improve.


