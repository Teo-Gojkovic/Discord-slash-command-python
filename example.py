import discord
from discord import app_commands

id_server = 000000000000000000 #remove zeros and enter your server ID

my_guild = discord.Object(id = id_server)
class MyClient(discord.Client):
    def __init__ (self, *, intents:discord.Intents): 
        super().__init__(intents=intents)
        self.tree= app_commands.CommandTree(self)

    async def setup_hook(self): 
        self.tree.copy_global_to(guild=my_guild)
        await self.tree.sync(guild = my_guild)

intents = discord.Intents.default()
bot = MyClient(intents=intents)

#print in console name and ID of your discord bot
@bot.event 
async def on_ready():
    print(f'Connected as {bot.user} with ID {bot.user.id}')

#example for make your command
@bot.tree.command(description='command description')
async def example(interaction = ''):
    await interaction.response.send_message("")
