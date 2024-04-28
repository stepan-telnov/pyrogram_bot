import asyncio
from pyrogram import Client
from settings import API_ID, API_HASH, ME

async def main():
    async with Client("my_account", API_ID, API_HASH) as app:
        await app.send_message(ME, "аААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААА!")


asyncio.run(main())