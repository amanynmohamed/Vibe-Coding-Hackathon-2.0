from dotenv import load_dotenv
load_dotenv()

import httpx, base64, datetime, os
from fastapi import APIRouter, HTTPException
from dotenv import load_dotenv

from config import MPESA_CONSUMER_KEY, MPESA_CALLBACK_URL

print("Your M-Pesa Key is:", MPESA_CONSUMER_KEY)

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class STKPushRequest(BaseModel):
    phone_number: str
    amount: int

@router.post("/stk_push")
def initiate_stk_push(payload: STKPushRequest):
    # Your Daraja logic goes here
    return {"message": "STK push initiated", "phone_number": payload.phone_number, "amount": payload.amount}


load_dotenv()
router = APIRouter()
import os
import base64
import datetime
import httpx
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

class STKPushRequest(BaseModel):
    phone_number: str
    amount: int

# 🔐 Function to get access token
async def get_access_token():
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    auth = (os.getenv("MPESA_CONSUMER_KEY"), os.getenv("MPESA_CONSUMER_SECRET"))
    async with httpx.AsyncClient() as client:
        response = await client.get(url, auth=auth)
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to get access token")
        return response.json()["access_token"]

# 📲 STK Push endpoint
@router.post("/stk_push")
async def initiate_stk_push(payload: STKPushRequest):
    token = await get_access_token()
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    password = base64.b64encode(
        f"{os.getenv('MPESA_SHORTCODE')}{os.getenv('MPESA_PASSKEY')}{timestamp}".encode()
    ).decode()

    headers = {"Authorization": f"Bearer {token}"}
    payload_data = {
        "BusinessShortCode": os.getenv("MPESA_SHORTCODE"),
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": payload.amount,
        "PartyA": payload.phone_number,
        "PartyB": os.getenv("MPESA_SHORTCODE"),
        "PhoneNumber": payload.phone_number,
        "CallBackURL": os.getenv("MPESA_CALLBACK_URL"),
        "AccountReference": "FundiLink",
        "TransactionDesc": "Fundi Booking Payment"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest",
            headers=headers,
            json=payload_data
        )
        return response.json()

# Get access token
async def get_access_token():
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    auth = (os.getenv("MPESA_CONSUMER_KEY"), os.getenv("MPESA_CONSUMER_SECRET"))
    async with httpx.AsyncClient() as client:
        response = await client.get(url, auth=auth)
        return response.json()['access_token']

# STK Push Endpoint
@router.post("/pay")
async def initiate_stk_push(phone: str, amount: int):
    token = await get_access_token()
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    password = base64.b64encode(
        f"{os.getenv('MPESA_SHORTCODE')}{os.getenv('MPESA_PASSKEY')}{timestamp}".encode()
    ).decode()

    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "BusinessShortCode": os.getenv("MPESA_SHORTCODE"),
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone,
        "PartyB": os.getenv("MPESA_SHORTCODE"),
        "PhoneNumber": phone,
        "CallBackURL": os.getenv("MPESA_CALLBACK_URL"),
        "AccountReference": "FundiLink",
        "TransactionDesc": "Fundi Booking Payment"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest",
            headers=headers, json=payload
        )
        return response.json()
