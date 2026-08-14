# MyBlog

A simple blog/CMS built with Django and PostgreSQL as part of a structured Django learning plan. This is Project 1 of 2 — the fundamentals project focused on the full CRUD + auth loop.

> **Status:** Work in progress (Week 2 of 4 for this project). Authentication is not yet implemented — posts are currently assigned to a placeholder user. See [What's Next](#whats-next) below.

## Features

- Create, read, update, and delete blog posts
- Categorize posts (with graceful handling for posts with no category)
- Django admin panel for managing posts and categories
- Styled post list and detail views with category badges
- PostgreSQL database (via `python-decouple` for secure credential management)

## Tech Stack

- **Backend:** Django
- **Database:** PostgreSQL
- **Config/secrets:** `python-decouple` + `.env`
- **Frontend:** Django templates, vanilla CSS

## Setup — Run Locally

**Prerequisites:** Python installed, PostgreSQL installed and running locally.

1. **Clone the repository**

   ```
   git clone <your-repo-url>
   cd myblog
   ```

2. **Create and activate a virtual environment**

   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**

   ```
   pip install -r requirements.txt
   ```

4. **Set up the database**
   - Create a PostgreSQL database named `myblog_db`
   - Create a `.env` file in the project root (same level as `manage.py`) with:
     ```
     DB_NAME=myblog_db
     DB_USER=your_postgres_username
     DB_PASSWORD=your_postgres_password
     DB_HOST=localhost
     DB_PORT=5432
     ```

5. **Run migrations**

   ```
   python manage.py migrate
   ```

6. **Create a superuser** (to access the admin panel)

   ```
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000/` in your browser. Admin panel is at `/admin/`.

## Project Structure

```
myblog/
├── manage.py
├── requirements.txt
├── .env                # not committed — see .gitignore
├── myblog/              # project settings
└── blog/                 # main app (models, views, templates)
```

## What's Next

- [ ] User authentication (signup, login, logout)
- [ ] Restrict post editing to the post's author
- [ ] Comments (many-to-one relationship with Post and User)
- [ ] "My posts" dashboard
- [ ] Deployment (Railway/Render/Fly.io)
- [ ] Tests

## Learning Context

Built as Project 1 of an 8-week Django + PostgreSQL learn-by-doing plan, focused on mastering the core CRUD + auth loop before moving on to a more complex second project (relational data modeling, class-based views, DRF API layer).
