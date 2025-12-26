from sqlalchemy.orm import Session
from . import models, auth

def create_user(db: Session, email: str, password: str):
    user = models.User(
        email=email,
        hashed_password=auth.hash_password(password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_task(db: Session, title: str, user_id: int):
    task = models.Task(title=title, owner_id=user_id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task
