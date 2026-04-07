from discord.ext import commands

class Reverter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(help="Manda a Mensagem enviada ao contrário! Exemplo: !reverse Olá Mundo = odnuM álO")
    async def reverse(self, ctx, *, message):
        reversed_message = message[::-1]
        await ctx.send(reversed_message)
        return

async def setup(bot):
    await bot.add_cog(Reverter(bot))
