import discord
import app.responses as responses
import os
from dotenv import load_dotenv

load_dotenv()

async def send_message(message, user_message, is_private):
    try:
        # response we return to the user
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

def run_bot():
    token = os.getenv('TOKEN')
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is online!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return # prevents having endless loops? still don't know how this works

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' in the '{channel}' Channel.")

        if user_message[0] == "?":
            # gets rid of the question mark and processes the rest of the message
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)



    client.run(token)