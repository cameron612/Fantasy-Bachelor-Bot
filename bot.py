import os
import discord
from dotenv import load_dotenv, find_dotenv
from discord.ext import commands

from message_generator import MessageGenerator

load_dotenv(find_dotenv())
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

message_generator = MessageGenerator()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    guild = discord.utils.find(lambda g: g.name == GUILD, bot.guilds)
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@bot.event
async def on_member_join(member):
    await message.channel.send(
        f'Hi {member.name}, welcome to Fantasy Bachelor!'
    )

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if 'congrats' in message.content.lower() or 'congratulations' in message.content.lower():
        response = message_generator.get_congrats_message()
        await message.channel.send(response)

    if 'barb' in message.content.lower():
        response = message_generator.get_barb_message()
        await message.channel.send(response)

    await bot.process_commands(message)

@bot.command(name='scoreboard', help='Get scores for every team')
async def scoreboard(context):
    response = message_generator.get_league_standings()
    await context.send(response)

@bot.command(name='team', help='Get scores for just your team')
async def team(context):
    response = message_generator.get_requested_team(message.author)
    await context.send(response)

@bot.command(name='quote', help='History lesson')
async def team(context):
    response = message_generator.get_random_quote()
    await context.send(response)

@bot.command(name='matt', help='Hot pic')
async def team(context):
    response = message_generator.get_matt_pic()
    await context.send(response)

@bot.command(name='source', help='github link')
async def team(context):
    response = message_generator.get_source()
    await context.send(response)

@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise



bot.run(TOKEN)