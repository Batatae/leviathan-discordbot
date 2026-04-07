from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(help="Você fala Ping eu respondo Pong! :D (testa o delay tlgd?)")
    async def ping(self, ctx):
        await ctx.send("Pong!")
        return

async def setup(bot):
    await bot.add_cog(Ping(bot))
