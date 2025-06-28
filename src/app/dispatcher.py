from src.infrastructure.telegram.telegram_api import send_message
from src.models.telegram_request import TelegramRequest
from loguru import logger


async def telegram_dispatcher(telegram_request: TelegramRequest) -> None:
    """
    Dispatcher for handling Telegram requests.
        :param telegram_request: TelegramRequest
        :return: None
    """
    if telegram_request.message.text == "/start":
        logger.info(f"Received /start command from user {telegram_request.message.from_.id}")
        await send_message(
            chat_id=telegram_request.message.chat.id,
            text="Welcome to the bot! How can I assist you today?",
            reply_to_message_id=telegram_request.message.message_id,
        )
        return

    # Handle other commands or messages
    logger.info(f"Received message from user {telegram_request.message.from_.id}: {telegram_request.message.text}")
    await send_message(
        chat_id=telegram_request.message.chat.id,
        text=f"I received your message.\nBut I don't know how to respond yet.",
        reply_to_message_id=telegram_request.message.message_id,
    )
    return
