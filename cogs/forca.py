from discord.ext import commands
from extras.forca_palavras import palavras
import random

class Forca(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.word = None
        self.display = None
        self.letters = []
        
    @commands.command(help="Joguinho da forca. eu escolho uma palavra e você tem que adivinhar qual é. Mas tem umas Regrinhas: Você pode enviar uma letra ou a palavra inteira, se errar enviando a palavra inteira, perde. para iniciar o jogo, basta usar o comando nomal; para enviar uma letra ou palavra, use !forca <letra/palavra>")
    
    async def forca(self, ctx, *, msg=None):
        if self.word is None:
            self.word = random.choice(palavras)
            self.display = ["_"] * len(self.word)
            await ctx.send(f"Já escolhi uma palavra. Ela tem {len(self.word)} letras. Tente adivinhar!\n")
        if msg is None:
            await ctx.send("Manda assim: !forca <letra/palavra> ou '!forca parar' para desistir")
            return

        msg = msg.lower()

        if msg == "parar":
            await ctx.send(f"Jogo encerrado! A palavra era {self.word}.")
            self.word = None
            self.display = None
            self.letters = []
            return
            
        if msg == self.word:
            await ctx.send(f"🎉 Parabéns! Você acertou! A palavra era {self.word} mesmo!.")
            self.word = None
            self.display = None
            self.letters = []
            return
        
        elif msg in self.letters:
            await ctx.send(f"Ops, você já tentou a letra {msg}. Tente outra!\n\n `{' '.join(self.display)}`\nLetras já usadas: {', '.join(self.letters)}")
            return
        
        elif len(msg) == 1:
            if msg in self.word:
                for i, letra in enumerate(self.word):
                    if letra == msg:
                        self.display[i] = msg
                
                self.letters.append(msg)
                await ctx.send(f"Ohhh, tem a letra {msg} na palavra!\n\n `{' '.join(self.display)}`\nLetras já usadas: {', '.join(self.letters)}")
                

                if ''.join(self.display) == self.word:
                    await ctx.send(f"🎉 Parabéns! Você acertou! A palavra era {self.word}!.")
                    self.word = None
                    self.display = None
                    self.letters = []
                return
            else:
                
                self.letters.append(msg)
                await ctx.send(f"Ops, não tem a letra {msg} na palavra. Tente de novo!\n\n `{' '.join(self.display)}`\nLetras já usadas: {', '.join(self.letters)}")
                return
        
        else:
            await ctx.send(f"Ops, a palavra não é {msg}. Você perdeu!\n A palavra era: {self.word}.")
            self.word = None
            self.display = None
            self.letters = []
            return


async def setup(bot):
    await bot.add_cog(Forca(bot))
