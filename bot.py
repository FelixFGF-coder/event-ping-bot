import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")

CHANNEL_ID = 1454452221310926849
ROLE_ID = 1454471319436529769

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_message(message):

    if message.author.id == bot.user.id:
        return

    if message.channel.id != CHANNEL_ID:
        return

    role = message.guild.get_role(ROLE_ID)
    if role:
        await message.channel.send(role.mention)

    await bot.process_commands(message)

bot.run(TOKEN)
