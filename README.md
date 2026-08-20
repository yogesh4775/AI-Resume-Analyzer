# 🤖 AI Resume Analyzer

An AI-powered web application that analyzes PDF resumes and provides useful insights such as resume score, technical skills, job-role matches, word count, improvement suggestions, and job-description matching.

---

## 🚀 Features

### 📄 Resume Analysis

- Upload a PDF resume
- Extract text from the uploaded PDF
- Calculate resume score out of 100
- Calculate resume word count
- Detect technical skills
- Match resume with suitable job roles
- Generate resume improvement suggestions

### 🎯 Job Description Matching

Users can paste a job description and compare it with their resume.

The application provides:

- Job match percentage
- Matched skills
- Missing skills
- Job-specific recommendations

### 🖥️ User Interface

- Clean and responsive interface
- Simple PDF upload system
- Resume analysis dashboard
- Skill tags
- Job-role progress bars
- Job-description matching section
- Mobile-friendly design

---

## 🛠️ Tech Stack

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Python
- FastAPI
- Uvicorn
- PyPDF

### Other Technologies

- REST API
- CORS
- Multipart File Upload
- PDF Text Extraction

---

## 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── backend/
│   ├── main.py
│   ├── analyzer.py
│   └── resume_parser.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── uploads/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔄 How the Application Works

```text
                 User
                  │
                  ▼
          Upload PDF Resume
                  │
                  ▼
           PDF Validation
                  │
                  ▼
          Extract Resume Text
                  │
                  ▼
           Resume Analyzer
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
      Skills    Score    Word Count
        │
        ▼
     Job Role Matching
        │
        ▼
 Improvement Suggestions
        │
        ▼
      Display Results
```

---

## 📊 Resume Analysis

The application analyzes the uploaded resume and provides several useful metrics.

### Resume Score

The resume receives a score out of 100 based on different resume factors.

The analyzer considers information such as:

- Resume length
- Technical skills
- Important resume sections
- Contact information
- Projects
- Experience
- Achievement-related content

### Technical Skills

The application detects technical skills mentioned in the resume.

Example:

```text
Python
C++
Java
SQL
NumPy
Pandas
Machine Learning
Git
GitHub
FastAPI
```

### Word Count

The application calculates the number of words extracted from the uploaded resume.

### Job Role Matching

The detected technical skills are compared with predefined job roles.

Example:

```text
Python Developer
Data Analyst
Machine Learning Engineer
Backend Developer
Frontend Developer
Full Stack Developer
DevOps Engineer
```

The application displays the matching percentage for suitable roles.

---

## 🎯 Job Description Matching

The application also provides a dedicated job-description matching feature.

Users can paste a job description into the application and compare it with their uploaded resume.

### Workflow

```text
Resume
   +
Job Description
   │
   ▼
Skill Comparison
   │
   ├── Matched Skills
   │
   ├── Missing Skills
   │
   └── Match Percentage
```

This helps users identify the skills they already have and the skills they may need to improve.

---

## 💡 Resume Improvement Suggestions

The analyzer provides suggestions based on the resume content.

Examples include:

- Add more technical skills
- Add relevant projects
- Add internship or work experience
- Add measurable achievements
- Add LinkedIn profile
- Add GitHub profile
- Improve resume content
- Maintain an appropriate resume length

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/yogesh4775/AI-Resume-Analyzer.git
```

Move into the project directory:

```bash
cd AI-Resume-Analyzer
```

---

## 2. Create a Virtual Environment

On Windows:

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

The project contains two parts:

- FastAPI backend
- HTML/CSS/JavaScript frontend

---

## 🚀 Start the Backend

From the project root directory:

```bash
uvicorn backend.main:app --reload
```

The FastAPI server will run at:

```text
http://127.0.0.1:8000
```

---

## 📚 FastAPI API Documentation

FastAPI provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

Available endpoints include:

```text
GET  /
POST /analyze
POST /match-job
```

---

## 🌐 Start the Frontend

You can run the frontend using VS Code Live Server.

Alternatively, from the project root:

```bash
python -m http.server 5500 --directory frontend
```

Then open:

```text
http://127.0.0.1:5500
```

---

# 🔌 API Endpoints

## GET /

Checks whether the FastAPI backend is running.

Example response:

```json
{
    "message": "AI Resume Analyzer API is running"
}
```

---

## POST /analyze

Uploads and analyzes a PDF resume.

### Input

```text
PDF Resume
```

### Output

The API returns information including:

- Filename
- Resume score
- Word count
- Technical skills
- Job-role matches
- Resume suggestions

---

## POST /match-job

Matches a resume against a specific job description.

### Input

```text
PDF Resume
Job Description
```

### Output

The API returns job matching information.

---

# 🔐 File Handling

Only PDF files are accepted for resume analysis.

Uploaded files are stored temporarily in:

```text
uploads/
```

Unique filenames are generated for uploaded resumes to avoid filename conflicts.

The `uploads/` directory is excluded from Git tracking using `.gitignore`.

---

# 🖥️ Application Screens

The application contains the following main sections:

### Resume Upload

Users can select their PDF resume and start the analysis.

### Resume Analysis

The results section displays:

- Resume Score
- Word Count
- Detected Technical Skills
- Job Role Matches
- Improvement Suggestions

### Job Matching

Users can enter a job description and compare it with their resume.

---

# 🧪 Testing

The application can be tested with different types of resumes.

### Test Cases

| Test | Expected Result |
|------|------------------|
| Upload valid PDF | Resume analyzed successfully |
| Upload non-PDF file | PDF validation error |
| Upload empty/scanned PDF | Text extraction error |
| Analyze without selecting file | File selection error |
| Match without job description | Job description error |
| Valid resume + job description | Job match result displayed |

---

# 📈 Future Improvements

Possible future improvements include:

- Advanced NLP-based resume analysis
- LLM-powered resume feedback
- ATS compatibility score
- Automatic keyword optimization
- Advanced skill extraction
- Job recommendation system
- Resume section detection
- Resume comparison
- Downloadable analysis report
- User authentication
- Database integration
- Cloud deployment
- Resume improvement using generative AI

---

# 🎓 Project Purpose

This project was developed as a practical Computer Science project to demonstrate the use of:

- Python
- FastAPI
- REST APIs
- PDF processing
- Frontend development
- File uploads
- Text analysis
- Resume scoring
- Skill matching

---

# 👨‍💻 Author

**Yogesh Kumar Yadav**

BTech Computer Science & Engineering Student

---

# 📌 Project Status

**Status: Completed ✅**

The current version supports:

- PDF resume upload
- Resume text extraction
- Resume scoring
- Word count
- Technical skill detection
- Job-role matching
- Job-description matching
- Resume improvement suggestions

---

## ⭐ If you find this project useful

Consider giving the repository a ⭐ on GitHub.