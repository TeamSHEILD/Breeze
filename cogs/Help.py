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


class Help_Command(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener(name='on_message')
    async def mention_bot_prefix(self, message):
        if "@everyone" in message.content:
            return
        if "@here" in message.content:
            return
        if self.client.user.mentioned_in(message):
            guild = message.guild.id
            prefix = self.client.cur.execute(f"SELECT prefix FROM prefix WHERE guild={guild}").fetchone()[0]
            if prefix is None:
                self.client.cur.execute(f"INSERT INTO prefix(guild, prefix) VALUES({guild}, '-')")
                self.client.con.commit()
                embedd = discord.Embed(
                    colour=0x3498DB,
                    title=f'The Prefix For This Server Is `-`'
                )
                await message.channel.send(embed=embedd)
                return
            else:
                prefix = self.client.cur.execute(f"SELECT prefix FROM prefix WHERE guild={guild}").fetchone()[0]
                embed = discord.Embed(
                    colour=0x3498DB,
                    title=f'The Prefix For This Server Is `{prefix}`'
                )
                await message.channel.send(embed=embed)
                return



    @commands.command(aliases=['pages', 'helpme'])
    async def help(self, ctx):
        member = ctx.author
        embed = discord.Embed(
            colour=0x3498DB,
            title=f'Help Command'
        )
        embed.add_field(name=f'Fun Commands', value=f'`-fun`', inline=True)
        embed.add_field(name=f'Emoji Commands', value=f'`-emojis`', inline=True)
        embed.add_field(name=f'Bot Commands', value=f'`-bot`', inline=True)
        embed.add_field(name=f'Info Commands', value=f'`-info`', inline=True)
        embed.add_field(name=f'Admin Commands', value=f'`-admin`', inline=True)
        embed.add_field(name=f'Bot Developer Commands', value=f'`-botdev`', inline=True)
        embed.set_footer(text="<> - Required | () - Not Required", icon_url=f"{member.avatar_url}")
        await ctx.send(embed=embed)
        
    @commands.command(aliases=['fun_commands', 'funs'])
    async def fun(self, ctx):
        member = ctx.author
        embed = discord.Embed(
            colour=0x3498DB,
            title=f'Fun Commands'
        )
        embed.set_footer(text="<> - Required | () - Not Required", icon_url=f"{member.avatar_url}")
        embed.add_field(name=f'Commands', value=f'`-meme` `-reddit <subreddit>` `-chatrevive` `-remind <mins> <reminder>` `-whois (mention user)` `-pfp (mention user)` `-confess <confession>` `-rick <mention user>` `-facepalm` `-basketball` `-noshit` `-dumb` `-goodpoint` `-coinflip` `-dad` `-8ball <question>` `-pp` `-math <equation>`')
        await ctx.send(embed=embed)

    @commands.command(aliases=['emoji_commands', 'emoji'])
    async def emojis(self, ctx):
        member = ctx.author
        embed = discord.Embed(
            colour=0x3498DB,
            title=f'Emoji Commands'
        )
        embed.set_footer(text="<> - Required | () - Not Required", icon_url=f"{member.avatar_url}")
        embed.add_field(name=f'Commands', value=f'`-skull` `-thinking` `-clown` `-moyai` `-lul` `-shrug` `-thumbsup` `-thumbsdown` `-oof` `-eyes` `-dead` `-boi` `-masspingsock` `-pingsock` `-stonks` `-triggered` `-simp` `-simpspotted` `-youtried` `-mmm` `-breezelogo`')
        await ctx.send(embed=embed)


    @commands.command(aliases=['bot_commands'])
    async def bot(self, ctx):
        member = ctx.author
        embed = discord.Embed(
            colour=0x3498DB,
            title=f'Bot Commands'
        )
        embed.set_footer(text="<> - Required | () - Not Required", icon_url=f"{member.avatar_url}")
        embed.add_field(name=f'Commands', value=f'`-suggest <suggestion>` `-bug <bug>` `-ping` `-vote` `-invite` `-support` `-donate`')
        await ctx.send(embed=embed)


    @commands.command(aliases=['info_commands', 'information'])
    async def info(self, ctx):
        member = ctx.author
        embed = discord.Embed(
            colour=0x3498DB,
            title=f'Info Commands'
        )
        embed.set_footer(text="<> - Required | () - Not Required", icon_url=f"{member.avatar_url}")
        embed.add_field(name=f'Commands', value=f'`-covid` `-about`')
        await ctx.send(embed=embed)


    @commands.command(aliases=['dev_commands', 'developer', 'devs'])
    async def botdev(self, ctx):
        member = ctx.author
        embed = discord.Embed(
            colour=0x3498DB,
            title=f'Dev Commands'
        )
        embed.set_footer(text="<> - Required | () - Not Required", icon_url=f"{member.avatar_url}")
        embed.add_field(name=f'Commands', value=f'`-kill` `-prefixin <guild id>` `-serverprefix <guild id> <new prefix>` `-serverprefixremove <guild id>` `-botleave <guild id>` `-reload <cog>` `-load <cog>` `-unload <cog>`')
        await ctx.send(embed=embed)


    @commands.command(aliases=['admin_commands', 'administartor', 'admins'])
    async def admin(self, ctx):
        member = ctx.author
        embed = discord.Embed(
            colour=0x3498DB,
            title=f'Admin Commands'
        )
        embed.set_footer(text="<> - Required | () - Not Required", icon_url=f"{member.avatar_url}")
        embed.add_field(name=f'Commands', value=f'`-kick <mention user> (reason)` `-ban <mention user> (reason)` `-unban <user id>` `-prefix <new prefix>` `-purge <amount>` `-role <mention user> <mention role>` `-allrole <mention role>` `-allroleremove <mention role>` `-move <channel id> <mention user>` `-say <tag channel> <message>` `-dm <mention user> <message>`')
        await ctx.send(embed=embed)


    async def cog_command_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            embed = discord.Embed(
                title=f':x: You Need To Be In A NSFW Channel :x:'
            )
            await ctx.send(embed=embed)
            return
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
    client.add_cog(Help_Command(client))