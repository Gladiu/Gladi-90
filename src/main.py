import discord_token # used for bot token
import discord
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@tree.command(name = "Register for Tourney!", description = "Register for tourney") 
async def Register_for_tourney(interaction):
    print(interaction.user.id)
    await interaction.response.send_message("Hello!")

@client.event
async def on_ready():
    await tree.sync()
    print("Ready!")
    

client.run(discord_token.TOKEN)
