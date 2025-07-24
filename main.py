import discord
import os
intents = discord.Intents.default()
intents.message_content = True
token = os.getenv("BOT_TOKEN")
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"we have logged in as {client.user}")

client.run(token)

