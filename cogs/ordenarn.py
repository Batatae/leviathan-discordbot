from discord.ext import commands
import string

class OrdenarNumeros(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(help="Ordena uma lista de números em ordem crescente ou decrescente. Exemplo: !ordenarn 5 3 8 1 c -> ordena em ordem crescente, !ordenarn 5 3 8 1 d -> ordena em ordem decrescente")
    
    async def ordenarn(self, ctx, *msg):
        if not msg:
            await ctx.send("Ordenar oq fi?")
            return
        elif msg[-1].lower() not in ['c', 'd'] and msg[-1].lower() not in string.digits:
            await ctx.send("A ordem tem que ser 'c' para crescente ou 'd' para decrescente. Se você não mandar a ordem vai ser crescente por padrão.")
            return
        else:
            if msg[-1].lower() in ['c', 'd']:
                ordem = msg[-1].lower()
                n = msg[:-1]
            else:
                ordem = 'c'
                n = msg

            try:
                n = [float(x) for x in n]
            except ValueError:
                await ctx.send("Tem letra no meio dos números.")
                return

            result = []
            while len(n) > 0:
                if result == []:
                    result.append(n[0])
                    n.pop(0)
                else: 
                    if n[0] <= result[0]:
                        result.insert(0, n[0])
                        n.pop(0)
                    elif n[0] >= result[-1]:
                        result.append(n[0])
                        n.pop(0)
                    else:
                        for i in range(len(result)):
                            if n[0] <= result[i]:
                                result.insert(i, n[0])
                                n.pop(0)
                                break
            
            if ordem == 'd':
                result.reverse()
            
            await ctx.send(f"Lista ordenada:\n {', '.join(map(str, result))}")
            return
        

async def setup(bot):
    await bot.add_cog(OrdenarNumeros(bot))
