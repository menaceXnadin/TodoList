# TodoList

A simple and modern Todo List web application built with **Django** and **PostgreSQL**.

## Features
- User registration and authentication
- Create, edit, complete, and delete tasks
- Each user has their own private task list
- Responsive and attractive UI using Tailwind CSS
- Task due dates and completion tracking

## Tech Stack
- **Backend:** Django (Python)
- **Database:** PostgreSQL
- **Frontend:** HTML, Tailwind CSS

## Setup Instructions

### Prerequisites
- Python 3.10+
- PostgreSQL
- Node.js and npm (for Tailwind CSS)

### Installation
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd TodoList
   ```
2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Install Node.js dependencies for Tailwind CSS:**
   ```bash
   cd theme/static_src
   npm install
   cd ../../..
   ```
5. **Configure your PostgreSQL database:**
   - Create a PostgreSQL database and user.
   - Update `DATABASES` in `TodoList/settings.py` with your credentials.
6. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```
7. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```
8. **Run the Tailwind CSS build:**
   ```bash
   cd theme/static_src
   npx tailwindcss -i ./src/styles.css -o ../static/css/styles.css --watch
   ```
9. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

## Usage
- Visit `http://127.0.0.1:8000/` in your browser.
- Register a new account and start managing your tasks!


