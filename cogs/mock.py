from discord.ext import commands

class Mock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(help="Alterna entre letras maisculas e minusculas da mensagem recebida. exemplo: Mensagem -> mEnSaGeM")

    async def mock(self, ctx, *, mensagem: str):
        resultado = ""

        for i, letra in enumerate(mensagem):
            if i % 2 == 0:
                resultado += letra.lower()
            else:
                resultado += letra.upper()

        await ctx.send(resultado)
        return
            

async def setup(bot):
    await bot.add_cog(Mock(bot))
