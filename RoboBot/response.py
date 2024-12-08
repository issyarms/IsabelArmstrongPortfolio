import discord
from discord.ext import commands
import random

class Response(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author.bot:
      return
    
    if message.content.lower() in ["hows gumball?", "how's gumball?", "hows gumball", "how's gumball"]:
      await message.channel.send("How do you know about that?")
  
    if "mcdonalds" in message.content.lower() or "mc donalds" in message.content.lower() or "mcdonald's" in message.content.lower() or "mc donald's" in message.content.lower():
      await message.channel.send("I have the urge to traumatize a child.")
  
    if "party" in message.content.lower() or "porty" in message.content.lower():
      with open("./responses/partyResponses.txt", "r") as f:
        choice = f.readlines()
      response = random.choice(choice)
      await message.channel.send(response)
    

def setup(bot):
    bot.add_cog(Response(bot))