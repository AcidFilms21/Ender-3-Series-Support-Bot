import discord

from discord.ext import commands
from global_functions import (
      TOKEN,
)

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def cogtest(self, ctx):
        await ctx.send("cog test complete")
        
async def setup(client):
    await client.add_cog(Utilities(client))