from nextcord import Message, Intents
from nextcord.ext import commands
from dotenv import dotenv_values

intents = Intents(messages=True, guilds=True);
bot = commands.Bot(intents=intents);
config = dotenv_values("./.env")
TOKEN = config["TOKEN"]

@bot.event
async def on_ready():
    print(f"WoW i actualy work")

#bot.event
@bot.event
async def on_message(msg: Message):
    print(f"cutor {msg.author.name}" + msg.content);

bot.run(TOKEN)
