from __future__ import annotations

import sqlite3
from pathlib import Path

from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    send_from_directory,
    session,
    url_for,
)

from config.config import (
    ADMIN_PASSWORD,
    ADMIN_USERNAME,
    DB_PATH,
    SECRET_KEY,
)


# ============================================================
# APPLICATION CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates"),
    static_folder=str(BASE_DIR / "static"),
)

app.secret_key = SECRET_KEY


# ============================================================
# DEVELOPER PROFILE
# ============================================================

PROFILE = {
    "name": "Sulakshana Manchikanti",

    "title": "Computer Science Engineer | AI & ML | Software Developer",

    "short_title": "AI & ML Developer",

    "degree": "B.Tech in Computer Science & Engineering (AI & ML)",

    "college": "Srinivasa Ramanujan Institute of Technology",

    "graduation": "2027",

    "cgpa": "8.14",

    "location": "Andhra Pradesh, India",

    "email": "sulakshanamanchikanti@gmail.com",

    "phone": "+91 9392093948",

    "github": "https://github.com/sulakshana18",

    "linkedin": "https://www.linkedin.com/in/sulakshana-manchikanti-78087629/",

    "career_focus": (
        "Software Engineering, AI/ML, Full-Stack Development "
        "and Cloud Computing"
    ),
}


# ============================================================
# DATABASE CONNECTION
# ============================================================

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# ============================================================
# INITIALIZE DATABASE
# ============================================================

def init_db():

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DB_PATH) as conn:

        # ----------------------------------------------------
        # CONTACT MESSAGES TABLE
        # ----------------------------------------------------

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS contact_messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                subject TEXT NOT NULL,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        # ----------------------------------------------------
        # PORTFOLIO PROJECTS TABLE
        # ----------------------------------------------------

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS portfolio_projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                tech TEXT NOT NULL,
                image TEXT,
                link TEXT
            )
            """
        )

        # ----------------------------------------------------
        # INSERT PROJECTS ONLY IF DATABASE IS EMPTY
        # ----------------------------------------------------

        count = conn.execute(
            "SELECT COUNT(*) FROM portfolio_projects"
        ).fetchone()[0]

        if count == 0:

            projects = [

                (
                    "AI Career Guidance System",

                    (
                        "An AI-powered career guidance platform designed "
                        "to provide personalized career recommendations "
                        "based on students' skills, interests and career goals."
                    ),

                    (
                        "Python, AI/ML, NLP, React, Flask, "
                        "Supabase, REST API"
                    ),

                    (
                        "https://images.unsplash.com/"
                        "photo-1556761175-b413da4baf72"
                        "?auto=format&fit=crop&w=900&q=80"
                    ),

                    "https://github.com/sulakshana18",
                ),

                (
                    "Object Detection System",

                    (
                        "A computer vision application using YOLO and "
                        "OpenCV for detecting and identifying objects "
                        "from images and video."
                    ),

                    (
                        "Python, YOLO, OpenCV, Computer Vision, "
                        "Deep Learning"
                    ),

                    (
                        "https://images.unsplash.com/"
                        "photo-1516321318423-f06f85e504b3"
                        "?auto=format&fit=crop&w=900&q=80"
                    ),

                    "https://github.com/sulakshana18",
                ),

                (
                    "Student Management System",

                    (
                        "A CRUD-based student management application "
                        "for adding, viewing, updating and managing "
                        "student records using programming and database concepts."
                    ),

                    (
                        "Python, HTML, CSS, JavaScript, SQL"
                    ),

                    (
                        "https://images.unsplash.com/"
                        "photo-1523240795612-9a054b0db644"
                        "?auto=format&fit=crop&w=900&q=80"
                    ),

                    "https://github.com/sulakshana18",
                ),

                (
                    "College Portal",

                    (
                        "A full-stack web application designed to provide "
                        "college-related information and functionality "
                        "through a structured and responsive interface."
                    ),

                    (
                        "HTML, CSS, JavaScript, React, "
                        "Backend, Database"
                    ),

                    (
                        "https://images.unsplash.com/"
                        "photo-1522202176988-66273c2fd55f"
                        "?auto=format&fit=crop&w=900&q=80"
                    ),

                    "https://github.com/sulakshana18",
                ),

                (
                    "Signature Matching System",

                    (
                        "A computer vision and image-processing based "
                        "application focused on comparing signature "
                        "samples and identifying similarities."
                    ),

                    (
                        "Python, Image Processing, "
                        "Computer Vision"
                    ),

                    (
                        "https://images.unsplash.com/"
                        "photo-1551288049-bebda4e38f71"
                        "?auto=format&fit=crop&w=900&q=80"
                    ),

                    "https://github.com/sulakshana18",
                ),

            ]

            conn.executemany(
                """
                INSERT INTO portfolio_projects
                (title, description, tech, image, link)
                VALUES (?, ?, ?, ?, ?)
                """,
                projects,
            )

        conn.commit()


# ============================================================
# INITIALIZE DATABASE WHEN APPLICATION STARTS
# ============================================================

init_db()


# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def index():

    conn = get_db_connection()

    project_list = conn.execute(
        """
        SELECT *
        FROM portfolio_projects
        ORDER BY id ASC
        """
    ).fetchall()

    conn.close()

    return render_template(
        "index.html",
        title="Home",
        profile=PROFILE,
        projects=project_list,
    )


# ============================================================
# ABOUT PAGE
# ============================================================

@app.route("/about")
def about():

    return render_template(
        "about.html",
        title="About",
        profile=PROFILE,
    )


# ============================================================
# PROJECTS PAGE
# ============================================================

@app.route("/projects")
def projects():

    conn = get_db_connection()

    project_list = conn.execute(
        """
        SELECT *
        FROM portfolio_projects
        ORDER BY id ASC
        """
    ).fetchall()

    conn.close()

    return render_template(
        "projects.html",
        title="Projects",
        projects=project_list,
        profile=PROFILE,
    )


# ============================================================
# CERTIFICATIONS PAGE
# ============================================================

@app.route("/certifications")
def certifications():

    certifications_list = [

        {
            "name": "AWS Certified Cloud Practitioner",
            "issuer": "Amazon Web Services (AWS)",
            "year": "2026",
            "description": (
                "Foundational knowledge of AWS Cloud concepts, "
                "core AWS services, cloud security, pricing, "
                "billing and cloud computing fundamentals."
            ),
        },

    ]

    return render_template(
        "certifications.html",
        title="Certifications",
        certifications=certifications_list,
        profile=PROFILE,
    )


# ============================================================
# CONTACT PAGE
# ============================================================

@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form.get("name", "").strip()

        email = request.form.get("email", "").strip()

        subject = request.form.get("subject", "").strip()

        message = request.form.get("message", "").strip()


        # ----------------------------------------------------
        # VALIDATE FORM
        # ----------------------------------------------------

        if not all([name, email, subject, message]):

            flash(
                "Please fill in all form fields.",
                "danger"
            )

            return redirect(url_for("contact"))


        # ----------------------------------------------------
        # SAVE MESSAGE
        # ----------------------------------------------------

        conn = get_db_connection()

        conn.execute(
            """
            INSERT INTO contact_messages
            (name, email, subject, message)
            VALUES (?, ?, ?, ?)
            """,
            (
                name,
                email,
                subject,
                message,
            ),
        )

        conn.commit()

        conn.close()


        flash(
            "Your message has been sent successfully. "
            "I will get back to you soon!",
            "success",
        )

        return redirect(url_for("contact"))


    return render_template(
        "contact.html",
        title="Contact",
        profile=PROFILE,
    )


# ============================================================
# ADMIN LOGIN
# ============================================================

@app.route("/admin", methods=["GET", "POST"])
def admin():

    if request.method == "POST":

        username = request.form.get(
            "username",
            ""
        )

        password = request.form.get(
            "password",
            ""
        )


        # ----------------------------------------------------
        # CHECK ADMIN CREDENTIALS
        # ----------------------------------------------------

        if (
            username == ADMIN_USERNAME
            and password == ADMIN_PASSWORD
        ):

            session["admin_logged_in"] = True

            return redirect(
                url_for("admin_dashboard")
            )


        flash(
            "Invalid username or password.",
            "danger",
        )


    return render_template(
        "admin.html",
        title="Admin Login",
        admin_page=True,
        profile=PROFILE,
    )


# ============================================================
# ADMIN DASHBOARD
# ============================================================

@app.route("/admin/dashboard")
def admin_dashboard():

    # --------------------------------------------------------
    # CHECK LOGIN
    # --------------------------------------------------------

    if not session.get("admin_logged_in"):

        flash(
            "Please log in to access the admin dashboard.",
            "warning",
        )

        return redirect(
            url_for("admin")
        )


    # --------------------------------------------------------
    # GET CONTACT MESSAGES
    # --------------------------------------------------------

    conn = get_db_connection()

    messages = conn.execute(
        """
        SELECT *
        FROM contact_messages
        ORDER BY created_at DESC
        """
    ).fetchall()

    conn.close()


    return render_template(
        "admin.html",
        title="Admin Dashboard",
        admin_page=False,
        messages=messages,
        profile=PROFILE,
    )


# ============================================================
# ADMIN LOGOUT
# ============================================================

@app.route("/admin/logout")
def admin_logout():

    session.pop(
        "admin_logged_in",
        None
    )

    flash(
        "You have been logged out.",
        "info"
    )

    return redirect(
        url_for("admin")
    )


# ============================================================
# RESUME
# ============================================================

@app.route("/resume")
def resume():
    resume_path = BASE_DIR / "static" / "resume" / "Sulakshana_Manchikanti_Resume.pdf"

    if resume_path.exists():
        return send_from_directory(
            str(resume_path.parent),
            resume_path.name,
            as_attachment=True,
        )

    return redirect(url_for("index"))


# ============================================================
# APPLICATION ENTRY POINT
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000,
    )