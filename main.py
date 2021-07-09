import discord
import os

client = discord.Client();

@client.event
async def on_ready():
    print("Succesfully logged in!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$test"):
        await message.channel.send("Hello world!")



client.run(os.getenv("BOT_TOKEN"))
