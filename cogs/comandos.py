from discord.ext import commands
import random

class CommandsList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command()
    async def comandos(self, ctx):
        cmds_list = ["!" + cmd.name for cmd in self.bot.commands] + ["\n"]
        exibe = ""

        for cmd in self.bot.commands:
            if cmd == self.bot.get_command("comandos"):
                continue
            exibe += f"**!{cmd.name}**: {cmd.help}\n"

        await ctx.send(f"Comandos disponíveis: \n{exibe}\nUse !help <comando> para mais detalhes sobre um comando específico.")
        return


async def setup(bot):
    await bot.add_cog(CommandsList(bot))