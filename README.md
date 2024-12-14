# Routine App

**Routine** is a web application that helps users track their daily routines, create to-do lists, and set goals. It’s designed to empower users to build better habits and stay organized.

---

## Features
- **To-Do Lists**: Manage tasks and deadlines efficiently.
- **Goal Setting**: Set personal goals.
- **Simple Design**: A clean and user-friendly interface for easy navigation.

---

## Technologies Used

- **Backend**: Django Framework
- **Frontend**: Django(Template Engine), HTML, CSS (Tailwind CSS)
- **Database**: SQLite

---

## Requirements

To run this app locally, you'll need the following installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install)
- A text editor or IDE (e.g., VS Code, PyCharm)

---

## Setting Up the Development Server

### Step 1: Clone the Repository

Start by cloning the repository:

```bash
git clone https://github.com/yourusername/routine.git
cd routine
```
### Step 2: Install Dependencies
Create a `.env` file to store the enviroment variable.
```.env
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=127.0.0.1,localhost
```
### Step 3: Build the Docker Container
Build the Docker image for the app:
```bash
docker-compose build
```

### Step 4: Run the Application
Start the app using Docker Compose:
```bash
docker-compose up
```
### Step 5: Apply Database Migrations
After the container is running, apply the migrations to set up the database schema:
```bash
docker exec -it routine_app_container python manage.py migrate
```

### Step 6: Access the Application
Visit the app in your browser at http://localhost:8000

