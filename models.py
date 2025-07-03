from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String, unique=True)
    role = Column(String)  # 'client' or 'fundi'
    location = Column(String)

class Service(Base):
    __tablename__ = "services"
    id = Column(Integer, primary_key=True)
    category = Column(String)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("users.id"))
    fundi_id = Column(Integer, ForeignKey("users.id"))
    service_id = Column(Integer, ForeignKey("services.id"))
    date = Column(String)
    status = Column(String, default="pending")  # pending, confirmed, completed
    payment_status = Column(String, default="unpaid")
