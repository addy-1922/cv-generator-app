# 📄 CV Generator

A web-based **CV Generator** built with **Python** and **Django** that enables users to create professional resumes through a simple and intuitive interface. Users can enter their personal, educational, and professional details to generate a well-structured resume and download it as a PDF.

## 🌐 Live Demo

**[View CV Generator](https://cv-generator-app-bvjr.onrender.com/)**

> Hosted on Render's free tier. The first load can take around 50 seconds while the server wakes up. Data may reset when the app restarts.

---

## 🚀 Features

- Create professional resumes
- Add personal information
- Manage education details
- Add work experience
- Add technical and soft skills
- Showcase projects
- Add certifications
- Preview resume before downloading
- Download resume as PDF
- Responsive user interface
- Django Admin Panel

---

## 🛠️ Tech Stack

### Backend
- Python
- Django

### Frontend
- HTML5
- CSS3
- JavaScript
- Tailwind CSS

### Database
- SQLite

### Tools
- Git
- GitHub
- Render (deployment)

---

## 📂 Project Structure

```text
cv-generator-app/
├── mysite/
│   ├── manage.py
│   ├── mysite/          # project settings, urls, wsgi/asgi
│   └── myapp/           # app: models, views, urls, templates, migrations
├── docs/                # screenshots and extra files
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/addy-1922/cv-generator-app.git
cd cv-generator-app
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
cd mysite
```

### Apply migrations

```bash
python manage.py migrate
```

### Run the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

---

## 👨‍💻 Author

**Aditya Naik**

GitHub: https://github.com/addy-1922
