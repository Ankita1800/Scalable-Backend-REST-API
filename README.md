Scalable Backend REST API
Overview

This project is a scalable backend REST API built using FastAPI and Python 3.10.
It demonstrates backend development fundamentals including API design, database integration, authentication basics, and error handling.
The project is designed to reflect real-world backend responsibilities expected from a Python Backend Intern.

Tech Stack

Python 3.10

FastAPI

PostgreSQL

SQLAlchemy ORM

JWT Authentication

Uvicorn

Postman (API testing)

Git & GitHub

Project Structure

backend-api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   ├── crud.py
│   ├── routers/
│   │   ├── users.py
│   │   └── tasks.py
│
├── screenshots/
│   └── postman_api_tests.png
│
├── requirements.txt
├── README.md

Features Implemented

Modular FastAPI application structure

RESTful API design following HTTP standards

User registration functionality

Task creation and management APIs

PostgreSQL database integration using SQLAlchemy ORM

Centralized database session handling

Password hashing using bcrypt

JWT token generation

Structured request and response validation using Pydantic

Error handling for invalid inputs and failed operations

API Endpoints
Authentication
Method	Endpoint	Description
POST	/users/register	Register a new user
Tasks
Method	Endpoint	Description
POST	/tasks	Create a new task
GET	/tasks	Retrieve all tasks (extendable)
Database Design

The project uses a relational database schema with the following entities:

User Table

id (Primary Key)

email (Unique)

hashed_password

Task Table

id (Primary Key)

title

completed

owner_id (Foreign Key referencing User)

SQLAlchemy ORM is used to define models and manage database interactions.

How to Run the Project Locally
Prerequisites

Python 3.10+

PostgreSQL installed and running

Virtual environment (recommended)

Installation Steps
git clone https://github.com/Ankita1800/Scalable-Backend-REST-API.git
cd Scalable-Backend-REST-API/backend-api
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

Database Configuration

Update the database connection string in app/database.py:

DATABASE_URL = "postgresql://username:password@localhost:5432/backend_db"


Create the database manually in PostgreSQL before running the application.

Run the Server
uvicorn app.main:app --reload


Open in browser:

http://127.0.0.1:8000/docs

Swagger UI is available for testing all endpoints interactively.


Testing

All APIs were tested using Swagger UI and Postman.

Request and response validation handled using Pydantic schemas.

Screenshots of successful API responses are included in the screenshots/ folder.

Debugging and Improvements

During development, common backend issues such as incorrect ORM queries, invalid request payloads, and response validation errors were identified and resolved.
Database queries were refactored to reduce redundancy and improve API response consistency.

Learning Outcomes

Built a production-style FastAPI backend with modular architecture

Gained hands-on experience with RESTful API development

Learned PostgreSQL integration using SQLAlchemy ORM

Implemented authentication fundamentals using JWT

Practiced debugging and backend issue resolution

Structured backend code for scalability and maintainability

Future Enhancements

JWT-protected routes

Role-based access control

Pagination and filtering for task APIs

Deployment on cloud platforms (Render / Railway)

Unit and integration testing

Author

Ankita Sahoo
GitHub: https://github.com/Ankita1800
