from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

# ✅ User schema (used for creation)
class UserCreate(BaseModel):
    name: str
    phone: str
    role: str  # "client" or "fundi"

# ✅ User response schema (optional, if needed)
class User(BaseModel):
    id: int
    name: str
    phone: str
    role: str

    class Config:
        orm_mode = True


# ✅ Service schema
class ServiceCreate(BaseModel):
    title: str
    description: str
    category: str
    location: str
    price: float
    provider_id: int  # Foreign key to User (fundi)

class Service(BaseModel):
    id: int
    title: str
    description: str
    category: str
    location: str
    price: float
    provider_id: int

    class Config:
        orm_mode = True


# ✅ Booking schema
class BookingCreate(BaseModel):
    client_id: int
    service_id: int
    scheduled_date: date

class Booking(BaseModel):
    id: int
    client_id: int
    service_id: int
    scheduled_date: date
    status: str

    class Config:
        orm_mode = True


# ✅ Payment schema
class Payment(BaseModel):
    id: int
    booking_id: int
    amount: float
    status: str
    timestamp: datetime

    class Config:
        orm_mode = True
