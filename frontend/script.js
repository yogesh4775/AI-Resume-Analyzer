// ============================================================
// AI RESUME ANALYZER - SCRIPT.JS
// ============================================================


// ============================================================
// ELEMENTS
// ============================================================

const resumeFile = document.getElementById("resumeFile");

const fileName = document.getElementById("fileName");

const analyzeBtn = document.getElementById("analyzeBtn");

const statusText = document.getElementById("status");

const results = document.getElementById("results");

const scoreElement = document.getElementById("score");

const wordCountElement =
    document.getElementById("wordCount");

const skillsElement =
    document.getElementById("skills");

const jobRolesElement =
    document.getElementById("jobRoles");

const suggestionsElement =
    document.getElementById("suggestions");


// Job matching elements

const jobDescription =
    document.getElementById("jobDescription");

const matchJobBtn =
    document.getElementById("matchJobBtn");

const jobMatchResult =
    document.getElementById("jobMatchResult");


// ============================================================
// INITIAL STATE
// ============================================================

results.style.display = "none";


// ============================================================
// FILE SELECTION
// ============================================================

resumeFile.addEventListener("change", () => {

    if (resumeFile.files.length === 0) {

        fileName.textContent =
            "No file selected";

        statusText.textContent = "";

        return;
    }


    const file =
        resumeFile.files[0];


    // Check PDF

    if (
        file.type !== "application/pdf" &&
        !file.name.toLowerCase().endsWith(".pdf")
    ) {

        fileName.textContent =
            "Please select a PDF file.";

        resumeFile.value = "";

        return;
    }


    fileName.textContent =
        file.name;

    statusText.textContent =
        "";

});


// ============================================================
// ANALYZE RESUME
// ============================================================

analyzeBtn.addEventListener(
    "click",
    async () => {

        // Check file

        if (resumeFile.files.length === 0) {

            statusText.textContent =
                "Please select a PDF resume first.";

            return;
        }


        const file =
            resumeFile.files[0];


        // Check PDF

        if (
            file.type !== "application/pdf" &&
            !file.name.toLowerCase().endsWith(".pdf")
        ) {

            statusText.textContent =
                "Please upload a PDF file.";

            return;
        }


        // Disable button

        analyzeBtn.disabled = true;

        analyzeBtn.textContent =
            "Analyzing...";


        statusText.textContent =
            "Uploading and analyzing your resume...";


        // FormData

        const formData =
            new FormData();


        formData.append(
            "file",
            file
        );


        try {

            const response =
                await fetch(
                    "http://127.0.0.1:8000/analyze",
                    {
                        method: "POST",
                        body: formData
                    }
                );


            const data =
                await response.json();


            // Backend error

            if (
                !response.ok ||
                data.error
            ) {

                throw new Error(
                    data.error ||
                    "Resume analysis failed."
                );

            }


            // Display results

            displayResults(
                data.analysis
            );


            statusText.textContent =
                "Resume analyzed successfully!";


        } catch (error) {

            console.error(error);


            statusText.textContent =
                "Error: " + error.message;


        } finally {

            analyzeBtn.disabled = false;

            analyzeBtn.textContent =
                "Analyze Resume";

        }

    }
);


// ============================================================
// DISPLAY RESUME RESULTS
// ============================================================

function displayResults(analysis) {

    results.style.display =
        "block";


    // Score

    scoreElement.textContent =
        analysis.score ?? 0;


    // Word count

    wordCountElement.textContent =
        analysis.word_count ?? 0;


    // Skills

    displaySkills(
        analysis.skills
    );


    // Job roles

    displayJobRoles(
        analysis.job_roles
    );


    // Suggestions

    displaySuggestions(
        analysis.suggestions
    );


    // Scroll

    results.scrollIntoView({
        behavior: "smooth",
        block: "start"
    });

}


// ============================================================
// DISPLAY SKILLS
// ============================================================

function displaySkills(skills) {

    skillsElement.innerHTML =
        "";


    if (
        !skills ||
        skills.length === 0
    ) {

        skillsElement.innerHTML =
            "<p>No technical skills detected.</p>";

        return;
    }


    skills.forEach(
        skill => {

            const skillElement =
                document.createElement("span");


            skillElement.className =
                "skill";


            skillElement.textContent =
                skill;


            skillsElement.appendChild(
                skillElement
            );

        }
    );

}


// ============================================================
// DISPLAY JOB ROLES
// ============================================================

function displayJobRoles(jobRoles) {

    jobRolesElement.innerHTML =
        "";


    if (
        !jobRoles ||
        jobRoles.length === 0
    ) {

        jobRolesElement.innerHTML =
            "<p>No suitable job roles found.</p>";

        return;
    }


    jobRoles.forEach(
        job => {

            const roleElement =
                document.createElement("div");


            roleElement.className =
                "job-role";


            const role =
                job.role || "Unknown Role";


            const percentage =
                job.match_percentage ?? 0;


            const matchedSkills =
                job.matched_skills || [];


            roleElement.innerHTML = `

                <div class="job-role-header">

                    <strong>
                        ${escapeHtml(role)}
                    </strong>

                    <span class="match">
                        ${percentage}% Match
                    </span>

                </div>


                <div class="progress">

                    <div
                        class="progress-bar"
                        style="width: ${percentage}%"
                    ></div>

                </div>


                <p style="margin-top: 10px;">

                    <strong>
                        Matched skills:
                    </strong>

                    ${
                        matchedSkills.length > 0
                        ? matchedSkills
                            .map(skill =>
                                escapeHtml(skill)
                            )
                            .join(", ")
                        : "None"
                    }

                </p>

            `;


            jobRolesElement.appendChild(
                roleElement
            );

        }
    );

}


// ============================================================
// DISPLAY SUGGESTIONS
// ============================================================

function displaySuggestions(
    suggestions
) {

    suggestionsElement.innerHTML =
        "";


    if (
        !suggestions ||
        suggestions.length === 0
    ) {

        suggestionsElement.innerHTML =
            "<li>No suggestions available.</li>";

        return;
    }


    suggestions.forEach(
        suggestion => {

            const listItem =
                document.createElement("li");


            listItem.textContent =
                suggestion;


            suggestionsElement.appendChild(
                listItem
            );

        }
    );

}


// ============================================================
// JOB DESCRIPTION MATCHING
// ============================================================

matchJobBtn.addEventListener(
    "click",
    async () => {

        // Check resume

        if (resumeFile.files.length === 0) {

            showJobMessage(
                "Please select your resume PDF first.",
                true
            );

            return;
        }


        // Check job description

        if (
            !jobDescription.value.trim()
        ) {

            showJobMessage(
                "Please enter a job description.",
                true
            );

            return;
        }


        const file =
            resumeFile.files[0];


        // Check PDF

        if (
            file.type !== "application/pdf" &&
            !file.name.toLowerCase().endsWith(".pdf")
        ) {

            showJobMessage(
                "Please upload a PDF resume.",
                true
            );

            return;
        }


        // Disable button

        matchJobBtn.disabled = true;

        matchJobBtn.textContent =
            "Matching...";


        jobMatchResult.innerHTML = `
            <p>
                Comparing your resume with the job description...
            </p>
        `;


        // FormData

        const formData =
            new FormData();


        formData.append(
            "file",
            file
        );


        formData.append(
            "job_description",
            jobDescription.value.trim()
        );


        try {

            const response =
                await fetch(
                    "http://127.0.0.1:8000/match-job",
                    {
                        method: "POST",
                        body: formData
                    }
                );


            const data =
                await response.json();


            // Backend error

            if (
                !response.ok ||
                data.error
            ) {

                throw new Error(
                    data.error ||
                    "Job matching failed."
                );

            }


            // Get actual result

            const result =
                data.job_match ||
                data.analysis ||
                data;


            displayJobMatchResult(
                result
            );


        } catch (error) {

            console.error(error);


            jobMatchResult.innerHTML = `
                <p class="error-message">
                    Error: ${escapeHtml(error.message)}
                </p>
            `;


        } finally {

            matchJobBtn.disabled = false;

            matchJobBtn.textContent =
                "Match With Job";

        }

    }
);


// ============================================================
// DISPLAY JOB MATCH RESULT
// ============================================================

function displayJobMatchResult(
    result
) {

    if (!result) {

        jobMatchResult.innerHTML = `
            <p class="error-message">
                No job matching result received.
            </p>
        `;

        return;
    }


    // Match percentage

    const percentage =
        result.match_percentage ??
        result.match ??
        result.score ??
        0;


    // Matched skills

    const matchedSkills =
        result.matched_skills || [];


    // Missing skills

    const missingSkills =
        result.missing_skills || [];


    // Suggestions

    const suggestions =
        result.suggestions || [];


    // Build matched skills HTML

    let matchedSkillsHTML =
        "<p>No matching skills found.</p>";


    if (
        matchedSkills.length > 0
    ) {

        matchedSkillsHTML =
            matchedSkills
                .map(
                    skill => `
                        <span class="skill matched-skill">
                            ${escapeHtml(skill)}
                        </span>
                    `
                )
                .join("");

    }


    // Build missing skills HTML

    let missingSkillsHTML =
        "<p>No major missing skills.</p>";


    if (
        missingSkills.length > 0
    ) {

        missingSkillsHTML =
            missingSkills
                .map(
                    skill => `
                        <span class="skill missing-skill">
                            ${escapeHtml(skill)}
                        </span>
                    `
                )
                .join("");

    }


    // Build suggestions HTML

    let suggestionsHTML =
        "<li>No additional suggestions.</li>";


    if (
        suggestions.length > 0
    ) {

        suggestionsHTML =
            suggestions
                .map(
                    suggestion => `
                        <li>
                            ${escapeHtml(suggestion)}
                        </li>
                    `
                )
                .join("");

    }


    // Result HTML

    jobMatchResult.innerHTML = `

        <div class="job-match-result">

            <h3>
                🎯 Job Match Result
            </h3>


            <div class="match-score">

                <span>
                    ${percentage}%
                </span>

                <small>
                    Match
                </small>

            </div>


            <div class="match-progress">

                <div
                    class="match-progress-bar"
                    style="width: ${percentage}%"
                ></div>

            </div>


            <div class="match-details">


                <div>

                    <h4>
                        ✅ Matched Skills
                    </h4>

                    <div class="skills-container">

                        ${matchedSkillsHTML}

                    </div>

                </div>


                <div>

                    <h4>
                        ❌ Missing Skills
                    </h4>

                    <div class="skills-container">

                        ${missingSkillsHTML}

                    </div>

                </div>


                <div>

                    <h4>
                        💡 Recommendations
                    </h4>

                    <ul>
                        ${suggestionsHTML}
                    </ul>

                </div>


            </div>

        </div>

    `;


    // Scroll to result

    jobMatchResult.scrollIntoView({
        behavior: "smooth",
        block: "start"
    });

}


// ============================================================
// JOB MESSAGE
// ============================================================

function showJobMessage(
    message,
    isError = false
) {

    jobMatchResult.innerHTML = `

        <p class="${isError ? "error-message" : ""}">
            ${escapeHtml(message)}
        </p>

    `;

}


// ============================================================
// HTML ESCAPE
// ============================================================

function escapeHtml(value) {

    if (value === null || value === undefined) {

        return "";

    }


    return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");

}