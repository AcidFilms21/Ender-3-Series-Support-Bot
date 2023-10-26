import discord
import os
import asyncio

from global_functions import (
      PREFIX,
      TOKEN,
)
from discord.ext import commands
from discord.ext import tasks

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(intents=intents,command_prefix=PREFIX, case_insensitive=True)
client.remove_command("help")

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.change_presence(activity=discord.Game(name='3D Printing!'))
    
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

@client.command()
async def check_cogs(ctx, cog_name):
    try:
        await client.load_extension(f"cogs.{cog_name}")
    except commands.ExtensionAlreadyLoaded:
        await ctx.send("Cog is loaded")
    except commands.ExtensionNotFound:
        await ctx.send("Cog not found")
    else:
        await ctx.send("Cog is unloaded")
        await client.unload_extension(f"cogs.{cog_name}")

@client.command()
async def load_cogs(ctx, cog_name):
    await client.load_extension(f"cogs.{cog_name}")

@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! 🏓  | {round(client.latency * 1000)}ms')
      
async def main():
    async with client:
        await load_extensions()
        await client.start(TOKEN)

asyncio.run(main())