from discord.ext import commands
import random

class Coin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(help="Gira uma moeda, Vai cair Cara ou Coroa")
    async def coin(self, ctx):
        coin = random.choice(["Cara", "Coroa"])
        await ctx.send(f"Caiu {coin}!")
        return


async def setup(bot):
    await bot.add_cog(Coin(bot))
