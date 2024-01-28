import discord
import json
import lunch_manager
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    lunch_manager.load_menu()
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='mat', help='Visar dagens lunch')
async def mat(ctx):
    await ctx.send(lunch_manager.get_todays_menu())

@bot.command(name='meny', help='Visar veckans meny')
async def meny(ctx):
    await ctx.send(lunch_manager.get_full_menu())

@bot.command(name='måndag', help='Visar måndagens lunch')
async def måndag(ctx):
    await ctx.send(lunch_manager.get_menu('monday'))

@bot.command(name='tisdag', help='Visar tisdagens lunch')
async def tisdag(ctx):
    await ctx.send(lunch_manager.get_menu('tuesday'))

@bot.command(name='onsdag', help='Visar onsdagens lunch')
async def onsdag(ctx):
    await ctx.send(lunch_manager.get_menu('wednesday'))

@bot.command(name='torsdag', help='Visar torsdagens lunch')
async def torsdag(ctx):
    await ctx.send(lunch_manager.get_menu('thursday'))

@bot.command(name='fredag', help='Visar fredagens lunch')
async def fredag(ctx):
    await ctx.send(lunch_manager.get_menu('friday'))

@bot.command(name='uppdatera', help='Uppdaterar menyn')
async def uppdatera(ctx):
    lunch_manager.update_menu()
    await ctx.send('Menyn har uppdaterats')

with open('secrets.json', 'r') as file:
    config = json.load(file)

API_TOKEN = config['api_token']

bot.run(API_TOKEN)
