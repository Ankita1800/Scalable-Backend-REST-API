# Scalable Backend REST API

A scalable REST API built with FastAPI, featuring user authentication, task management, and SQLAlchemy ORM.

## Features

- 🔐 User Authentication (JWT-based)
- 👥 User Management
- ✅ Task Management (CRUD operations)
- 🗄️ SQLAlchemy ORM with SQLite (easily switchable to PostgreSQL/MySQL)
- 📝 API Documentation (Swagger UI & ReDoc)
- 🔒 Password Hashing with bcrypt
- 🎯 RESTful API design

## Project Structure

```
backend-api/
│
├── app/
│   ├── main.py           # FastAPI application entry point
│   ├── database.py       # Database configuration
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas
│   ├── auth.py           # Authentication utilities
│   ├── crud.py           # CRUD operations
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── users.py      # User endpoints
│   │   └── tasks.py      # Task endpoints
│
├── screenshots/          # Postman screenshots
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd backend-api
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows:
  ```bash
  venv\Scripts\activate
  ```
- Linux/Mac:
  ```bash
  source venv/bin/activate
  ```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at: `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### Users
- `POST /users/register` - Register a new user
- `POST /users/login` - Login and get access token
- `GET /users/me` - Get current user info
- `GET /users/` - List all users
- `GET /users/{user_id}` - Get user by ID

### Tasks
- `POST /tasks/` - Create a new task
- `GET /tasks/` - Get all tasks for current user
- `GET /tasks/{task_id}` - Get task by ID
- `PUT /tasks/{task_id}` - Update a task
- `DELETE /tasks/{task_id}` - Delete a task

## Authentication

The API uses JWT (JSON Web Tokens) for authentication. To access protected endpoints:

1. Register a new user at `/users/register`
2. Login at `/users/login` to get an access token
3. Include the token in the Authorization header:
   ```
   Authorization: Bearer <your-access-token>
   ```

## Database

By default, the application uses SQLite. To switch to PostgreSQL or MySQL, update the `SQLALCHEMY_DATABASE_URL` in [app/database.py](app/database.py).

Example for PostgreSQL:
```python
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"
```

## Security Notes

⚠️ **Important**: Before deploying to production:
- Change the `SECRET_KEY` in [app/auth.py](app/auth.py)
- Use environment variables for sensitive data
- Enable HTTPS
- Configure CORS properly
- Use a production-grade database (PostgreSQL, MySQL)

## Development

To add new features:
1. Create models in [app/models.py](app/models.py)
2. Define schemas in [app/schemas.py](app/schemas.py)
3. Add CRUD operations in [app/crud.py](app/crud.py)
4. Create router endpoints in [app/routers/](app/routers/)
5. Register router in [app/main.py](app/main.py)

## License

MIT License
