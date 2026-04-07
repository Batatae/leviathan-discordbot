from discord.ext import commands

class Embaralhar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(help="Embaralha as opções dadas.")
    async def embaralhar(self, ctx, *msg):
        if not msg:
            await ctx.send("Embaralhar oq fi?")
            return
        else:
            import random
            msg = list(msg)
            res = []
            while len(res) < len(msg):
                n = random.choice(msg)
                res.append(n)
                msg.remove(n)
            await ctx.send(f"Opções embaralhadas:\n {', '.join(res)}")
            return

async def setup(bot):
    await bot.add_cog(Embaralhar(bot))
