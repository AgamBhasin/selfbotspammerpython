import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print("I'm ready daddy")

@client.event
async def on_message(message):
    if message.content == "spam":
        while 1==1:
            await client.send_message(message.channel, "spam")

client.run("MTg4OTkzMDQ2MzYzMzczNTY4.DGlrCA.0-Q_aish_Rqj67G5IVhyQOvFlTw",bot=False)
