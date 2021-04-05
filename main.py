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

client = discord.Client()

    # On Ready

@client.event
async def on_ready():
  change_status.start()
  print('{0.user}'.format(client))
  print('Is Online')
  print('-----------')
  print('Dont Fuck This Up')

    # Status Task

@tasks.loop(seconds=3.2)
async def change_status():
  await client.change_presence(activity=discord.Game(next(status)))

# Actions

coinflip_actions = ['You Got  **Heads!!**', '>>> You Got **Tails!!**']

tips = [
  '> **Tip** Join The Community By Doing __**d/support**__ If You Need Any Help',
  '> **Tip** __**d/doggo**__ Sends Cute Images Of Dogs!!',
  '> **Tip** __**d/list**__ Sends A List Of all The Servers I Am In In!!',
  ]
 
grabify_links = ['']

invite_links = ['']

status = cycle([
'd/help',  
'Made By DxrkPxndx',
'd/support',
'I Am Online',
'Join The Community!!'
])

inspires = ['“Do what you can, with what you have, where you are.” – Theodore Roosevelt.', '“If you can dream it, you can do it.” – Walt Disney.']

# API Commands

#Get Dog API

def get_puppy():
  response = requests.get("https://dog.ceo/api/breeds/image/random")
  embed_data = json.loads(response.text)
  string=embedpic = embed_data['message']
  e = discord.Embed(title= 'Doggo Picture')
  e.set_image(url=embedpic)
  return(e)

# Get Meme API NOT READY

def get_anime():
  response = requests.get("https://animechan.vercel.app/api/random")
  embed_data = json.loads(response.text)
  string=embedpic = embed_data['message']
  e = discord.Embed(title= 'Oni-Chan')
  e.set_image(url=embedpic)
  return(e)

  # Get Quote API

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = "**" + json_data[0]['q'] + "** *-" + json_data[0]['a'] + "*"
  return(quote)

#Main Features 

@client.event
async def on_message(message):
    if message.author.bot :
      return



    # Help DM

    if message.content.startswith('d/help'):
      await message.channel.send(f'Hello {message.author.mention} I Have Just Sent You A DM.\nIf Your DMs Are Off You Wont Get A DM From Me :cry:')
      await message.author.send(f"Hello {message.author}\nI Am Dxrk's Son A Bot Made By DxrkPxndx Him Self\nIf There Is Any Problems With The Bot Feel Free To Join The Suppport Server And Join  One Of The Support Voice Channels And Someone Will Be With You Shortly Or If Its A Question Feel Free To Ask It In Our FAQ Channel\nhttps://discord.gg/KrXbCt2FjD")
      print(f"DM was sent to {message.author}")

    # Delete Invite Links

    if message.content.startswith('https://discord.gg/'):
      await message.delete()
      await message.author.send(f"No Links Allowed!!")
      print(f"Link Was Deleted, Sent By {message.author} ") 

         # Inspire Command

    msg = message.content

    if msg.startswith('d/inspire'):
      quote = get_quote()
      quote_text = '**__Quote:__**\n> {}'.format(quote)
      await message.channel.send(quote_text)
      print(f'request.zeninspire - {message.author}')



    if message.content.startswith('d!list'):
      servers = list(client.guilds)
      await message.channel.send(f"Connected on {str(len(servers))}  servers:")
      await message.channel.send('\n' .join(guild.name for guild in  client.guilds))
      print(f"List Command Ran By {message.author}  ") 

    # Botinfo Command

    if message.content.startswith('d/botinfo'):
        embedVar = discord.Embed(title="**Bot Info**", description="Dxrk's Son\nStart Date - Feb 24th 3:48PM 2021\nMade With - Repl.it\n Lines Of Code - 171\nFiles - 3\nBot Status - Online | Thanks To UptimeRobot\n Owner - DxrkPxndx\nDevs - Python", color=message.guild.get_member(client.user.id).color)
        embedVar.add_field(name="Dxrks Community And Support Server", value="Join The Discord If You Need Any Help\n https://discord.gg/3MGV26qnQy", inline=True)
        await message.channel.send(embed=embedVar)
        print(f"Info Command Ran By {message.author}") 

    # Ping Command

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

    # Doggo Command

    if message.content.startswith('d/doggo'):
      embed = get_puppy()
      await message.channel.send(random.choice(tips))
      await message.channel.send(embed=embed)
      print(f"Doggo Ran By {message.author} ") 

 
    # Meme Command NOT DONE 

    if message.content.startswith('d/anime'):
      embed = get_anime()
      await message.channel.send(random.choice(tips))
      await message.channel.send(embed=embed)
      print(f"MemeCommand Ran By {message.author} ") 

    # Coinflip Command

    if message.content.startswith('d/coinflip'):
      await message.channel.send(random.choice(coinflip_actions))
      print(f"Coinflip Command Ran By {message.author} ") 

    # Invite Command

    if message.content.startswith('d/invite'):
        await message.channel.send(random.choice(tips))
        embedVar = discord.Embed(title="**Invite**", description="Add The Bot To Your Own Server", color=message.guild.get_member(client.user.id).color)
        embedVar.add_field(name="Dxrks Community", value="Join The Discord If You Need Any Help", inline=True)
        embedVar.add_field(name="Dxrk's Son Discord Bot List Link", value="https://discordbotlist.com/bots/dxrks-son\nhttps://top.gg/bot/796802441000648714", inline=True)
        await message.channel.send(embed=embedVar)
        print(f"Invite Command Ran By {message.author} ") 

    # Help Command

    if message.content.startswith('d/help'):
      embedVar = discord.Embed(title=":star2: **Help** :star2:", description="All Commands You Can Do With Dxrk's Son!!\n__**Main Commands**__\nd/support\nd/devs\nd/invite\nd/ping\nd/botinfo\nd/vote\n__**Fun Commands**__\nd/inspire\nd/followers\nd/coinflip\nd/doggo ", color=message.guild.get_member(client.user.id).color)
      await message.channel.send(embed=embedVar)
      print(f"Help Command Ran By {message.author} ")

    # Devs Command

    if message.content.startswith('d/devs'):
        embedVar = discord.Embed(title="Helpers", description="DxrkPxndx \nPython#2313", color=message.guild.get_member(client.user.id).color)
        embedVar.add_field(name="Dxrks Community", value="Join The Discord If You Need Any Help", inline=True)
        embedVar.add_field(name="Invite Link", value="Type d/help If You Need Any Help", inline=True)
        await message.channel.send(embed=embedVar)
        print(f"Devs Command Ran By {message.author} ") 

    # Vote Command

    if message.content.startswith('d/vote'):
        embedVar = discord.Embed(title="Vote For Dxrk's Son", description="Voters Will A Thanks If You DM DxrkPxndx With Proof You Have Voted", color=message.guild.get_member(client.user.id).color)
        embedVar.add_field(name="Discord Bot List", value="https://discordbotlist.com/bots/dxrks-son/upvote", inline=True)
        await message.channel.send(embed=embedVar)
        print(f"Vote Command Ran By {message.author} ") 

    # Support Command

    if message.content.startswith('d/support'):
        embedVar = discord.Embed(title="__**Support Server**__", description="Join The Discord It You Have Any Questions About The Bot", color=message.guild.get_member(client.user.id).color)
        embedVar.add_field(name="__**Invite Link**__", value="Join Or Text In One Of Our Support Channels If You Need Help\nhttps://discord.gg/KrXbCt2FjD", inline=True)
        await message.channel.send(embed=embedVar)
        print(f"Support Command Ran By {message.author} ") 

    # Follower Command

    if message.content.startswith('d/followers'):
      embedVar = discord.Embed(title=":star2: **Supporters** :star2:", description="All The People That Have Dxrk's Son In There Servers!!\nThunderbird765\nAlmanacHack#8888 ", color=message.guild.get_member(client.user.id).color)
      embedVar.add_field(name="How To Be Added To This Board", value="DM DxrkPxndx#4425 Saying Your Server Name And That You Have The Bot In Your Server", inline=True)
      await message.channel.send(embed=embedVar)
      print(f"Follower Command Ran By {message.author} ")



keep_alive()
client.run(os.getenv('TOKEN')) 
