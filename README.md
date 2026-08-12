# Sulakshana Portfolio

A modern personal portfolio website built with Python and Flask. It includes sections for home, about, projects, certifications, contact, and a simple admin panel for viewing messages.

## Project Structure

- `app.py` - Flask application entry point
- `config/config.py` - Application configuration and credentials
- `database/portfolio.db` - SQLite database for contact form and project data
- `templates/` - HTML pages
- `static/` - CSS, JavaScript, and images

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open the app in your browser:
   ```text
   http://127.0.0.1:5000
   ```

## Admin Login

- Username: `admin`
- Password: `admin123`

## Notes

- Update your own resume and profile details in the templates and config.
- Add real project images and certification assets in the `static/images/` folder.
