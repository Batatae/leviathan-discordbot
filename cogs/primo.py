from discord.ext import commands

class Primo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(help="Checa se o número é primo ou não")
    
    async def primo(self, ctx, num: int):
        if num < 2: 
            await ctx.send(f"{num} não é primo.")
            return
        else:
            p = True
            for i in range(2, num):
                if num % i == 0:
                    p = False
                    break
            if p:
                await ctx.send(f"O numero {num} é primo.")
            else:
                await ctx.send(f"O numero {num} não é primo.")
            return



async def setup(bot):
    await bot.add_cog(Primo(bot))
