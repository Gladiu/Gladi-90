import discord_token # used for bot token
import discord
import tournament

bot = discord.Bot()

tournament_instance = tournament.Tournament()

@bot.application_command(name="register", description="Register for the Tournament.") # this decorator makes a slash command
async def register(ctx):
    if await tournament_instance.participant_register(ctx.author):
        await ctx.author.send("You have succesfully registered to a tournament! ")
    else:
        await ctx.author.send("You have already registered!")
    await ctx.delete()
        
    
@bot.event
async def on_message(message):
    if message.channel.type is discord.ChannelType.private and message.author != bot.user:
        print(message.content)



bot.run(discord_token.TOKEN)