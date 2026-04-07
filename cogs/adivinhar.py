from discord.ext import commands
import random
import string

class Adivinhar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.numero = None
        self.chances = 3
        

    @commands.command(help="Eu escolho um número entre 1 e 10 e você tem três chanches para adivinhar.")
    async def adivinhar(self, ctx, n: int = None):

        if self.numero is None:
            self.numero = random.randint(1, 10)
            await ctx.send("Já esccolhi um número entre 1 e 10. Tente adivinhar!")

        if n is None:
            await ctx.send("Manda assim: !adivinhar <numero>")
            return
        
        if n < 1 or n > 10:
            await ctx.send("O número deve ser entre 1 e 10. Vai de novo!")
            return

        if n == self.numero:
            await ctx.send("🎉 Parabéns! Você acertou!")
            self.numero = None
            self.chances = 3

        elif n < self.numero:
            await ctx.send("O número é **maior**.")
            self.chances -= 1
        else:
            await ctx.send("O número é **menor**.")
            self.chances -= 1

        if self.chances == 0:
            await ctx.send(f"Suas chances acabaram! O número era {self.numero}.")
            self.numero = None
            self.chances = 3

async def setup(bot):
    await bot.add_cog(Adivinhar(bot))