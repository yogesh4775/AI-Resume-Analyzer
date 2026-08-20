import re


# ============================================================
# JOB ROLES
# ============================================================

JOB_ROLES = {

    "Python Developer": [
        "python",
        "django",
        "flask",
        "fastapi",
        "sql",
    ],

    "Web Developer": [
        "html",
        "css",
        "javascript",
        "react",
        "node.js",
    ],

    "Frontend Developer": [
        "html",
        "css",
        "javascript",
        "react",
        "typescript",
    ],

    "Backend Developer": [
        "python",
        "java",
        "node.js",
        "express",
        "django",
        "flask",
        "fastapi",
        "sql",
        "mongodb",
    ],

    "Data Analyst": [
        "python",
        "pandas",
        "numpy",
        "sql",
        "excel",
        "matplotlib",
    ],

    "Machine Learning Engineer": [
        "python",
        "machine learning",
        "scikit-learn",
        "tensorflow",
        "pytorch",
        "numpy",
        "pandas",
    ],

    "Full Stack Developer": [
        "html",
        "css",
        "javascript",
        "react",
        "node.js",
        "sql",
        "mongodb",
    ],

    "DevOps Engineer": [
        "linux",
        "docker",
        "kubernetes",
        "aws",
        "git",
    ],
}


# ============================================================
# ADDITIONAL TECHNICAL SKILLS
# ============================================================

TECHNICAL_SKILLS = [

    "python",
    "java",
    "c++",
    "c#",
    "c",

    "javascript",
    "typescript",

    "html",
    "css",

    "react",
    "angular",
    "vue",

    "node.js",
    "express",

    "django",
    "flask",
    "fastapi",

    "sql",
    "mysql",
    "postgresql",
    "mongodb",

    "git",
    "github",

    "docker",
    "kubernetes",

    "aws",
    "azure",
    "gcp",

    "linux",

    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",

    "scikit-learn",
    "tensorflow",
    "pytorch",

    "machine learning",
    "deep learning",

    "data analysis",
    "data science",

    "rest api",
    "api",

    "oop",
    "dsa",
    "data structures",
    "algorithms",

    "excel",
]


# ============================================================
# SKILL EXISTENCE
# ============================================================

def skill_exists(text, skill):

    text_lower = text.lower()

    skill_lower = skill.lower()


    # --------------------------------------------------------
    # C++
    # --------------------------------------------------------

    if skill_lower == "c++":

        return bool(
            re.search(
                r"(?<!\w)c\+\+(?!\w)",
                text_lower
            )
        )


    # --------------------------------------------------------
    # C#
    # --------------------------------------------------------

    if skill_lower == "c#":

        return bool(
            re.search(
                r"(?<!\w)c#(?!\w)",
                text_lower
            )
        )


    # --------------------------------------------------------
    # C
    # --------------------------------------------------------

    if skill_lower == "c":

        patterns = [

            r"\bc programming\b",

            r"\bc language\b",

            r"\bc developer\b",

            r"\bc\/c\+\+\b",

            r"\bc and c\+\+\b",

        ]

        return any(
            re.search(
                pattern,
                text_lower
            )
            for pattern in patterns
        )


    # --------------------------------------------------------
    # Go
    # --------------------------------------------------------

    if skill_lower == "go":

        patterns = [

            r"\bgo programming\b",

            r"\bgolang\b",

            r"\bgo language\b",

        ]

        return any(
            re.search(
                pattern,
                text_lower
            )
            for pattern in patterns
        )


    # --------------------------------------------------------
    # Normal skill
    # --------------------------------------------------------

    pattern = (

        r"(?<!\w)"

        + re.escape(skill_lower)

        + r"(?!\w)"

    )


    return bool(
        re.search(
            pattern,
            text_lower
        )
    )


# ============================================================
# DETECT SKILLS
# ============================================================

def detect_skills(text):

    detected = []


    for skill in TECHNICAL_SKILLS:

        if skill_exists(
            text,
            skill
        ):

            detected.append(skill)


    return detected


# ============================================================
# WORD COUNT
# ============================================================

def calculate_word_count(text):

    if not text:

        return 0


    words = re.findall(
        r"\b[\w+#.-]+\b",
        text
    )


    return len(words)


# ============================================================
# RESUME SCORE
# ============================================================

def calculate_resume_score(
    text,
    skills
):

    text_lower = text.lower()


    score = 0


    # --------------------------------------------------------
    # Technical skills
    # --------------------------------------------------------

    skill_score = min(
        len(skills) * 4,
        30
    )

    score += skill_score


    # --------------------------------------------------------
    # Sections
    # --------------------------------------------------------

    sections = [

        "education",

        "experience",

        "project",

        "skills",

        "summary",

        "objective",

        "certification",

    ]


    section_count = 0


    for section in sections:

        if section in text_lower:

            section_count += 1


    score += min(
        section_count * 5,
        30
    )


    # --------------------------------------------------------
    # Contact / profile
    # --------------------------------------------------------

    contact_items = [

        "email",

        "phone",

        "linkedin",

        "github",

    ]


    contact_count = 0


    for item in contact_items:

        if item in text_lower:

            contact_count += 1


    score += min(
        contact_count * 5,
        20
    )


    # --------------------------------------------------------
    # Experience / projects
    # --------------------------------------------------------

    if "experience" in text_lower:

        score += 5


    if "project" in text_lower:

        score += 5


    # --------------------------------------------------------
    # Final score
    # --------------------------------------------------------

    return min(
        score,
        100
    )


# ============================================================
# JOB ROLE MATCHING
# ============================================================

def match_job_roles(skills):

    resume_skills = set(
        skill.lower()
        for skill in skills
    )


    results = []


    for role, required_skills in JOB_ROLES.items():

        matched_skills = []


        for skill in required_skills:

            if skill.lower() in resume_skills:

                matched_skills.append(
                    skill
                )


        if required_skills:

            percentage = round(

                (
                    len(matched_skills)
                    /
                    len(required_skills)
                )
                * 100

            )

        else:

            percentage = 0


        results.append({

            "role":
                role,

            "match_percentage":
                percentage,

            "matched_skills":
                matched_skills,

        })


    # Highest match first

    results.sort(

        key=lambda x:
            x["match_percentage"],

        reverse=True

    )


    return results


# ============================================================
# JOB DESCRIPTION SKILL DETECTION
# ============================================================

def detect_job_description_skills(
    job_description
):

    return detect_skills(
        job_description
    )


# ============================================================
# JOB DESCRIPTION MATCHING
# ============================================================

def match_job_description(
    resume_text,
    job_description
):

    # --------------------------------------------------------
    # Detect resume skills
    # --------------------------------------------------------

    resume_skills = detect_skills(
        resume_text
    )


    # --------------------------------------------------------
    # Detect job description skills
    # --------------------------------------------------------

    jd_skills = detect_job_description_skills(
        job_description
    )


    resume_skill_set = set(

        skill.lower()
        for skill in resume_skills

    )


    jd_skill_set = set(

        skill.lower()
        for skill in jd_skills

    )


    # --------------------------------------------------------
    # Matched skills
    # --------------------------------------------------------

    matched_skills = []


    for skill in jd_skills:

        if skill.lower() in resume_skill_set:

            matched_skills.append(
                skill
            )


    # --------------------------------------------------------
    # Missing skills
    # --------------------------------------------------------

    missing_skills = []


    for skill in jd_skills:

        if skill.lower() not in resume_skill_set:

            missing_skills.append(
                skill
            )


    # --------------------------------------------------------
    # Match percentage
    # --------------------------------------------------------

    if len(jd_skills) > 0:

        match_percentage = round(

            (
                len(matched_skills)
                /
                len(jd_skills)
            )
            * 100

        )

    else:

        # If no recognized technical
        # skills exist in JD

        match_percentage = 0


    # --------------------------------------------------------
    # Suggestions
    # --------------------------------------------------------

    suggestions = []


    if missing_skills:

        suggestions.append(

            "Consider adding these relevant "
            "skills if you have experience with them: "
            + ", ".join(
                missing_skills
            )

        )


    if match_percentage < 40:

        suggestions.append(

            "Your resume has a low skill match "
            "with this job description. Consider "
            "tailoring your resume to the role."

        )


    elif match_percentage < 70:

        suggestions.append(

            "Your resume has a moderate match. "
            "Add relevant skills and projects "
            "from the job description where applicable."

        )


    else:

        suggestions.append(

            "Your resume has a strong technical "
            "skill match with this job description."

        )


    # --------------------------------------------------------
    # Return result
    # --------------------------------------------------------

    return {

        "match_percentage":
            match_percentage,

        "matched_skills":
            matched_skills,

        "missing_skills":
            missing_skills,

        "resume_skills":
            resume_skills,

        "job_description_skills":
            jd_skills,

        "suggestions":
            suggestions,

    }


# ============================================================
# RESUME IMPROVEMENT SUGGESTIONS
# ============================================================

def generate_suggestions(
    text,
    skills
):

    suggestions = []


    text_lower = text.lower()


    word_count = calculate_word_count(text)

    # --------------------------------------------------------
    # Skills
    # --------------------------------------------------------

    if len(skills) < 5:

        suggestions.append(

            "Add more relevant technical skills "
            "based on your target job role."

        )


    # --------------------------------------------------------
    # Experience
    # --------------------------------------------------------

    if "experience" not in text_lower:

        suggestions.append(

            "Add an internship, work experience, "
            "or relevant practical experience section."

        )


    # --------------------------------------------------------
    # Projects
    # --------------------------------------------------------

    if "project" not in text_lower:

        suggestions.append(

            "Add 2-3 projects with technologies used "
            "and measurable results."

        )


    # --------------------------------------------------------
    # Education
    # --------------------------------------------------------

    if "education" not in text_lower:

        suggestions.append(

            "Add a clear education section with "
            "degree, university and CGPA/percentage."

        )


    # --------------------------------------------------------
    # Achievements
    # --------------------------------------------------------

    achievement_keywords = [

        "achieved",

        "improved",

        "increased",

        "reduced",

        "optimized",

        "developed",

        "implemented",

    ]


    has_achievement = any(

        keyword in text_lower

        for keyword in achievement_keywords

    )


    if not has_achievement:

        suggestions.append(

            "Use measurable achievements in your "
            "project and experience descriptions."

        )


    # --------------------------------------------------------
    # Resume length
    # --------------------------------------------------------

    if word_count < 150:

        suggestions.append(

            "Your resume is quite short. Add more "
            "relevant projects, skills and achievements."

        )


    elif word_count > 900:

        suggestions.append(

            "Your resume is quite long. Remove "
            "unnecessary information and keep it concise."

        )


    # --------------------------------------------------------
    # LinkedIn
    # --------------------------------------------------------

    if "linkedin" not in text_lower:

        suggestions.append(

            "Consider adding your LinkedIn profile."

        )


    # --------------------------------------------------------
    # GitHub
    # --------------------------------------------------------

    if "github" not in text_lower:

        suggestions.append(

            "Consider adding your GitHub profile "
            "to showcase coding projects."

        )


    # --------------------------------------------------------
    # Default
    # --------------------------------------------------------

    if not suggestions:

        suggestions.append(

            "Your resume has a strong basic structure. "
            "Focus on measurable achievements and "
            "tailoring it to each job description."

        )


    return suggestions


# ============================================================
# COMPLETE RESUME ANALYSIS
# ============================================================

def analyze_resume(text):

    # Detect skills

    skills = detect_skills(
        text
    )


    # Word count

    word_count = calculate_word_count(
        text
    )


    # Resume score

    score = calculate_resume_score(

        text,

        skills

    )


    # Job roles

    job_roles = match_job_roles(
        skills
    )


    # Suggestions

    suggestions = generate_suggestions(

        text,

        skills

    )


    return {

        "score":
            score,

        "word_count":
            word_count,

        "skills":
            skills,

        "job_roles":
            job_roles,

        "suggestions":
            suggestions,

    }