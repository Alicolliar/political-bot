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
    token = environ.get("BOT_TOKEN", "NDc5NzQ0MjA3MzM1MTk0NjQ2.Xf1g2Q.4eeQh8eRhxMcQz6GRWIigdiabeU")
    if token is None:
        sys.exit("Please set envvar BOT_TOKEN to your token.")
    else:
        bot.run(token)
