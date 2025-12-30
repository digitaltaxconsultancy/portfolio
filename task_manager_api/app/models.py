from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    description = Column(Text)
    status = Column(String(50))
    user_id = Column(Integer, ForeignKey("users.id"))
