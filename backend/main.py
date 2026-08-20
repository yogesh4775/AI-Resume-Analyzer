from fastapi import (
    FastAPI,
    UploadFile,
    File,
    Form
)

from fastapi.middleware.cors import CORSMiddleware

import os
import shutil
import uuid


from backend.resume_parser import (
    extract_text_from_pdf
)

from backend.analyzer import (
    analyze_resume,
    match_job_description
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
# UPLOAD DIRECTORY
# ============================================================

UPLOAD_DIR = "../uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


# ============================================================
# HOME
# ============================================================

@app.get("/")
def home():

    return {

        "message":
            "AI Resume Analyzer API is running"

    }


# ============================================================
# RESUME ANALYSIS
# ============================================================

@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...)
):

    # --------------------------------------------------------
    # Check file
    # --------------------------------------------------------

    if not file.filename:

        return {

            "error":
                "No file selected."

        }


    # --------------------------------------------------------
    # Check PDF
    # --------------------------------------------------------

    if not file.filename.lower().endswith(".pdf"):

        return {

            "error":
                "Only PDF files are allowed."

        }


    # --------------------------------------------------------
    # Create safe filename
    # --------------------------------------------------------

    safe_filename = (
        str(uuid.uuid4())
        + ".pdf"
    )


    file_path = os.path.join(

        UPLOAD_DIR,

        safe_filename

    )


    # --------------------------------------------------------
    # Save uploaded file
    # --------------------------------------------------------

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )


    # --------------------------------------------------------
    # Extract text
    # --------------------------------------------------------

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


    # --------------------------------------------------------
    # Check extracted text
    # --------------------------------------------------------

    if not text or not text.strip():

        return {

            "error":
                "Could not extract text from this PDF. "
                "Please upload a text-based PDF."

        }


    # --------------------------------------------------------
    # Analyze resume
    # --------------------------------------------------------

    result = analyze_resume(
        text
    )


    return {

        "filename":
            file.filename,

        "analysis":
            result

    }


# ============================================================
# JOB DESCRIPTION MATCHING
# ============================================================

@app.post("/match-job")
async def match_job(

    file: UploadFile = File(...),

    job_description: str = Form(...)

):

    # --------------------------------------------------------
    # Check file
    # --------------------------------------------------------

    if not file.filename:

        return {

            "error":
                "No resume file selected."

        }


    # --------------------------------------------------------
    # Check PDF
    # --------------------------------------------------------

    if not file.filename.lower().endswith(".pdf"):

        return {

            "error":
                "Only PDF files are allowed."

        }


    # --------------------------------------------------------
    # Check Job Description
    # --------------------------------------------------------

    if not job_description.strip():

        return {

            "error":
                "Please enter a job description."

        }


    # --------------------------------------------------------
    # Create temporary filename
    # --------------------------------------------------------

    safe_filename = (

        str(uuid.uuid4())

        + ".pdf"

    )


    file_path = os.path.join(

        UPLOAD_DIR,

        safe_filename

    )


    # --------------------------------------------------------
    # Save PDF
    # --------------------------------------------------------

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )


    # --------------------------------------------------------
    # Extract resume text
    # --------------------------------------------------------

    try:

        resume_text = (
            extract_text_from_pdf(
                file_path
            )
        )

    except Exception as error:

        return {

            "error":
                "Could not read the resume PDF: "
                + str(error)

        }


    # --------------------------------------------------------
    # Validate resume text
    # --------------------------------------------------------

    if not resume_text or not resume_text.strip():

        return {

            "error":
                "Could not extract text from the resume."

        }


    # --------------------------------------------------------
    # Match Resume vs Job Description
    # --------------------------------------------------------

    result = match_job_description(

        resume_text,

        job_description

    )


    # --------------------------------------------------------
    # Return result
    # --------------------------------------------------------

    return {

        "filename":
            file.filename,

        "job_match":
            result

    }