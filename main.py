import asyncio
from pyrogram import Client
from settings import API_ID, API_HASH, ME

from pyrogram import Client, filters


app = Client('my_account', api_id=API_ID, api_hash=API_HASH)

@app.on_message(filters.command("", prefixes=".") & filters.private)
async def message_to_user(client, message):
    if ME != message.from_user.id:
        print(message)
        print(message.text[2:])
        if "hello" in message.text:
            await message.reply_text("help")


def main() -> None:
    try:
        app.run()
    except Exception as err:
        print(err)


if __name__ == '__main__':
    main()
