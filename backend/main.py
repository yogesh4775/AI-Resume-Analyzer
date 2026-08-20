from fastapi import (
    FastAPI,
    UploadFile,
    File,
    Form
)

from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import os
import shutil
import uuid

from backend.resume_parser import extract_text_from_pdf

from backend.analyzer import (
    analyze_resume,
    match_job_description
)


# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

UPLOAD_DIR = os.path.join(
    BASE_DIR,
    "uploads"
)

FRONTEND_DIR = os.path.join(
    BASE_DIR,
    "frontend"
)

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


# ============================================================
# FASTAPI APP
# ============================================================

app = FastAPI(
    title="AI Resume Analyzer"
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# RESUME ANALYSIS
# ============================================================

@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...)
):

    if not file.filename:
        return {
            "error": "No file selected."
        }

    if not file.filename.lower().endswith(".pdf"):
        return {
            "error": "Only PDF files are allowed."
        }

    safe_filename = (
        str(uuid.uuid4()) + ".pdf"
    )

    file_path = os.path.join(
        UPLOAD_DIR,
        safe_filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    try:

        text = extract_text_from_pdf(
            file_path
        )

    except Exception as error:

        return {
            "error":
                "Could not read the PDF: "
                + str(error)
        }

    if not text or not text.strip():

        return {
            "error":
                "Could not extract text from this PDF. "
                "Please upload a text-based PDF."
        }

    result = analyze_resume(
        text
    )

    return {
        "filename": file.filename,
        "analysis": result
    }


# ============================================================
# JOB DESCRIPTION MATCHING
# ============================================================

@app.post("/match-job")
async def match_job(

    file: UploadFile = File(...),

    job_description: str = Form(...)

):

    if not file.filename:

        return {
            "error":
                "No resume file selected."
        }

    if not file.filename.lower().endswith(".pdf"):

        return {
            "error":
                "Only PDF files are allowed."
        }

    if not job_description.strip():

        return {
            "error":
                "Please enter a job description."
        }

    safe_filename = (
        str(uuid.uuid4()) + ".pdf"
    )

    file_path = os.path.join(
        UPLOAD_DIR,
        safe_filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    try:

        resume_text = extract_text_from_pdf(
            file_path
        )

    except Exception as error:

        return {
            "error":
                "Could not read the resume PDF: "
                + str(error)
        }

    if not resume_text or not resume_text.strip():

        return {
            "error":
                "Could not extract text from the resume."
        }

    result = match_job_description(
        resume_text,
        job_description
    )

    return {
        "filename": file.filename,
        "job_match": result
    }


# ============================================================
# FRONTEND
# ============================================================

app.mount(
    "/",
    StaticFiles(
        directory=FRONTEND_DIR,
        html=True
    ),
    name="frontend"
)