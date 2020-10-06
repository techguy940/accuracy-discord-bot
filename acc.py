import discord
from discord.ext import commands
import random

botToken = ""
botPrefix = ""
accRole = ""
bot=commands.Bot(command_prefix=botPrefix)

@bot.event
async def on_ready():
    print("Logged in as "+bot.user.name)


@bot.command()
@commands.has_role(accRole)
async def acc(ctx,gameName=None,time=None,accuracy=None,winAmt=None,*,status=None):
    embed=discord.Embed(
        title="Accuracy",
        description="Game: {}\nTiming: {}\nAccuracy: {}\nWinning Amount: {}\nStatus: {}".format(gameName,time,accuracy,winAmt,status),
        colour=random.randint(0,0xfffff)
        )

    await ctx.send(embed=embed)
@acc.error
async def acc_error(ctx,error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send("You need {} to use this command".format(accRole))
    else:
        raise error


###EXAMPLE = {botPrefix}acc Loco 1:30PM 10/10 2.37rs All won


bot.run(botToken)

