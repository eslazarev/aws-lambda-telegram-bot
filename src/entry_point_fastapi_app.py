from fastapi import FastAPI

from mangum import Mangum
from src.app.dispatcher import telegram_dispatcher

from src.models.telegram_request import TelegramRequest
from loguru import logger


app = FastAPI()


@app.post("/")
async def telegram_webhook(request: TelegramRequest):

    logger.info(f"Telegram webhook request: {request}")

    await telegram_dispatcher(request)

    logger.info("Telegram webhook request processed successfully")

    return {"ok": True}


handler = Mangum(app)
