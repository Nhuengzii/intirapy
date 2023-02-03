import nextcord
from nextcord.ext import commands
from dotenv import dotenv_values

bot = commands.Bot()
config = dotenv_values("./.env")
TOKEN = config["TOKEN"]

@bot.event
async def on_ready():
    print(f"WoW i actualy work")



bot.run(TOKEN)
