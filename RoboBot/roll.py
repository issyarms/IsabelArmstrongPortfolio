import discord
from discord.ext import commands
import random, asyncio

class Roll(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  @commands.cooldown(1, 86400, commands.BucketType.user)
  async def lmkroll(self, ctx):
    with open("./responses/lmkRolls.txt", "r") as f:
      character = f.readlines()
      responses = random.choice(character)
    await ctx.send(f'You got {responses[:-1]}!')
  
  @commands.command()
  @commands.cooldown(1, 86400, commands.BucketType.user)
  async def tohroll(self, ctx):
    with open("./responses/tohRolls.txt", "r") as f:
      character = f.readlines()
      responses = random.choice(character)
    await ctx.send(f'You got {responses[:-1]}!')

  @commands.Cog.listener()
  async def on_command_completion(self, ctx):
    await asyncio.sleep(86400)
    await ctx.send(f'{ctx.message.author.mention}, {ctx.command.name} is ready!')
  
  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      cd = round(error.retry_after)
      cd = cd % (24 * 3600)
      hours = cd // 3600
      cd %= 3600
      minutes = cd // 60
      cd %= 60
      await ctx.send(f'You can use this command again in {hours} hour(s), {minutes} minute(s), {cd} second(s)')


def setup(bot):
  bot.add_cog(Roll(bot))