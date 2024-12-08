import discord
from discord.ext import commands
from ready import Ready
from response import Response
from roll import Roll
import os

TOKEN = os.getenv("TOKEN")



def run():
  bot = commands.Bot(command_prefix=">", intents=discord.Intents.all(), activity=discord.Game(">help"))

  @bot.event
  async def on_ready():
    await bot.add_cog(Ready(bot))
    await bot.add_cog(Response(bot))
    await bot.add_cog(Roll(bot))


    print(f'{bot.user} is now running!')
  
  bot.run(TOKEN)

if __name__ == "__main__":
  run()