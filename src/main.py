from nextcord import Message, Intents
from nextcord.ext import commands
from dotenv import dotenv_values
import aiopg

dsn = "dbname=tdb user=postgres password=passwd host=127.0.0.1"

intents = Intents(messages=True, message_content = True, guilds=True);
bot = commands.Bot(intents=intents);
config = dotenv_values("./.env")
TOKEN = config["TOKEN"]

async def go(state_ment):
    async with aiopg.create_pool(dsn) as pool:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                if(state_ment == ""):
                    return
                await cur.execute(state_ment)
                ret = []
                async for row in cur:
                    ret.append(row)
                return ret


@bot.event
async def on_ready():
    print(f"WoW i actualy work")

@bot.event
async def on_message(msg: Message):
    if(msg.author.bot):
        return
    result = await go(msg.content);
    await msg.reply(str(result));

bot.run(TOKEN)
