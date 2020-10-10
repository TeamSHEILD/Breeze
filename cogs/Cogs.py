import json
from itertools import cycle
import discord
from discord.ext import commands, tasks
import random
from discord.ext.commands.cooldowns import BucketType
from discord.utils import get
from discord.ext import commands
import time
import datetime
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


class Cog_Commands(commands.Cog):
    def __init__(self, client):
        self.client = client    
    
    
    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, cog=None):
        try:
            if not cog:
                async with ctx.typing():
                    e = discord.Embed(
                        title="Reloading all cogs!",
                        timestamp=datetime.datetime.utcnow())
                        
                    for ext in os.listdir("/home/container/cogs"):
                        if ext.endswith(".py") and not ext.startswith("_"):
                            try:
                                self.client.unload_extension(f"cogs.{ext[:-3]}")
                                self.client.load_extension(f"cogs.{ext[:-3]}")
                                
                                e.add_field(
                                    name=f"Reloaded: `{ext}`",
                                    value='\uFEFF',
                                    inline=True)

                            except Exception as e:
                                e.add_field(
                                    name=f"Failed to reload ``{ext}``",
                                    value=e,
                                    inline=True)
                                    
                            await asyncio.sleep(0.5)
                    await ctx.send(embed=e)
            else:
                async with ctx.typing():
                
                    e = discord.Embed(
                        title="Reloaded",
                        timestamp=datetime.datetime.utcnow())
                        
                    ext = f"{cog}.py"
                    if not os.path.exists(f"/home/container/cogs/{ext}"):
                        e.add_field(
                            name=f"Failed to reload ``{ext}``",
                            value="This cog doesn't exist",
                            inline=True)

                    elif ext.endswith(".py") and not ext.startswith("_"):
                        try:
                        
                            self.client.unload_extension(f"cogs.{ext[:-3]}")
                            
                            self.client.load_extension(f"cogs.{ext[:-3]}")
                            e.add_field(
                                name=f"Reloaded ``{ext}``",
                                value='\uFEFF',
                                inline=True)
                                
                        except Exception:
                        
                            trace = traceback.format_exc()
                            
                            if len(trace) > 850:
                                length = len(trace) - 850
                                
                                trace = f"```{trace[:850]}``` and **{length}** more words..."
                            
                            else:
                                trace = f"```{trace}```"
                            
                            e.add_field(
                                name=f"Failed to reload ``{ext}``",
                                value=trace,
                                inline=True)
                                
                    await ctx.send(embed=e)
        
        except Exception as e:
            await ctx.send(f'```{e}```')

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, cog=None):
        if not cog:
            async with ctx.typing():
                e = discord.Embed(
                    title="Reloading all cogs",
                    timestamp=datetime.datetime.utcnow())
                for ext in os.listdir("/home/container/cogs"):
                    if ext.endswith(".py") and not ext.startswith("_"):
                        try:
                            self.client.load_extension(f"cogs.{ext[:-3]}")
                            
                            e.add_field(
                                name=f"Reloaded ``{ext}``",
                                value='\uFEFF',
                                inline=True)
                                
                        except Exception as e:
                            e.add_field(
                                name=f"Failed to load in ``{ext}``",
                                value=e,
                                inline=True)
                                
                        await asyncio.sleep(0.5)
                await ctx.send(embed=e)
        else:
            async with ctx.typing():
                e = discord.Embed(
                    title=f"Loading in ``{cog}``",
                    timestamp=datetime.datetime.utcnow())
                    
                ext = f"{cog}.py"
                if not os.path.exists(f"/home/container/cogs/{ext}"):
                    e.add_field(
                        name=f"Failed to load in ``{ext}``", 
                        value="This cog doesn't exist",
                        inline=True)

                elif ext.endswith(".py") and not ext.startswith("_"):
                    try:
                        self.client.load_extension(f"cogs.{ext[:-3]}")
                        
                        e.add_field(
                            name=f"Loaded ``{ext}``",
                            value='\uFEFF',
                            inline=True)
                            
                    except Exception:
                        trace = traceback.format_exc()
                        
                        if len(trace) > 850:
                            length = len(trace) - 850
                            
                            trace = f"```{trace[:850]}``` and **{length}** more words..."
                        
                        else:
                            trace = f"```{trace}```"
                        
                        e.add_field(
                            name=f"Failed to load ``{ext}``",
                            value=trace,
                            inline=True)
                            
                await ctx.send(embed=e)

    @commands.command(
        brief="{Unload a cog}", 
        usage="unload <cog_name>")
    @commands.is_owner()
    async def unload(self, ctx, cog):
        async with ctx.typing():
            e = discord.Embed(
                title=f"Unloading ``{cog}``",
                timestamp=datetime.datetime.utcnow())
                
            ext = f"{cog}.py"
            if not os.path.exists(f"/home/container/cogs/{ext}"):
                e.add_field(
                    name=f"Failed to Unload ``{ext}``",
                    value="This cog doesn't exist",
                    inline=True)

            elif ext.endswith(".py") and not ext.startswith("_"):
                try:
                    self.client.unload_extension(f"cogs.{ext[:-3]}")
                        
                    e.add_field(
                        name=f"Unloaded ``{ext}``",
                        value='\uFEFF',
                        inline=True)
                            
                except Exception:
                    desired_trace = traceback.format_exc()
                        
                    e.add_field(
                        name=f"Failed to reload ``{ext}``",
                        value=desired_trace,
                        inline=True)
                            
            await ctx.send(embed=e)


def setup(client):
    client.add_cog(Cog_Commands(client))