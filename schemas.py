from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    phone: str
    role: str
    location: str

class ServiceCreate(BaseModel):
    category: str
    description: str
    user_id: int

class BookingCreate(BaseModel):
    client_id: int
    fundi_id: int
    service_id: int
    date: str
