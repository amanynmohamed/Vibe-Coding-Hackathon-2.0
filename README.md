# 🛠️ FundiLink - WhatsApp-Based Freelancer Booking System

FundiLink is a backend service that connects clients with local fundis (freelancers like plumbers or electricians) through a WhatsApp chatbot. Built using **FastAPI**, **SQLAlchemy**, and **Twilio**, it offers users a seamless way to register, search for services, make bookings, and confirm payments — all via WhatsApp.

---

## 🚀 Features

- 📱 WhatsApp chatbot for real-time interaction
- ✅ Register clients and fundis
- 🔎 Search services by category and location
- 📆 Book a service
- 💳 Confirm booking payment
- 💬 Chatbot powered by Twilio

---

## 📸 Demo

Below is a sample conversation between a user and the FundiLink bot on WhatsApp:

![FundiLink WhatsApp Demo](./7bc5f59a-4980-468e-949e-2042c2c32fd3.png)

---

## 🧰 Tech Stack

- **Python 3.10+**
- **FastAPI**
- **SQLAlchemy**
- **Twilio WhatsApp API**
- **SQLite** (or any SQL DB)
- **Uvicorn**
- **ngrok** (for public webhook testing)

---

## 📂 Project Structure

```text
FundiLink/
├── main.py             # FastAPI app and routes
├── crud.py             # Business logic
├── models.py           # SQLAlchemy models
├── schemas.py          # Pydantic schemas
├── database.py         # Database connection
├── requirements.txt    # Installed dependencies
├── README.md           # Project documentation
└── screenshot.png      # WhatsApp bot chat image

---

## **👥 Contributors**

<table>
  <tr>
    <td align="center" width="25%">
      <a href="https://github.com/amanynabil" target="_blank">
        <img src="https://avatars.githubusercontent.com/u/0?v=4" width="100px;" alt="Amany Nabil Ahmed"/>
        <br /><b>Amany Nabil Ahmed</b>
      </a>
    </td>
    <td align="center" width="25%">
      <a href="https://github.com/nakhanu" target="_blank">
        <img src="https://avatars.githubusercontent.com/u/131362156?v=4" width="100px;" alt="Sophia Nakhanu"/>
        <br /><b>Sophia Nakhanu</b>
      </a>
    </td>
    <td align="center" width="25%">
      <a href="https://github.com/RICCOM" target="_blank">
        <img src="https://avatars.githubusercontent.com/u/0?v=4" width="100px;" alt="Eric Munjuri"/>
        <br /><b>Eric Munjuri</b>
      </a>
    </td>
    <td align="center" width="25%">
      <a href="https://github.com/steviedave" target="_blank">
        <img src="https://avatars.githubusercontent.com/u/0?v=4" width="100px;" alt="Stephen David Oduor"/>
        <br /><b>Stephen David Oduor</b>
      </a>
    </td>
  </tr>
</table>


## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/amanynmohamed/Vibe-Coding-Hackathon-2.0.git
cd Vibe-Coding-Hackathon-2.0

---
