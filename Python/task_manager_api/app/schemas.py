from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class TaskCreate(BaseModel):
    title: str
    description: str
    status: str
    user_id: int
