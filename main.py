import discord 
import os 
import random
import requests
import json
from stay_awake import stay_awake
from replit import db

bot = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]

doggo_list = [
  "https://media1.tenor.com/images/0b427c8b9deae36ab887f219c5d86304/tenor.gif?itemid=10310980",
  "https://th.bing.com/th/id/R13519d06325ebb81fb6a8ff1d2f1a130?rik=cHuzfPp3MmxOjA&riu=http%3a%2f%2fgifimage.net%2fwp-content%2fuploads%2f2017%2f07%2fdoggo-gif-5.gif&ehk=2ac7Rua2VWZM0Rv1PRR5I%2f%2fWzpvEtnWrVB5%2bKm3zkjU%3d&risl=&pid=ImgRaw",
  "https://media1.tenor.com/images/eab50baa14b17576489741219d4dfa1e/tenor.gif?itemid=17143316"
]

if "responding" not in db.keys():
  db["responding"] = True

def delete_encouragment(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
  db["encouragements"] = encouragements

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@bot.event
async def on_ready():
  print("We have logged on as {0.user}".format(bot))

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
    
  msg = message.content

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"]

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))
  
  if message.content.startswith("$cheems"):
    await message.channel.send(random.choice(doggo_list))

  if message.content.startswith("$inspire"):
    quote = get_quote()
    await message.channel.send(quote)

  if msg.startswith("$new"):
    encouraging_message = msg.split("$new ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")

  if msg.startswith("$del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$del",1)[1])
      delete_encouragment(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)
    
  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")

stay_awake()
bot.run(os.getenv('TOKEN'))