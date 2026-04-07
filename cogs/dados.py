from discord.ext import commands
import random

class Dados6(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(help="Joga a quantidade de Dados que o usuario pedir")
    async def dados(self, ctx, quantidade: int):
        if quantidade < 1:
            await ctx.send("Vou jogar dados negativos? insere uma quantidade valida (1 ou mais).")
            return
        
        resultados = ""

        for i in range(quantidade):
            resultado = random.randint(1, 6)
            resultados += f"**Dado {i+1}:** {resultado}\n"

        await ctx.send(resultados)
        return
        

async def setup(bot):
    await bot.add_cog(Dados6(bot))
