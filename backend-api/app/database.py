from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite for local development (change to PostgreSQL for production)
DATABASE_URL = "sqlite:///./backend_db.db"
# For PostgreSQL: DATABASE_URL = "postgresql://postgres:password@localhost:5432/backend_db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
