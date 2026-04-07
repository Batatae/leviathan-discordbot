from discord.ext import commands

class Anagrama(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(help="Checa se as palavras são um anagrama ou não. Exemplo: !anagrama palavra1 palavra2")
    
    async def anagrama(self,ctx, p1: str, p2:str):
        if len(p1) != len(p2):
            await ctx.send(f"{p1} e {p2} não são anagramas.")
            return
        
        else: 
            a = True
            p1.lower()
            p2.lower()
            for i in p1:
                if i in p2:
                    p1.pop(p1.index(i))
                    p2.pop(p2.index(i))
                else:
                    a = False
                    break
            if a: 
                await ctx.send(f"{p1} e {p2} são anagramas.")
            else:
                await ctx.send(f"{p1} e {p2} não são anagramas.")
            return
            
async def setup(bot):
    await bot.add_cog(Anagrama(bot))
