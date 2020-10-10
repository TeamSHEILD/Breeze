import json
import os
from itertools import cycle
import discord
from discord.ext import commands, tasks
import random
from discord.ext.commands.cooldowns import BucketType
from discord.utils import get
from discord.ext import commands
import time
from discord import Webhook, AsyncWebhookAdapter
import sys, traceback
import asyncio
import aiohttp
import requests
import re
from fake_useragent import UserAgent
import sqlite3
import ratelimiter
import logging
import youtube_dl
import os
from os import system
from datetime import datetime
from discord.ext import commands
from cogs.Top_Secret import token
#import dbl


# Get Prefix


async def get_prefix(client, message):
  client.cur.execute("CREATE TABLE IF NOT EXISTS prefix(guild INT, prefix TEXT DEFAULT '-')")
  if message.guild is None:
    prefix = "-"
  else:
    prefix = client.cur.execute(f"SELECT prefix FROM prefix WHERE guild = {message.guild.id}").fetchall()
  if prefix == []:
    return "-"
  return prefix[0]


 
# Define Bot

client = commands.AutoShardedBot(command_prefix=get_prefix, owner_ids=[693661517824131172, 327994418240028673], case_insensitive=True)

client.ready = False

client.prefixes = {}

client.remove_command("help")

client.remove_command("define")


# On Ready


client.ready = False

client.prefixes = {}

client.con = sqlite3.connect('prefixes_sqlite.db')

client.cur = client.con.cursor()

status = cycle([f"over {len(client.users)} users!", f"over {len(client.guilds)} servers!", "for commands!", "people win Nitro! (join support server)"])

@tasks.loop(seconds=45)
async def statuschange():
  await client.change_presence(activity = discord.Activity (type = discord.ActivityType.watching, name = f"over {len(client.users)} users!"))
  await asyncio.sleep(45)
  await client.change_presence(activity = discord.Activity (type = discord.ActivityType.watching, name = f"over {len(client.guilds)} servers!"))
  await asyncio.sleep(45)
  await client.change_presence(activity = discord.Activity (type = discord.ActivityType.watching, name = "for commands!"))
  await asyncio.sleep(45)

@tasks.loop(seconds=43200)
async def vote_noti():
  channel = client.get_channel(752299694494973983)
  guild = channel.guild
  role = discord.utils.get(guild.roles, name="Top.gg Vote Notis")
  channel = client.get_channel(752299694494973983)
  embed = discord.Embed(
    colour=discord.Colour.green()
  )
  embed.add_field(name=f'Vote', value=f'Remember To Vote On [Top.gg](https://top.gg/bot/709775179303223387/vote)!')
  await channel.purge(limit=10)
  await channel.send(role.mention, embed=embed)


@client.event
async def on_ready():
  statuschange.start()
  vote_noti.start()
  print("Breeze is now online!")
  print(f"Breeze is in {len(client.guilds)} servers!")
  print(f'Breeze is used by {len(client.users)} users!')
  if len(client.shards) > 1:
    print(f'Breeze is using {len(client.shards)} shards!')
  else:
    print(f'Breeze is using {len(client.shards)} shard!')


client.launch_time = datetime.utcnow()

@client.command()
async def uptime(ctx):
  delta_uptime = datetime.utcnow() - client.launch_time
  hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
  minutes, seconds = divmod(remainder, 60)
  days, hours = divmod(hours, 24)
  embed = discord.Embed(
    title=f'Uptime - {days}d, {hours}h, {minutes}m, {seconds}s',
    colour=0x3498DB
  )
  await ctx.send(embed=embed)

    
# Guild Join/Guild Leave


@client.event
async def on_guild_join(guild):
    print(f"""Someone invited Breeze to their server!
Breeze is now in {len(client.guilds)} servers!
Breeze is now used by {len(client.users)} people!""")
    client.cur.execute(f"INSERT INTO prefix(guild, prefix) VALUES({guild.id}, '-')")
    client.con.commit()
    channel = client.get_channel(758179190192603156)
    embed=discord.Embed(
      colour=0x03498DB,
      title=f'Breeze Joined A Server!'
    )
    embed.add_field(name=f'Server Name', value=guild.name, inline=False)
    embed.add_field(name=f'New Server Count', value=len(client.guilds), inline=False)
    embed.add_field(name=f'New User Count', value=len(client.users), inline=False)
    await channel.send(embed=embed)


@client.event
async def on_guild_remove(guild):
    print(f"""Someone removed Breeze from their server!
Breeze is now in {len(client.guilds)} servers!
{len(client.users)} now use Breeze!""")
    channel = client.get_channel(758179190192603156)
    embed=discord.Embed(
      colour=0x03498DB,
      title=f'Breeze Left A Server!'
    )
    embed.add_field(name=f'Server Name', value=guild.name, inline=False)
    embed.add_field(name=f'New Server Count', value=len(client.guilds), inline=False)
    embed.add_field(name=f'New User Count', value=len(client.users), inline=False)
    await channel.send(embed=embed)
    list = client.cur.execute(f"SELECT * FROM prefix WHERE guild = {guild.id}").fetchall()
    if not list == []:
        client.cur.execute(f"DELETE FROM prefix WHERE guild = {guild.id}")
        client.con.commit()
        return


extentions = ["jishaku", "cogs.Information", "cogs.Admin", "cogs.Bot", "cogs.Emojis", "cogs.Fun", "cogs.Help", "cogs.Hidden", "cogs.Cook1e", "cogs.HCommands", "cogs.Cogs"]


if __name__ == '__main__':
    for extension in extentions:
        client.load_extension(extension)


@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    command = discord.Embed(
      title=f':x: Command Not Found :x:',
      colour=discord.Colour.red()
    )
    await ctx.send(embed=command)
  else:
    raise error


traceback.print_exception


logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


client.run(token)