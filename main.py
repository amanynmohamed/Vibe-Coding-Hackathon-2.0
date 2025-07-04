from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import Response
from sqlalchemy.orm import Session
from twilio.twiml.messaging_response import MessagingResponse

import models, crud, schemas
from database import SessionLocal, engine

from models import Base
Base.metadata.create_all(bind=engine)

# ✅ Create FastAPI app BEFORE using it
app = FastAPI()

# ✅ Create database tables
models.Base.metadata.create_all(bind=engine)

# ✅ Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ WhatsApp webhook endpoint
@app.post("/whatsapp")
async def whatsapp_webhook(request: Request):

    form = await request.form()
    incoming_msg = form.get("Body", "").strip().lower()

    # Respond with a welcome message
    resp = MessagingResponse()
    msg = resp.message()

    if "hi" in incoming_msg or "hello" in incoming_msg:
        msg.body("👋 Welcome to FundiLink!\nWhat service do you need? (e.g., plumber, electrician)")
    else:
        msg.body("🤖 Sorry, I didn’t understand that. Please type 'hi' to get started.")

    return Response(content=str(resp), media_type="application/xml")

# ✅ Register user (client or fundi)
@app.post("/register")
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = crud.get_user_by_phone(db, user.phone)
    if existing_user:
        raise HTTPException(status_code=400, detail="Phone number already registered.")
    return crud.create_user(db, user)

# ✅ Create a service (for fundis)
@app.post("/services")
def create_service(service: schemas.ServiceCreate, db: Session = Depends(get_db)):
    # Optional: check if provider exists and is a fundi
    provider = crud.get_user_by_id(db, service.provider_id)
    if not provider or provider.role != "fundi":
        raise HTTPException(status_code=400, detail="Invalid provider ID or user is not a fundi.")
    
    return crud.create_service(db, service)


# ✅ Search for services by category and location
@app.get("/services/search")
def search_services(category: str, location: str, db: Session = Depends(get_db)):
    services = crud.search_services(db, category, location)
    if not services:
        raise HTTPException(status_code=404, detail="No services found.")
    return services

# ✅ Create a booking
@app.post("/book")
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    return crud.create_booking(db, booking)

# ✅ Confirm payment
@app.put("/confirm_payment/{booking_id}")
def confirm_payment(booking_id: int, db: Session = Depends(get_db)):
    updated = crud.update_payment_status(db, booking_id, "paid")
    if not updated:
        raise HTTPException(status_code=404, detail="Booking not found.")
    return {"message": "Payment confirmed", "booking_id": booking_id}
