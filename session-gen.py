"""Simple python script to generate a session ID."""

from telethon import TelegramClient
from telethon.sessions import StringSession

API_KEY = int(input("Enter your API key: "))
API_HASH = input("Enter your API hash: ")

with TelegramClient(StringSession(), API_KEY, API_HASH) as client:

    print("Please check your saved messages for the string session.")
    session_string = client.session.save()
    reply_message = (
        f"Your session string is: `{session_string}`.\n"
        "Please save this string somewhere safe.\n"
        "Join support group for help and doubts - @blackbulls_support"
    )

    client.send_message("me", reply_message, parse_mode="markdown")