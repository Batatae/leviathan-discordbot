from discord.ext import commands

class Tabuada10(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(help="Envia a tabuada de um número específico. Exemplo: !tabuada 5")
    async def tabuada(self,ctx, a:int):
        if a<=0:
            await ctx.send("Insira um número positivo(maior que zero) seu burro")
            return
        else:
            resul = ""
            for i in range(1, 11):
                resul += f"{a} x {i} = {a*i}\n"
            await ctx.send(f"Tabuada do {a}:\n{resul}")
            return

async def setup(bot):
    await bot.add_cog(Tabuada10(bot))
