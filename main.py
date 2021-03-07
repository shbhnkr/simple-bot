import discord 
import os 
import random
from stay_awake import stay_awake

bot = discord.Client()

doggo_list = [
  "https://media1.tenor.com/images/0b427c8b9deae36ab887f219c5d86304/tenor.gif?itemid=10310980",
  "https://th.bing.com/th/id/R13519d06325ebb81fb6a8ff1d2f1a130?rik=cHuzfPp3MmxOjA&riu=http%3a%2f%2fgifimage.net%2fwp-content%2fuploads%2f2017%2f07%2fdoggo-gif-5.gif&ehk=2ac7Rua2VWZM0Rv1PRR5I%2f%2fWzpvEtnWrVB5%2bKm3zkjU%3d&risl=&pid=ImgRaw",
  "https://media1.tenor.com/images/eab50baa14b17576489741219d4dfa1e/tenor.gif?itemid=17143316"
]


@bot.event
async def on_ready():
  print("We have logged on as {0.user}".format(bot))

@bot.event
async def on_message(message):
  print("Received message")
  if message.author == bot.user:
    return

  if message.content.startswith("cheems"):
    await message.channel.send(random.choice(doggo_list))
  else:
    await message.channel.send("no cheems for you")

stay_awake()
bot.run(os.getenv('TOKEN'))