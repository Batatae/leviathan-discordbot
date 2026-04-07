import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot ligado como {bot.user}')

async def main():
    for arquivo in os.listdir("cogs"):
        if arquivo.endswith(".py") and arquivo != "__init__.py":
            await bot.load_extension(f"cogs.{arquivo[:-3]}")

    await bot.start(TOKEN)


import asyncio
asyncio.run(main())

