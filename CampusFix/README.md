# CampusFix — Smart Complaint Management System

A Django app for campus issue reporting, tracking, and administration. Students create accounts, file reports with an optional photo, and follow progress. Staff review all reports, assign departments, change status, and send updates.

## Features
- Student registration and login
- Responsive dashboard with counts, search, and status filtering
- Complaint categories, location, priority, description, and optional image upload
- Unique ticket IDs and a progress timeline
- Staff dashboard controls and Django Admin
- SQLite database for local development

## Run locally
Requires Python 3.10 or newer.

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000. Create a student account at `/signup/`. Staff can sign in at `/login/` to access all reports and staff controls. Django Admin is at `/admin/`.

## Deployment
This starter uses SQLite and local media serving for development. Before public deployment, load a strong secret key from an environment variable, set `DEBUG=False`, configure `ALLOWED_HOSTS`, use PostgreSQL, and configure durable media storage and HTTPS. Pillow enables image uploads. Google Fonts are an optional visual enhancement; system font fallbacks are included.
