from sqlalchemy.orm import Session
from models import User, Service, Booking
from schemas import UserCreate, ServiceCreate, BookingCreate

# -------- USER ----------
def create_user(db: Session, user: UserCreate):
    db_user = User(
        name=user.name,
        phone=user.phone,
        role=user.role,
        location=user.location
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_phone(db: Session, phone: str):
    return db.query(User).filter(User.phone == phone).first()

# -------- SERVICE ----------
def create_service(db: Session, service: ServiceCreate):
    db_service = Service(
        category=service.category,
        description=service.description,
        user_id=service.user_id
    )
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service

def search_services(db: Session, category: str, location: str):
    return db.query(Service).join(User).filter(
        Service.category.ilike(f"%{category}%"),
        User.location.ilike(f"%{location}%")
    ).all()

# -------- BOOKING ----------
def create_booking(db: Session, booking: BookingCreate):
    db_booking = Booking(
        client_id=booking.client_id,
        fundi_id=booking.fundi_id,
        service_id=booking.service_id,
        date=booking.date
    )
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

def get_booking_by_id(db: Session, booking_id: int):
    return db.query(Booking).filter(Booking.id == booking_id).first()

def update_payment_status(db: Session, booking_id: int, status: str):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if booking:
        booking.payment_status = status
        db.commit()
        db.refresh(booking)
    return booking
