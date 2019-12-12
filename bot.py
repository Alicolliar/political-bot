import discord
from discord.ext import commands

bot = commands.Bot("-")

@bot.command()
async def battlesceptre(ctx, who: discord.Member):
    """To be used by those who hold the battlesceptre only""" 
    role = ctx.guild.get_role(650003761577721877)
    if role not in who.roles:
        await ctx.send(f"{ctx.author.mention} is not a wielder of the Battle Sceptre!")
    else:
        await ctx.send(f"{ctx.author.mention} has used a battle sceptre on {who.mention}! Oh no!")
        await ctx.send(f":battlesceptre:")


@bot.command()
async def immigrate(ctx, who: discord.Member):
    """To allow immigration officers to enter our fine country"""
    role = ctx.guild.get_role(650004142198095872)
    if role in ctx.author.roles:
       immigrant = ctx.guild.get_role(575350849639809073)
       commoner = ctx.guild.get_role(575350847160975360)
       await who.remove_roles(immigrant)
       await who.add_roles(commoner)
       await ctx.send(f":thumbsup: {who.mention} is no longer an immigrant. Cause no trouble!")
    else:
       await ctx.send(f"{ctx.author.mention}  must be an immigration officer to immigrate people. If you are interested in being an immigration officer, talk to someone.")


@bot.command()
async def knight(ctx, who: discord.Member):
    """To be used by the Monarch after consultation with the Cabinet."""
    monarch = ctx.guild.get_role(575353983309316106)
    commoner - ctx.guild.get_role(575350847160975360)
    lord = ctx.guild.get_role(575379860944322571)
    if monarch in ctx.author.roles:
        await who.remove_roles(lord)
        await who.add_roles(commoner)
        await ctx.send(f"I, {ctx.author.mention} Regina, hereby dub thee Lord {who.mention}. You may sit in the House of Lords now.")
    else:
        await ctx.send(f"Oi, you! What the bloody hell are you doing 'ere?! Why do you have that sword? Gaurds!")


@bot.command()
async def arrest(ctx, who: discord.Member):
    """Lets police officers arrest people wuthout cause."""
    police = ctx.guild.get_role(650004142198095872)
    arrested = ctx.guild.get_role(654070645663072256)
    if police in ctx.author.roles:
        await ctx.guild.get_channel(654296229454544926).send(f"{ctx.author.mention} has arrested {who.mention}, make them feel as miserable as possible.")
        await who.add_roles(arrested)
    else:
        await ctx.send(f"{ctx.author.mention} isn't a police officer. If you are interested in being a police officer, talk to someone.")

@bot.event
async def on_member_join(member):
    guild = member.guild
    role = guild.get_role(575350849639809073)
    await member.add_roles(role)
    await guild.get_channel(575351598973321229).send(f"Welcome to Britain, {member.mention}, I hope you had a pleasant flight. But before you can pass you must answer me these riddles four: do you have rabies, what is your favourite hot beverage, are you a fascist and what condiment do you have chips with?")


if __name__ == "__main__":
    from os import environ
    import sys
    token = environ.get("BOT_TOKEN", "YOUR_TOKEN_HERE")
    if token is None:
        sys.exit("Please set envvar BOT_TOKEN to your token.")
    else:
        bot.run(token)
