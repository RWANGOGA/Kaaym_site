# Kaaym_site


## Development setup

Backend (Django)

1. Create and activate a virtual environment:

   Windows (PowerShell):

   ```powershell
   python -m venv .venv; .\.venv\Scripts\Activate.ps1
   ```

2. Install Python dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. Create `.env` (or use environment variables) and configure settings (SECRET_KEY, DATABASE_URL, etc.).

4. Run migrations and start the dev server:

   ```powershell
   python manage.py migrate; python manage.py runserver
   ```

Frontend (React + Vite)

1. Change into the frontend folder and install dependencies:

   ```powershell
   cd frontend; npm install
   ```

2. Start the Vite dev server:

   ```powershell
   npm run dev
   ```

Notes

- The backend serves API endpoints (Django REST Framework). Configure `django-cors-headers` to allow requests from the Vite dev server (usually http://localhost:5173).
- For production, build the frontend (`npm run build`) and serve static files with Django or a CDN. Use `whitenoise` or a proper web server (Nginx + Gunicorn).
- Optional: add Dockerfiles for both backend and frontend for reproducible deployments.
