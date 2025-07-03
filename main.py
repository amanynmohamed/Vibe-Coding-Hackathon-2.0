from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from twilio.twiml.messaging_response import MessagingResponse
from urllib.parse import parse_qs

app = FastAPI()

@app.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    body_bytes = await request.body()
    parsed = parse_qs(body_bytes.decode())
    incoming_msg = parsed.get("Body", [""])[0].strip().lower()

    print(f"Incoming message: {incoming_msg}")  # For debugging

    response = MessagingResponse()

    if "hi" in incoming_msg:
        response.message("👋 Welcome to FundiLink!\nWhat service do you need? (e.g., plumber, electrician)")
    elif "plumber" in incoming_msg:
        response.message("🛠️ Found 2 plumbers:\n1. John (⭐ 4.5)\n2. Grace (⭐ 4.7)\nReply with 1 or 2 to book.")
    elif incoming_msg in ["1", "2"]:
        response.message("When do you need the service? (Today or Tomorrow?)")
    elif incoming_msg in ["today", "tomorrow"]:
        response.message("To confirm your booking, pay KES 500 via M-Pesa to Paybill 123456, Acc: FUNDILINK123.")
    else:
        response.message("Sorry, I didn’t understand that. Try typing: plumber, electrician, or hi.")

    return PlainTextResponse(str(response))
