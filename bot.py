import discord
from discord.ext import commands

bot = commands.Bot("-")

@bot.command()
async def battlesceptre(ctx, who: discord.Member):
    role = ctx.guild.get_role(561682160801546251)
    if role not in who.roles:
        await ctx.send(f"{ctx.author.mention} is not a wielder of the Battle Sceptre!")
    else:
        await ctx.send(f"{ctx.author.mention} has used a battle sceptre on {who.mention}! Oh no!")

@bot.event
async def on_member_join(member):
    guild = member.guild
    role = guild.get_role(559123130191446028)
    await member.add_roles(role)
    await guild.get_channel(559122949140119553).send(f"Welcome to Britain, {member.mention}, I hope you had a pleasant flight. But before you can pass you must answer me these riddles three: do you have rabies, what is your favourite hot beverage and what condiment do you have chips with?")


if __name__ == "__main__":
    from os import environ
    import sys
    token = environ.get("BOT_TOKEN", None)
    if token is None:
        sys.exit("Please set envvar BOT_TOKEN to your token.")
    else:
        bot.run(token)
