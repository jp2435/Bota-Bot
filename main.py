import discord
from discord.ext import commands

import os
import asyncio
import random
from web_server import web_server

my_secret = os.environ['TOKEN']

infoclient = discord.Client()
client = commands.Bot(command_prefix='--')

#Inicio call

#Fim call

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd)

    print('We have logged in as {0.user}'.format(client))

#discord.Streaming(name="Como atropelar belhotas",  url="https://www.youtube.com/watch?v=dCgFVejm1-o")
#await client.change_presence(status=discord.Status.dnd, activity=discord.Streaming(name="How to scam", url="https://www.twitch.tv/scam")) Streaming
#await client.change_presence(activity=discord.Game('Chouriço')) Game
#await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Como atropelar belhotas")) watching
#@client.event
#async def on_message(message):
#    if message.author == client.user:
#      return

#    if message.content.startswith():
#      await message.channel.send("Boa tarde")


#Pra remover o comando padrão de help
client.remove_command("help")

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)


@client.command()
async def embedtest(ctx):
  embed=discord.Embed(title="Exemplo Embed", url="https://github.com/", description="E tu que dizes sobre isto? hum", color=0x9b42f5)
  embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/790612398070300673/845689775565570058/bota_que_tem.png")
  await ctx.send(embed=embed)

@client.command() #exemplo de embed
async def embed(ctx):
    embed=discord.Embed(title="Exemplo Embed", url="https://github.com/", description="E tu que dizes sobre isto? hum", color=0x9b42f5)
    await ctx.send(embed=embed)

@client.command()
async def ded(ctx):
  embed=discord.Embed(title="Papagaio are ded?", url="https://ded-scamwebsite.com", description="Maibi Papagaio ar ded bate neber num watt ar happen", color=0xc0f03)
  await ctx.send(embed=embed)
  
@client.command()
async def help(ctx):
    await ctx.send("test, \nhelp")

@client.command()
async def test(ctx, arg):
    await ctx.send(arg)

@client.command()
async def oqueémelhorque(ctx,arg):
    await ctx.send("O que é melhor que "+ arg)
    await ctx.send('CONA')


#@client.event
#async def on_member_join(member):
#  print(f'{member} entrou no servidor')

#@client.event
#async def on_member_remove(member):
#  print(f'{member} saiu do servidor')

web_server()
client.run(os.getenv('TOKEN'))
client.add_command(test)