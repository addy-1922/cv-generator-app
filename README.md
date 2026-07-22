# CV Generator App

A web application built with Python, Django, HTML, CSS, and Tailwind CSS that allows users to create and generate professional resumes through a simple and responsive interface.

## Features

- 📝 **Profile Creation** — Enter personal, education, and work details to build a profile
- 📄 **Resume Generation** — Automatically generate a formatted, downloadable resume
- 🎨 **Modern Templates** — Clean, responsive resume layouts
- 📊 **Dashboard** — View and manage created resumes
- 💾 **Download Resume** — Export resume as a downloadable file
- 💻 **Admin Panel** — Manage users and resume data via Django admin

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Tailwind CSS
- **Database:** SQLite
- **Deployment:** Render

## Project Structure

```
mysite/
├── manage.py
├── mysite/          # Project settings, URLs, WSGI/ASGI config
└── myapp/           # Core app logic
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    └── templates/myapp/
        ├── dashboard.html
        ├── modern-dashboard.html
        ├── resume.html
        ├── modern-resume.html
        ├── modern_create_profile.html
        ├── download_resume.html
        └── accept.html
```

## Getting Started

### Prerequisites
- Python 3.x
- pip

### Installation

1. Clone the repository
```bash
git clone https://github.com/addy-1922/cv-generator-app.git
cd cv-generator-app/mysite
```

2. Create and activate a virtual environment
```bash
python -m venv env
source env/Scripts/activate   # On Windows (Git Bash)
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Start the development server
```bash
python manage.py runserver
```

6. Visit `http://127.0.0.1:8000/` in your browser

## Live Demo

🔗 [Live Site](#) *(add your Render deployment link here)*

## Screenshots

*(Add screenshots of the dashboard, profile creation form, and generated resume here)*

## Future Improvements

- Multiple resume templates to choose from
- PDF export with custom styling
- LinkedIn profile import
- Resume sharing via public link

## Author

**Aditya Naik**
- GitHub: [@addy-1922](https://github.com/addy-1922)

## License

This project is open source and available for learning purposes.
