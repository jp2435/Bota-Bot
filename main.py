import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, CheckFailure
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
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name="--vai-te encher cheio de moscas", type=1))

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

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    embed = discord.Embed(title="Notificação Importante", color=0xff0000)
    embed.add_field(name="Tu deves ser é burro", value="Esse comando não existe")
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    resposta = "Enfim o que podemos fazer por ti {}, burro da piça".format(ctx.author)
    embed.set_footer(text=resposta)
    await ctx.send(embed=embed)
  if isinstance(error, CheckFailure):
      await ctx.send("Isto é muito poder para ti")
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Oh burro, faltam argumentos para eu trabalhar!!!")

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)

@client.command()
@commands.has_permissions(administrator=True)
async def DM(ctx, user: discord.User, *, message=None):
    message = message or "Oblá oh chouriço deves ser é tolinho"
    await user.send(message)

@client.command()
@commands.has_permissions(administrator=True)
async def admin(ctx):
  await ctx.send("é admin")

@admin.error
async def admin_error(ctx, error):
  if isinstance(error, CheckFailure):
      await ctx.send("Isto é muito poder para ti")

@client.command(name="say")
@commands.has_permissions(administrator=True)
async def say(ctx, channel:discord.TextChannel, *msg):
    message = " ".join(msg)
    #Embed making
    embed = discord.Embed(title="Notificação", color=discord.Color.dark_red())
    embed.add_field(name="Nova mensagem de {}".format(ctx.message.author), value="{}".format(message))
    embed.set_footer(text="{}".format(ctx.message.author))

    await channel.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, arg):
  amount = int(arg) + 1
  valor = int(arg)
  await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("És burro ou quê CRLH!!!, preciso de números")

@client.command()
async def ping(ctx):
    await ctx.send(f'My ping is {client.latency * 1000}!')

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
  embed=discord.Embed(title=" Lista de comandos", description="Todos os comandos que precisas", color=0xc0f03)
  embed.set_author(name="Bota Bot", url="https://github.com/jp2435/Bota-Bot", url_icon="https://cdn.discordapp.com/attachments/790612398070300673/845689775565570058/bota_que_tem.png")
  embed.add_field(name="--ping", value="Para retornar o ping do bot", inline=True)
  embed.add_field(name="--clear <número>", value="Para eleminar um número de mensagens pedidas, só para **Administradores**", inline=True)
  await ctx.send(embed=embed)

@client.command()
async def ajuda(ctx):
  embed=discord.Embed(title="Lista de comandos", url="https://github.com/jp2435/Bota-Bot", description="Lista de comandos que precisas", color=0xc0f03)
  embed.set_author(name="Bota Bot", icon_url="https://cdn.discordapp.com/attachments/790612398070300673/845689775565570058/bota_que_tem.png")
  embed.set_thumbnail(url="https://images.pexels.com/photos/416322/pexels-photo-416322.jpeg")
  embed.add_field(name="--ping", value="Para mostrar o ping do bot", inline=False) 
  embed.add_field(name="--clear", value="Para limpar mensagens, só para Administradores", inline=True)
  embed.add_field(name="Field 3 Title", value="It is inline with Field 2", inline=True)
  embed.set_footer(text="Informação drámatica pedida por: {}".format(ctx.author.display_name))
  await ctx.send(embed=embed)

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