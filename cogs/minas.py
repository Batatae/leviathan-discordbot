from discord.ext import commands
import random

class minado(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bombas = []
        self.stts = False
        
    @commands.command(help="Joguinho simples, o bot criara um pequeno campo minado,  e voce tera de escolher numeros até que não sobre mas nenhum. porém, se você escolher um número que possua uma mina, o jogo acaba e você perde. Para jogar, use !mine <dificuldade (facil, medio, dificil)>. a dificuldade varia conforme a quantidade de bombas, de 1 a 3. Após o inicio, use !mine <numero> para escolher um numero. O campo minado tem numeros de 1 a 9. Use !mine <parar> para desistir do jogo.")
    
    async def mina(self, ctx, msg: str):
        row1 = [1, 2, 3]
        row2 = [4, 5, 6]
        row3 = [7, 8, 9]
        numbers = row1 + row2 + row3
        message = f"{row1}\n{row2}\n{row3}"
        if self.stts == False:
            msg = msg[0].lower()
            if msg not in ["facil", "medio", "dificil"]:
                await ctx.send("Escolha uma dificuldade válida: facil, medio ou dificil.")
                return
            elif msg == "facil":
                dif = "Fácil"
                self.bombas = [random.randint(1, 9)]
            elif msg == "medio":
                dif = "Médio"
                self.bombas = [random.randint(1, 9), random.randint(1, 9)]
            elif msg == "dificil":
                dif = "Difícil"
                self.bombas = [random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)]

            await ctx.send(f"Jogo iniciado na dificuldade {dif}. Use !mine <números> para continuar.\n \n{message}")
            self.stts = True
            return
        elif msg.lower() == "parar":
            await ctx.send("Partida Encerrada.🕊️")
            self.bombas = []
            self.stts = False
            return
        else:
            try:
                n = int(msg)
            except ValueError:
                await ctx.send("Escolha um NÚMERO válido de 1 a 9.")
                return
            
            if n < 1 or n > 9:
                await ctx.send("Escolha um número válido de 1 a 9.")
                return
            
            if n in self.bombas:
                await ctx.send(f"💣💣💣💣 BOOOOOOMMMM!!!!\nVocê pisou numa bomba e teve seu corpo explodido em pedacinhos~~\nPerdeu!")
                self.bombas = []
                self.stts = False
                return
            else:
                if n in row1:
                    row1[row1.index(n)] = "X"
                elif n in row2:
                    row2[row2.index(n)] = "X"
                elif n in row3:
                    row3[row3.index(n)] = "X"

                elif (n not in numbers) and (numbers.sort() == self.bombas.sort()):
                    await ctx.send(f"Você Conseguiu, desarmou todas as bombas e ganhou!🎉")
                    self.bombas = []
                    self.stts = False
                    return

                elif n not in numbers:
                    await ctx.send("Número já escolhido ou inválido. Tente outro número.")
                    return
                
                else:
                    await ctx.send(f"Hm! O número {n} é seguro. Continue escolhendo!\n \n{message}")
                    return


async def setup(bot):
    await bot.add_cog(minado(bot))
