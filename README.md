# Scalable Backend REST API

## Description
A backend REST API built using FastAPI and Python 3.10.  
The project demonstrates core backend development concepts such as RESTful API design, database integration, authentication basics, and error handling.

---

## Tech Stack
- Python 3.10
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- JWT Authentication
- Uvicorn

---

## Project Structure
backend-api/
├── app/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│ ├── auth.py
│ ├── crud.py
│ └── routers/
│ ├── users.py
│ └── tasks.py
├── screenshots/
├── requirements.txt
└── README.md

---

## Features
- Modular FastAPI application structure
- RESTful API development
- User registration functionality
- Task creation and management APIs
- PostgreSQL integration using SQLAlchemy ORM
- Request and response validation using Pydantic
- Password hashing and JWT token generation
- Centralized database session handling
- Error handling for invalid requests

---

## API Endpoints

### User
- `POST /users/register` – Register a new user

### Tasks
- `POST /tasks` – Create a task
- `GET /tasks` – Fetch tasks (extendable)

---

## Database Schema

### User
- id
- email
- hashed_password

### Task
- id
- title
- completed
- owner_id

---

## How to Run

### 1. Clone the Repository

git clone https://github.com/Ankita1800/Scalable-Backend-REST-API.git
cd Scalable-Backend-REST-API/backend-api

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Configure Database
Update DATABASE_URL in app/database.py with your PostgreSQL credentials.

### 4. Run the Server
uvicorn app.main:app --reload

### Access API documentation at:
http://127.0.0.1:8000/docs

### Testing
APIs tested using Swagger UI and Postman
Screenshots of API responses are stored in the screenshots directory

### Future Improvements
JWT-protected routes
Update and delete task APIs
Pagination and filtering
Cloud deployment

### Author
### Ankita Sahoo
GitHub: https://github.com/Ankita1800
