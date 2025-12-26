from fastapi import FastAPI
from .database import Base, engine
from .routers import users, tasks

# Create database tables
try:
    Base.metadata.create_all(bind=engine)
except Exception as e:
    print(f"Warning: Could not initialize database: {e}")

app = FastAPI(title="Scalable Backend REST API")

app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"status": "API running"}
