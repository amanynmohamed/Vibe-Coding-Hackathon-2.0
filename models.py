from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from database import Base
import enum
from datetime import datetime

# Enum for user role
class UserRole(str, enum.Enum):
    client = "client"
    fundi = "fundi"

# User table
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    phone = Column(String(20), unique=True, index=True)
    location = Column(String(100))
    role = Column(Enum(UserRole))

    # Relationships
    services = relationship("Service", back_populates="owner", cascade="all, delete")
    bookings = relationship("Booking", back_populates="client", foreign_keys='Booking.client_id')
    assignments = relationship("Booking", back_populates="fundi", foreign_keys='Booking.fundi_id')
    payments = relationship("Payment", back_populates="user")

# Service table
class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(100))
    description = Column(String(255))
    location = Column(String(100))
    user_id = Column(Integer, ForeignKey("users.id"))

    # Relationships
    owner = relationship("User", back_populates="services")

# Booking table
class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("users.id"))
    fundi_id = Column(Integer, ForeignKey("users.id"))
    service_id = Column(Integer, ForeignKey("services.id"))
    date = Column(DateTime, default=datetime.utcnow)
    status = Column(String(50), default="pending")

    # Relationships
    client = relationship("User", back_populates="bookings", foreign_keys=[client_id])
    fundi = relationship("User", back_populates="assignments", foreign_keys=[fundi_id])
    service = relationship("Service")
    payment = relationship("Payment", back_populates="booking", uselist=False)

# Payment table
class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    booking_id = Column(Integer, ForeignKey("bookings.id"))
    amount = Column(Integer)
    status = Column(String(50), default="unpaid")
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="payments")
    booking = relationship("Booking", back_populates="payment")
