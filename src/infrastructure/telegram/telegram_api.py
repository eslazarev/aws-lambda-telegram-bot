import httpx

from src.settings import TELEGRAM_API_URL


async def send_message(
    chat_id: int,
    text: str,
    reply_to_message_id: int | None = None,
) -> None:

    payload = {
        "chat_id": chat_id,
        "text": text,
    }

    if reply_to_message_id is not None:
        payload["reply_to_message_id"] = reply_to_message_id

    async with httpx.AsyncClient() as client:
        await client.post(f"{TELEGRAM_API_URL}/sendMessage", json=payload)
