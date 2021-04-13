import os
import discord
from discord import Activity, ActivityType
from keep_alive import keep_alive
import random
import requests
import json
from discord.ext import tasks
from itertools import cycle
import asyncio
from discord.ext import commands
import logging 
import datetime
import json

client = discord.Client()

    # On Ready

@client.event
async def on_ready():
  change_status.start()
  print('{0.user}'.format(client))
  print('Is Online')
  print('-----------')

    # Status Task

@tasks.loop(seconds=2)
async def change_status():
  await client.change_presence(activity=discord.Game(next(status)))

# Actions

client.blacklisted_users = []

coinflip_actions = ['You Got  __**Heads!!**__', '>>> You Got __**Tails!!**__']

tips = [
  '> **Tip** __**d/doggo**__ Sends Cute Images Of Dogs!!',
  '> **Tip** Join The Community!!',
  '> **Tip** Join The Support Server If You Need Any Help!!'
  ]

grabify_links = [
'https://lovebird.guru',
'https://trulove.guru',
'https://dateing.club',
'otherhalf.life',
'https://shrekis.life',
'https://headshot.monster',
'https://gaming-at-my.best',
'https://progaming.monster',
'https://yourmy.monster',
'https://screenshare.host',
'https://imageshare.best',
'https://screenshot.best',
'https://https://gamingfun.me',
'https://catsnthing.com',
'https://mypic.icu',
'https://catsnthings.fun',
'https://curiouscat.club',
'https://joinmy.site',
'https://fortnitechat.site',
'https://fortnight.space',
'https://freegiftcards.co',
'https://stopify.co',
'https://leancoding.co',
'https://grabify.link'
]

status = cycle([
'd/help',
'd/invite',
'Join The Community!!',
])

emoji = '\N{THUMBS UP SIGN}'

# API Commands

#Get Dog API

def get_puppy():
  response = requests.get("https://dog.ceo/api/breeds/image/random")
  embed_data = json.loads(response.text)
  string=embedpic = embed_data['message']
  e = discord.Embed(title= 'Doggo Picture')
  e.set_image(url=embedpic)
  return(e)

  # Get Quote API


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = "**" + json_data[0]['q'] + "** *-" + json_data[0]['a'] + "*"
  return(quote)

# Webhook api

def get_upvote():
  response = requests.get("https://discord.com/api/webhooks/829706631834632243/GxEAqOd0132ESYkmyDfvR2OGaXkU1wsLEotOACIS6k9cdP-VapCxwyuWo9LMxakMQwOI")
  json_data = json.loads(response.text)
  upvote = "**" + json_data[0]['q'] + "** *-" + json_data[0]['a'] + "*"
  return(upvote)


#Main Features 

#vars
owners_id = [517020964261855232, 659813166678540320]

@client.event
async def on_message(message):
    if message.author.bot :
      return

    for i in range(len(grabify_links)):
      if message.content == grabify_links[i]:
        await message.delete()
        await message.channel.send(f"Really {message.author}??\n Manz Sent A Grabify Link Lmao")
      elif f"{message.content}" == f"https://{grabify_links[i]}":
        await message.delete()
        await message.channel.send("u nub")
        break

    if message.content.startswith("d/echo"):
      await message.channel.send(message.content[7:].format("```message```"))
      await message.add_reaction(emoji)

    if 'Hello <@796802441000648714>' in message.content:
      await message.channel.send(f'Check Your DMs {message.author}')
      await message.author.send(f"Hello {message.author.mention}\n If There Is Any Problems Feel Free To Type `d/help` And Join The Support Server!!")
      await message.add_reaction(emoji)

    if '<@796802441000648714>' in message.content:
      await message.channel.send(f'Check Your DMs {message.author}')
      await message.author.send(f"Hello {message.author.mention}\n If There Is Any Problems Feel Free To Type `d/help` And Join The Support Server!!")
      await message.add_reaction(emoji)

    # Delete Invite Links

    if 'https://discord.gg/' in message.content:
      await message.delete()
      await message.author.send("No Links Allowed!!")
      print(f"Link Was Deleted, Sent By {message.author} ") 

    if 'Nigger' in message.content:
      await message.delete()
      await message.author.send(f"Really {message.author.mention}")

    if 'nigger' in message.content:
      await message.delete()
      await message.author.send(f"Really {message.author.mention}")

         # Inspire Command

    msg = message.content

    if msg.startswith('d/inspire'):
      quote = get_quote()
      quote_text = '**__Quote:__**\n> {}'.format(quote)
      await message.channel.send(quote_text)
      print(f'Inspire Command Ran By {message.author}')
      await message.add_reaction(emoji)

    # Ping Command
    if message.content.startswith('TestPing'):
      await message.channel.send(f" My Latency Is {round(client.latency *1000)} Milliseconds!!")

    #  await message.channel.send(f"{client.latency}")

    if message.content.startswith('d/ping'):
      if round(client.latency * 1000) <= 50:
        embed=discord.Embed(title="Pong", description=f":ping_pong: Pingpingpingpingping!\n My Latency Is {round(client.latency *1000)} Milliseconds!", color=message.guild.get_member(client.user.id).color)
      elif round(client.latency * 1000) <= 100:
        embed=discord.Embed(title="Pong", description=f":ping_pong: Pingpingpingpingping!\n My Latency Is {round(client.latency *1000)} Milliseconds!", color=message.guild.get_member(client.user.id).color)
      elif round(client.latency * 1000) <= 200:
        embed=discord.Embed(title="Pong", description=f":ping_pong: Pingpingpingpingping!\n My Latency Is {round(client.latency *1000)} Milliseconds!", color=message.guild.get_member(client.user.id).color)
      else:
        embed=discord.Embed(title="Pong", description=f":ping_pong: Pingpingpingpingping!\n My Latency Is {round(client.latency *1000)} Milliseconds!", color=message.guild.get_member(client.user.id).color)
      await message.channel.send(embed=embed)
      print(f"Ping Command Ran By {message.author} ") 
      await message.add_reaction(emoji)

    # Doggo Command

    if message.content.startswith('d/doggo'):
      embed = get_puppy()
      await message.channel.send(random.choice(tips))
      await message.channel.send(embed=embed)
      print(f"Doggo Ran By {message.author} ") 
      await message.add_reaction(emoji)
 
    # Meme Command NOT DONE 

    # Coinflip Command

    if message.content.startswith('d/coinflip'):
      await message.channel.send(random.choice(coinflip_actions))
      print(f"Coinflip Command Ran By {message.author} ") 
      await message.add_reaction(emoji)

    # Invite Command

    if message.content.startswith('d/invite'):
        await message.channel.send(random.choice(tips))
        embedVar = discord.Embed(title="**Invite**", description="Add The Bot To Your Own Server!!", color=message.guild.get_member(client.user.id).color)
        embedVar.add_field(name="Dxrk's Son Bot Pages", value="[DiscrdBotList](https://discordbotlist.com/bots/dxrks-son)\n[Top.gg](https://top.gg/bot/796802441000648714)", inline=True)
        await message.channel.send(embed=embedVar)
        print(f"Invite Command Ran By {message.author} ") 
        await message.add_reaction(emoji)

    # Help Command

    if message.content.startswith('d/help'):
      embedVar = discord.Embed(title=":star2: **Help** :star2:", description="All Commands You Can Do With Dxrk's Son!!\n__**Main Commands**__\nd/support\nd/devs\nd/invite\nd/ping\nd/vote\n__**Fun Commands**__\nd/inspire\nd/followers\nd/coinflip\nd/echo\nd/doggo\nd/servers\nd/list - Mod Command Only\n", color=message.guild.get_member(client.user.id).color)
      embedVar.add_field(name="__**Our Discord Servers**__", value="[**Community Server**](https://discord.gg/325CGZBCfD)\n[**Support Server**](https://discord.gg/j9b9DtfheU)", inline=True)
      await message.channel.send(embed=embedVar)
      await message.add_reaction(emoji)

    if message.content.startswith('d/devs'):
        embedVar = discord.Embed(title="Helpers", description="DxrkPxndx \nBubz", color=message.guild.get_member(client.user.id).color)
        embedVar.add_field(name="__**Community**__", value="Join The Support Server\n[**Support Server**](https://discord.gg/j9b9DtfheU)", inline=True)
        await message.channel.send(embed=embedVar)
        print(f"Devs Command Ran By {message.author} ") 
        await message.add_reaction(emoji)

    # Vote Command

    if message.content.startswith('d/vote'):
        embedVar = discord.Embed(title="Vote For Dxrk's Son", description="Voters Will A Thanks If You DM DxrkPxndx With Proof You Have Voted", color=message.guild.get_member(client.user.id).color)
        embedVar.add_field(name="Upvote", value="[**Top.gg Upvote Dxrks Son**](https://top.gg/bot/796802441000648714/vote)", inline=True)
        await message.channel.send(embed=embedVar)
        print(f"Vote Command Ran By {message.author} ") 
        await message.add_reaction(emoji)

    # Follower Command

    if message.content.startswith('d/followers'):
      embedVar = discord.Embed(title=":star2: **Supporters** :star2:", description="All The People That Have Dxrk's Son In There Servers!!\nThunderbird765\nAlmanacHack#8888 ", color=message.guild.get_member(client.user.id).color)
      embedVar.add_field(name="How To Be Added To This Board", value="DM DxrkPxndx#4425 Saying Your Server Name And That You Have The Bot In Your Server", inline=True)
      await message.channel.send(embed=embedVar)
      print(f"Follower Command Ran By {message.author} ")
      await message.add_reaction(emoji)

    if message.content.startswith('d/list'):
      for i in range(len(owners_id)):
        servers = list(client.guilds)
        if message.author.id == owners_id[i]:
          await message.channel.send(f'Check Your DMs {message.author} : ) ')
          await message.author.send(f"Connected on {str(len(servers))}  servers:")
          await message.author.send('\n' .join(guild.name for guild in  client.guilds))
        elif message.author.id == owners_id[i+1]:
          pass
        elif message.author.id == owners_id[i-1]:
          pass
        else:
          await message.channel.send('You Do Not Have Permission To Use This Command\n\nSad : ( ')
      await message.add_reaction(emoji)

    if message.content.startswith ('d/servers'):
      servers = list(client.guilds)
      await message.channel.send(f"Connected on {str(len(servers))}  Servers")

keep_alive()
client.run(os.getenv('TOKEN')) 
