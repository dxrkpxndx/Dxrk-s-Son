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

client = discord.Client()



status = cycle([
'd/help',  
'Made By DxrkPxndx',
'd/support',
'I Am Online',
'Join The Community!!'
])

@client.event
async def on_ready():
  change_status.start()
  print('Bot is online and to go {0.user}'.format(client))

@tasks.loop(seconds=3.2)
async def change_status():
  await client.change_presence(activity=discord.Game(next(status)))



coinflip_actions = ['You Got  **Heads!!**', '>>> You Got **Tails!!**']

tips = [
  '> **Tip** Join The Community By Doing __**d/support**__ If You Need Any Help',
  '> **Tip** __**d/doggo**__ Sends Cute Images Of Dogs!!',
  '> **Tip** __**d/list**__ Sends A List Of all The Servers I Am In In!!',
  ]
 


inspires = ['“Do what you can, with what you have, where you are.” – Theodore Roosevelt.', '“If you can dream it, you can do it.” – Walt Disney.']


def get_puppy():
  response = requests.get("https://dog.ceo/api/breeds/image/random")
  embed_data = json.loads(response.text)
  string=embedpic = embed_data['message']
  e = discord.Embed(title= 'Doggo Picture')
  e.set_image(url=embedpic)
  return(e)

@client.event
async def on_message(message):
    if message.author.bot :
      return
       
    if message.content.startswith('d/help'):
      await message.channel.send(f'Hello {message.author} I Have Just Sent You A DM')
      await message.author.send(f"Hello {message.author}\nI Am Dxrk's Son A Bot Made By DxrkPxndx Him Self\nIf There Is Any Problems With The Bot Feel Free To Join The Suppport Server And Join  One Of The Support Voice Channels And Someone Will Be With You Shortly Or If Its A Question Feel Free To Ask It In Our FAQ Channel")
      print(f"DM was sent to {message.author}")

    if message.content.startswith('d/inspire'):
      await message.channel.send(random.choice(inspires))
      print(f"Inspire Command Ran By {message.author} ") 

      #test for invite urls.
    if message.content.startswith('https://discord.gg/'):
      await message.delete()
      await message.channel.send('No Links Allowed!!')
      print(f"Link Was Deleted, Sent By {message.author} ") 

    if message.content.startswith('d/list'):
      servers = list(client.guilds)
      await message.channel.send(f"Connected on {str(len(servers))}  servers:")
      await message.channel.send('\n' .join(guild.name for guild in  client.guilds))
      print(f"List Command Ran By {message.author}  ") 



    #if(message.content.startswith('d/help')):
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

    if message.content.startswith('d/doggo'):
      embed = get_puppy()
      await message.channel.send(random.choice(tips))
      await message.channel.send(embed=embed)
      print(f"Dog Command Ran By {message.author} ") 

    if message.content.startswith('d/coinflip'):
      await message.channel.send(random.choice(coinflip_actions))
      print(f"Coinflip Command Ran By {message.author} ") 

    if message.content.startswith('d/invite'):
        await message.channel.send(random.choice(tips))
        embedVar = discord.Embed(title="**Invite**", description="Add The Bot To Your Own Server", color=message.guild.get_member(client.user.id).color)
        embedVar.add_field(name="Dxrks Community", value="Join The Discord If You Need Any Help", inline=True)
        embedVar.add_field(name="Dxrk's Son Discord Bot List Link", value="https://discordbotlist.com/bots/dxrks-son", inline=True)
        await message.channel.send(embed=embedVar)
        print(f"Invite Command Ran By {message.author} ") 

    if message.content.startswith('d/help'):
      embedVar = discord.Embed(title=":star2: **Help** :star2:", description="All Commands You Can Do With Dxrk's Son!!\nd/support\nd/devs\nd/invite\nd/coinflip\nd/doggo\nd/ping\nd/vote\nd/list\nd/inspire\nd/followers ", color=message.guild.get_member(client.user.id).color)
      embedVar.add_field(name="Command Help", value="DM DxrkPxndx#4425 With Any Questions Or Problems\nDxrkPxndx's Support Server\nhttps://discord.gg/3MGV26qnQy", inline=True)
      await message.channel.send(embed=embedVar)
      print(f"Help Command Ran By {message.author} ")

    if message.content.startswith('d/devs'):
        embedVar = discord.Embed(title="Helpers", description="DxrkPxndx \nPython#2313", color=message.guild.get_member(client.user.id).color)
        embedVar.add_field(name="Dxrks Community", value="Join The Discord If You Need Any Help", inline=True)
        embedVar.add_field(name="Invite Link", value="Type d/help If You Need Any Help", inline=True)
        await message.channel.send(embed=embedVar)
        print(f"Devs Command Ran By {message.author} ") 

    if message.content.startswith('d/vote'):
        embedVar = discord.Embed(title="Vote For Dxrk's Son", description="Voters Will A Thanks If You DM DxrkPxndx With Proof You Have Voted", color=message.guild.get_member(client.user.id).color)
        embedVar.add_field(name="Dxrks Community", value="Join The Discord If You Need Any Help\n https://discord.gg/3MGV26qnQy", inline=True)
        embedVar.add_field(name="Discord Bot List", value="https://discordbotlist.com/bots/dxrks-son", inline=True)
        await message.channel.send(embed=embedVar)
        print(f"Vote Command Ran By {message.author} ") 

    if message.content.startswith('d/support'):
        embedVar = discord.Embed(title="Join The Community", description="Join The Discord It You Have Any Questions About The Bot \nhttps://discord.gg/3MGV26qnQy", color=message.guild.get_member(client.user.id).color)
        embedVar.add_field(name="DxrkPxndx", value="DM DxrkPxndx#4425 With Any Questions Or Problems", inline=True)
        await message.channel.send(embed=embedVar)
        print(f"Support Command Ran By {message.author} ") 

    if message.content.startswith('d/followers'):
      embedVar = discord.Embed(title=":star2: **Supporters** :star2:", description="All The People That Have Dxrk's Son In There Servers!!\nThunderbird765\n ", color=message.guild.get_member(client.user.id).color)
      embedVar.add_field(name="How To Be Added To This Board", value="DM DxrkPxndx#4425 Saying Your Server Name And That You Have The Bot In Your Server", inline=True)
      await message.channel.send(embed=embedVar)
      print(f"Follower Command Ran By {message.author} ")

keep_alive()
client.run(os.getenv('TOKEN')) 
