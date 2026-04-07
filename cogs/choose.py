from discord.ext import commands
import random

class Escolha(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Escolhe uma opção aleatória entre as opções fornecidas. Exemplo: !escolha opção1 opção2 opção3")
    
    async def escolha(self, ctx, *options):
        if not options:
            await ctx.send("Me diz as opção, seu cabaço")
            return
        else:
            mychoice = random.choice(options)
            if "," in mychoice:
                mychoice = mychoice.replace(",", "")

            await ctx.send(f"Eu escolhi: {mychoice}")
            return


async def setup(bot):
    await bot.add_cog(Escolha(bot))
