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


class Emoji_Commands(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def noice(self, ctx):
        await ctx.message.delete()
        await ctx.send('<:Noice_Breeze:734860593424629811>')

    @commands.command()
    async def skull(self, ctx):
        await ctx.message.delete()
        await ctx.send(':skull:')

    @commands.command()
    async def moyai(self, ctx):
        await ctx.message.delete()
        await ctx.send(':moyai:')

    @commands.command(aliases=['think'])
    async def thinking(self, ctx):
        await ctx.message.delete()
        await ctx.send(':thinking:')


    @commands.command()
    async def clown(self, ctx):
        await ctx.message.delete()
        await ctx.send(":clown:")

    
    @commands.command()
    async def lul(self, ctx):
        await ctx.message.delete()
        await ctx.send("<:LUL_Breeze:734863024678240297>")


    @commands.command()
    async def shrug(self, ctx):
        await ctx.message.delete()
        await ctx.send(":man_shrugging:")


    @commands.command()
    async def thumbsup(self, ctx):
        await ctx.message.delete()
        await ctx.send(":thumbsup:")


    @commands.command()
    async def thumbsdown(self, ctx):
        await ctx.message.delete()
        await ctx.send(":thumbsdown:")


    @commands.command()
    async def oof(self, ctx):
        await ctx.message.delete()
        await ctx.send("<:Oof_Breeze:736349625316802681>")


    @commands.command(aliases=['wot'])
    async def wut(self, ctx):
        await ctx.message.delete()
        await ctx.send("<:Wut_Breeze:734863153602494496>")


    @commands.command()
    async def eyes(self, ctx):
        await ctx.message.delete()
        await ctx.send("<:Eyes_Breeze:734861121139245061>")


    @commands.command(aliases=["deadchat"])
    async def dead(self, ctx):
        await ctx.message.delete()
        await ctx.send("<:DeadChat_Breeze:734861533690986631>")


    @commands.command()
    async def boi(self, ctx):
        await ctx.message.delete()
        await ctx.send("<a:Boi_Breeze:734863252009386034>")

    
    @commands.command()
    async def masspingsock(self, ctx):
        await ctx.message.delete()
        await ctx.send("<a:MassPingSock_Breeze:734861283173859368>")

    
    @commands.command()
    async def pingsock(self, ctx):
        await ctx.message.delete()
        await ctx.send("<:PingSock_Breeze:734861192983609407>")


    @commands.command()
    async def stonks(self, ctx):
        await ctx.message.delete()
        await ctx.send("<:Stonks_Breeze:734861609025011792>")


    @commands.command()
    async def triggered(self, ctx):
        await ctx.message.delete()
        await ctx.send("<a:DankMemesTriggerd_Breeze:734862686785110250>")


    @commands.command()
    async def simp(self, ctx):
        await ctx.message.delete()
        await ctx.send("<a:PeepoSimp_Breeze:734861881893978193>")


    @commands.command()
    async def youtried(self, ctx):
        await ctx.message.delete()
        await ctx.send("<a:YouTried_Breeze:734861454452326432>")


    @commands.command()
    async def doubt(self, ctx):
        await ctx.message.delete()
        await ctx.send("<:XToDoubt_Breeze:734861049546670092>")


    @commands.command()
    async def breezelogo(self, ctx):
        await ctx.message.delete()
        await ctx.send("<:Breeze:757346179439919244>")

    
    @commands.command()
    async def simpspotted(self, ctx):
        await ctx.message.delete()
        await ctx.send("<a:SimpSpotted_Breeze:734860840934703195>")


    @commands.command()
    async def mmm(self, ctx):
        await ctx.message.delete()
        await ctx.send('<:MmmMmmM_Breeze:734864695076323329>')


    @commands.command()
    async def tos(self, ctx):
        await ctx.message.delete()
        await ctx.send('<:monkaTOS:596577180474146827>')


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
    client.add_cog(Emoji_Commands(client))