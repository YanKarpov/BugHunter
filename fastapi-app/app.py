from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from aiogram import Bot
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")  
bot = Bot(token=bot_token)

class Initiative(BaseModel):
    territory: str
    proposal: str

async def send_message(chat_id: int, text: str):
    await bot.send_message(chat_id=chat_id, text=text)

async def send_to_express_webhook(initiative: Initiative):
    webhook_url = "http://localhost:3000/webhook"  
    async with httpx.AsyncClient() as client:
        response = await client.post(webhook_url, json=initiative.dict())
        return response

@app.post("/webhook")
async def handle_webhook(request: Request):
    try:
        data = await request.json()
        
        if 'message' in data:
            chat_id = data['message']['chat']['id']
            text = data['message'].get('text', '')

            if text.startswith('/start'):
                response_text = "Добро пожаловать! Пожалуйста, введите ваше предложение по благоустройству."
            else:
                territory = "Некоторая территория" 
                proposal = text

                initiative = Initiative(territory=territory, proposal=proposal)
                
                await send_to_express_webhook(initiative)

                response_text = f"Ваше предложение: {proposal}"

            await send_message(chat_id, response_text)

        return JSONResponse(content={"status": "ok"}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

