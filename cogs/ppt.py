from discord.ext import commands
import random

class ppt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(help="Classico pedra, papel e tesoura. Para jogar, use !ppt <pedra/papel/tesoura>")
    
    async def ppt(self, ctx, msg=None):
        if msg is None:
            await ctx.send("Escolha pedra, papel ou tesoura para jogar!")
            return
        
        choices = ["pedra", "papel", "tesoura"]
        msg = msg.lower()
        wins = {
            "pedra": "tesoura",
            "papel": "pedra",
            "tesoura": "papel"
        }

        if msg not in choices:
            await ctx.send("Escolha pedra, papel ou tesoura!")
            return

        else:
            mychoice = random.choice(choices)

            if msg == mychoice:
                await ctx.send(f"Eu escolhi {mychoice}.\nEmpatamos.")
                return
            elif msg == wins[mychoice]:
                await ctx.send(f"Eu escolhi {mychoice}.\nVocê ganhou, mortal.")
                return
            else:
                await ctx.send(f"Eu escolhi {mychoice}.\nVocê perdeu.")
                return

async def setup(bot):
    await bot.add_cog(ppt(bot))
