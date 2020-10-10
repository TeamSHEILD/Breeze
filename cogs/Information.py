import json
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
#import dbl


class Info(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def covid(self, ctx):
        r = requests.get("https://api.covid19api.com/summary")
        e = discord.Embed(title="Covid statistics ")
        r= r.json()["Global"]
        e.add_field(name="New Confirmed Cases", value=r["NewConfirmed"])
        e.add_field(name="New Deaths", value=r["NewDeaths"])
        e.add_field(name="New Recovered", value=r["NewRecovered"])
        e.add_field(name="Total Confirmed", value=r["TotalConfirmed"])
        e.add_field(name="Total Deaths", value=r["TotalDeaths"])
        e.add_field(name="Total Recovered", value=r["TotalRecovered"])
        await ctx.send(embed=e)


    @commands.command(aliases=['about', 'aboutbreeze', 'about_breeze'])
    async def breeze(self, ctx):
        embed = discord.Embed(
            colour=0x3498DB,
            title=f'About Breeze'
        )
        embed.add_field(name=f'First Name', value=f"Breeze's first name was 'Anon Bot'", inline=False)
        embed.add_field(name=f'Made', value=f'Breeze was made on May 12th 2020', inline=False)
        embed.add_field(name=f'First Server', value=f"Breeze's first server was 'The Layer'", inline=False)
        embed.add_field(name=f'Used For', value=f'Breeze was first used for whatever I needed at the time', inline=False)
        embed.add_field(name=f"Breeze's Goal", value=f'Breeze has the goal of being one of the best bots Discord has ever seen', inline=False)
        embed.add_field(name=f'Developers', value=f'Breeze was developed by ItzCook1e#6002 in the early stages of development', inline=False)
        embed.add_field(name=f'Other Info', value=f"Want other info about Breeze? Make a suggestion! We would love to tell you more about Breeze's past!", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def invites(self, ctx):
        totalInvites = 0
        for i in await ctx.guild.invites():
            if i.inviter == ctx.author:
                totalInvites += i.uses
        embed = discord.Embed(
            title=f"You've invited {totalInvites} member{'' if totalInvites == 1 else 's'} to the server!",
            colour=0x3498DB
        )
        await ctx.send(embed=embed)


    async def cog_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title=f':x: You Dont Have The Right Perms :x:',
                colour=discord.Colour.red()
            )
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.BotMissingPermissions):
            missing = discord.Embed(
                title=f':x: I Dont Have The Perms For That :x:',
                colour=discord.Colour.red()
            )
            await ctx.send(embed=missing)
            return
        if isinstance(error, commands.CommandNotFound):
            command = discord.Embed(
                title=f':x: Command Not Found :x:',
                colour=discord.Colour.red()
            )
            await ctx.send(embed=command)
            return
        if isinstance(error, commands.MissingRequiredArgument):
            missingarg = discord.Embed(
                colour = discord.Colour.red(),
                title=f':x: Missing Required Argument :x:'
            )
            await ctx.send(embed=missingarg)
            return



def setup(client):
    client.add_cog(Info(client))