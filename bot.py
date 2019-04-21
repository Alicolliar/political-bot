import discord
from discord.ext import commands

bot = commands.Bot("-")

@bot.command()
async def battlesceptre(ctx, who: discord.Member):
    await ctx.send(f"{ctx.author.mention} has used a battle sceptre on {who.mention}! Oh no!")

if __name__ == "__main__":
    from sys import argv
    bot.run(argv[1])
