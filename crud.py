from sqlalchemy.orm import Session
import models, schemas
from datetime import datetime

# ✅ Create a new user (client or fundi)
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# ✅ Get user by phone number
def get_user_by_phone(db: Session, phone: str):
    return db.query(models.User).filter(models.User.phone == phone).first()

# ✅ Search services by category and location
def search_services(db: Session, category: str, location: str):
    return db.query(models.Service).filter(
        models.Service.category.ilike(f"%{category}%"),
        models.Service.location.ilike(f"%{location}%")
    ).all()

# ✅ Create a booking
def create_booking(db: Session, booking: schemas.BookingCreate):
    db_booking = models.Booking(
        client_id=booking.client_id,
        service_id=booking.service_id,
        scheduled_date=booking.scheduled_date,
        status="pending"
    )
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

# ✅ Update payment status
def update_payment_status(db: Session, booking_id: int, status: str):
    booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    if not booking:
        return None

    # Update the booking's status
    booking.status = status
    db.commit()

    # Add a payment record
    payment = models.Payment(
        booking_id=booking_id,
        amount=booking.service.price,
        status=status,
        timestamp=datetime.utcnow()
    )
    db.add(payment)
    db.commit()
    db.refresh(payment)

    return payment

# ✅ Create a service
def create_service(db: Session, service: schemas.ServiceCreate):
    db_service = models.Service(**service.dict())
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service

# ✅ Get user by ID (used in service creation validation)
def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

