# External packages
import watchdog.events
import watchdog.observers
import discord
import time

# #
import discord_token # used for bot token
import tournament

bot = discord.Bot()

tournament_instance = tournament.Tournament()
tournament_instance.import_names()

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
        if message.content.find("!generate") != -1:
            print(message.content)
            tournament_instance.generate_matches()
            print(tournament_instance.matches)



class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.json'],
                                                             ignore_directories=True, case_sensitive=False)
 
    def on_modified(self, event):
        #print("Watchdog received modified event - % s." % event.src_path)
        if event.src_path.find("seeded_players") != -1:
            tournament_instance.update_seeds_from_json()

if __name__ == "__main__":
    src_path = r"src/shared_data"
    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()

    bot.run(discord_token.TOKEN)
    observer.join()