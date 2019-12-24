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
       await ctx.send(f"{ctx.author.mention} must be an immigration officer to immigrate people. If you are interested in being an immigration officer, talk to someone.")


@bot.command()
async def knight(ctx, who: discord.Member):
    """To be used by the Monarch after consultation with the Cabinet."""
    monarch = ctx.guild.get_role(575353983309316106)
    regent = ctx.guild.get_role(656248716352684043)
    commoner = ctx.guild.get_role(575350847160975360)
    lord = ctx.guild.get_role(575379860944322571)
    if monarch in ctx.author.roles or regent in ctx.author.roles:
        await who.add_roles(lord)
        await who.remove_roles(commoner)
        await ctx.send(f"I, {ctx.author.mention} Regina, hereby dub thee Lord {who.mention}. You may sit in the House of Lords now.")
    else:
        await ctx.send(f"Oi, you! What the bloody hell are you doing 'ere?! Why do you have that sword? Gaurds!")



@bot.command()
async def arrest(ctx, who: discord.Member):
    """Lets police officers arrest people without cause."""
    police = ctx.guild.get_role(650004142198095872)
    arrested = ctx.guild.get_role(654070645663072256)
    arrested_roles = [arrested]
    if police in ctx.author.roles:
        await ctx.guild.get_channel(654296229454544926).send(f"{ctx.author.mention} has arrested {who.mention}, make them feel as miserable as possible.")
        await who.edit(roles=arrested_roles)
    else:
        await ctx.send(f"{ctx.author.mention} isn't a police officer. If you are interested in being a police officer, talk to someone.")


@bot.command()
async def startvote(ctx, place, subject):
    """Used by the speaker to set up elections/votes."""
    speaker = ctx.guild.get_role(575355569712398348)
    global voteStatus
    if speaker in ctx.author.roles:
        if place == "public":
            await ctx.guild.get_channel(654305941331902511).send(f"The Speaker has started a vote on the subject of "+subject)
            await ctx.guild.get_channel(657273438796513310).send(f"A vote has been started on the subject of "+subject+". Please vote using the relevant bot commands.")
            voteStatus = [1,0,0]
        elif place == "commons":
            await ctx.guild.get_channel(654337039445000201).send(f"The Speaker has started a vote on the subject of "+subject)
            await ctx.guild.get_channel(649879662092222464).send(f"A vote has been started for "+subject+". Please vote using the relevant bot commands.")
            voteStatus = [0,1,0]
        elif place == "lords":
            await ctx.guild.get_channel(654337184429768740).send(f"The Speaker has started a vote on the subject of "+subject)
            await ctx.guild.get_channel(649879745189904384).send(f"A vote has been started for "+subject+". Please vote using the relevant bot commands.")
            voteStatus = [0,0,1]
        else:
            await ctx.send(f"Sorry, Speaker, but you can't set up a vote for that group.")
    else:
        await ctx.send(f"Sorry, but only the Speaker can set up votes.")



@bot.command()
async def vote(ctx, vote):
    """Used by people, MPs and Lords to vote in elections, referenda and House votes."""
    mp = ctx.guild.get_role(575350844724084736)
    lord = ctx.guild.get_role(575379860944322571)
    commoner = ctx.guild.get_role(575350847160975360)
    if voteStatus == [1,0,0]:
        if commoner not in ctx.author.roles:
            await ctx.send("You are not able to take part in this election. If you believe you have been disenfranchised, talk to any government employee.")
        else:
            await ctx.send(f"Thank you {ctx.author.mention}, your vote has been registered.")
            await ctx.guild.get_channel(654305941331902511).send(f"**One** Vote has been registered for: "+vote)
            await ctx.Messge.delete()
    elif voteStatus == [0,1,0]:
        if mp not in ctx.author.roles:
            await ctx.send(f"You are unable to take part in this vote. If you believe you have been disenfranchised, please talk to any government employee.")
        else:
            ctx.send(f"Thank you {ctx.author.mention}, your vote has been registered.")
            await ctx.guild.get_channel(654337039445000201).send(f"**One** Vote has been registeredd for: "+vote)
            await ctx.Message.delete()
    elif voteStatus == [0,0,1]:
        if lord not in ctx.author.roles:
            await ctx.send(f"You are unable to take part in this vote. If you believe you have been disenfranchised, please talk to any government employee.")
        else:
            await ctx.send(f"Thank you {ctx.author.mention}, your vote has been registered.")
            await ctx.guild.get_channel(654337184429768740).send(f"**One** Vote has been registered for: "+vote)
            await ctx.Message.delete()
    else:
        await ctx.send(f"There is no vote happening right now.")

@bot.command()
async def endvote(ctx):
    """Used by the speaker to end elections/votes."""
    speaker = ctx.guild.get_role(575355569712398348)
    global voteStatus
    if speaker in ctx.author.roles:
        if voteStatus == [1,0,0]:
            await ctx.guild.get_channel(657273438796513310).send(f"The election has ended, the results will be announced shortly.")
            await ctx.guild.get_channel(654305941331902511).send(f"The election ended.")
            voteStatus = [0,0,0]
        elif voteStatus == [0,1,0]:
            await ctx.guild.get_channel(649879662092222464).send(f"The vote has ended, the result will be announced shortly.")
            await ctx.guild.get_channel(654337039445000201).send(f"The vote ended.")
            voteStatus = [0,0,0]
        elif voteStatus == [0,0,1]:
            await ctx.guild.get_channel(649879745189904384).send(f"The vote has ended, the results will be announced shortly.")
            await ctx.guild.get_channel(654337184429768740).send(f"The vote ended.")
            voteStatus = [0,0,0]
        else:
            await ctx.send(f"There is not a vote to end, Speaker.")
    else:
        await ctx.send(f"Sorry, but only the Speaker can end votes.")


@bot.event
async def on_member_join(member):
    guild = member.guild
    role = guild.get_role(575350849639809073)
    await member.add_roles(role)
    await guild.get_channel(575351598973321229).send(f"Welcome to Britain, {member.mention}, I hope you had a pleasant flight. But before you can pass you must answer me these riddles four: do you have rabies, what is your favourite hot beverage, are you a fascist and what condiment do you have chips with?")


if __name__ == "__main__":
    from os import environ
    import sys
    token = environ.get("BOT_TOKEN", "YOUR-TOKEN-HERE")
    if token is None:
        sys.exit("Please set envvar BOT_TOKEN to your token.")
    else:
        bot.run(token)
