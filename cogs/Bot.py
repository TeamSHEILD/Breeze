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
import io
from os import system
from cogs.Top_Secret import suggestion_channel
from cogs.Top_Secret import bug_channel
#import dbl


class Bot_Commands(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member, guild=None):
        guild = member.guild
        embed = discord.Embed(
            title="User Joined Breeze HQ",
            colour=discord.Colour.green()
        )
        embed.add_field(name=f"Welcome {member}", value=f"Enjoy your stay at Breeze Headquarters! \rCheck out <#711508121637617766> or <#711508192294862898> for help or you can also chat it up in <#711507824919969816>!")
        embed.add_field(name="Account Created", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.set_thumbnail(url=member.avatar_url)
        if member.guild.id == 711507824919969812:
            role = discord.utils.get(guild.roles, name="Member")
            channel = self.client.get_channel(729477975690707024)
            await member.add_roles(role)
            await channel.send(embed=embed)


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        embed = discord.Embed(
            colour=discord.Colour.red()
        )
        embed.add_field(name=f"{member} left Breeze HQ", value="No cookies for them :x: :cookie: :x:")
        if member.guild.id == 711507824919969812:
            channel = self.client.get_channel(729477975690707024)
            await channel.send(embed=embed)


    @commands.command(aliases=["feedback", "suggestion"])
    async def suggest(self, ctx, *, content):
        await ctx.message.delete()
        embed = discord.Embed(
            colour=discord.Colour.green()
        )
        embed.add_field(name=f"Suggestion From {ctx.author}", value=f"{content}")
        cookie = discord.Embed(
            title=f"Thanks for the sugestion {ctx.author}! Here's a cookie! :cookie:",
            colour=discord.Colour.green()
        )
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(f'{suggestion_channel}', adapter=AsyncWebhookAdapter(session))
            await webhook.send(embed=embed)
            await ctx.send(embed=cookie)

    @commands.command(aliases=["reportbug", "sendbug", "bugreport"])
    async def bug(self, ctx, *, content):
        await ctx.message.delete()
        embed = discord.Embed(
            colour=discord.Colour.green()
        )
        embed.add_field(name=f"Bug Found By {ctx.author}", value=f"{content}")
        cookies = discord.Embed(
            title=f"Thanks for reporting that {ctx.author}! Here's a cookie! :cookie:",
            colour=discord.Colour.green()
        )
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(f'{bug_channel}', adapter=AsyncWebhookAdapter(session))
            await webhook.send(embed=embed)
            await ctx.send(embed=cookies)

    
    @commands.command()
    async def status(self, ctx):
        embed=discord.Embed(
            colour=0x3498DB,
            title=f"Breeze's Status"
        )
        embed.add_field(name=f'Ping', value=f'{round(self.client.latency * 1000)}ms', inline=False)
        embed.add_field(name=f'Number Of Users', value=f'{len(self.client.users)}', inline=False)
        embed.add_field(name=f'Number Of Guilds', value=f'{len(self.client.guilds)}', inline=False)
        embed.add_field(name=f'# Of Commands', value=f'{len(self.client.commands)}', inline=False)

    @commands.command()
    async def test(self, ctx):
        message = ctx.message
        await message.add_reaction('✅')


    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(
            title=f'Websocket: {round(self.client.latency * 1000)}ms',
            colour=discord.Colour.green()
        )
        await ctx.send(embed=embed)
        print(f"Someone requested the ping! The ping was {round(self.client.latency * 1000)}ms!")

    
    @commands.command()
    async def perms(self, ctx):
        embed = discord.Embed(
            title=f'Breeze has these perms in this server - {ctx.guild.me.guild_permissions}'
        )
        await ctx.send(embed=embed)


    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.guild is None:
            if message.author.id != 709775179303223387:
                if message.content.startswith('-'):
                    return
                if message.content.startswith('help'):
                    return
                embed = discord.Embed(
                    colour=0x3498DB
                )
                embed.add_field(name=f"Breeze DM - From {message.author} ({message.author.id})", value=f"{message.content}")
                channel = self.client.get_channel(739005766593151007)
                await channel.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def reply(self, ctx, userid: int, *, text):
        member = self.client.get_user(userid)
        await ctx.message.delete()
        embed = discord.Embed(
            colour=0x3498DB
        )
        embed.add_field(name=f"Responded To User", value=f"{text}")
        channel = self.client.get_channel(739005766593151007)
        await channel.send(embed=embed)
        embed = discord.Embed(
            colour=0x3498DB
        )
        embed.add_field(name=f"Message From Dev - {ctx.author}", value=f"{text}")
        await member.send(embed=embed)
                        
    @commands.command(aliases=["makevote", "makeavote"])
    async def vote(self, ctx):
        embed=discord.Embed(

        )
        embed.add_field(name=f"Vote For Breeze", value=f"[top.gg vote](https://top.gg/bot/709775179303223387/vote)")
        await ctx.send(embed=embed)

    @commands.command(aliases=['embedexample'])
    async def embed(self, ctx):
        embed = discord.Embed(
            title=f'Title',
            colour=0x3498DB,
        )
        embed.add_field(name=f'Field', value=f'Value')
        embed.set_author(name=f'Author Name')
        embed.set_footer(text=f'Footer')


    @commands.command(aliases=["enterqueue", "queueenter"])
    async def queue(self, ctx, *, text):
        embed = discord.Embed(
            title="User Entered The Queue",
            colour=discord.Colour.blue(),

        )

        embed.set_author(name=f"{ctx.author}")
        embed.add_field(name="Server", value=f"{ctx.guild}", inline=False)
        embed.add_field(name="User", value=f"{ctx.author}", inline=False)
        embed.add_field(name="Queue", value=f"{ctx.author} entered the queue!", inline=False)
        embed.add_field(name="Queue Username", value=f"{text}", inline=False)

        await ctx.send(embed=embed)


    @commands.command(aliases=["invitebot"])
    async def invite(self, ctx):
        embed = discord.Embed(

            title="Invite Breeze"
        )
        embed.add_field(name="Invite me to your server!",
                        value="[Invite Link](https://discord.com/api/oauth2/authorize?client_id=709775179303223387&permissions=456649846&scope=bot)")
        await ctx.send(embed=embed)


    @commands.command(aliases=["supportserver", "support_server", "help_server", "helpserver"])
    async def support(self, ctx):
        embed = discord.Embed(

            title="Join our support server!"
        )
        embed.add_field(name="Support Server", value="[Invite Link](https://discord.gg/YNw3bfj)")
        await ctx.send(embed=embed)


    @commands.command(aliases=["dono", "donation", "paypal", "venmo", "cashapp"])
    async def donate(self, ctx):
        embed = discord.Embed(

        )
        embed.add_field(name="Donate", value=f"[Donation Link](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=J67EDSGXA4GAL&source=url)")
        await ctx.send(embed=embed)

    @commands.command()
    async def serverupdates(self, ctx):
        guildid = 711507824919969812
        if ctx.guild.id == guildid:
            member = ctx.author
            guild = ctx.guild
            role = discord.utils.get(guild.roles, name="Server Update Notis")
            if role in member.roles:
                embed = discord.Embed(
                    colour=discord.Colour.green()
                )
                embed.add_field(name="Server Update Notis being removed", value=f"Server Update Notis has been removed from {ctx.author}")
                await member.remove_roles(role)
            else:
                embed = discord.Embed(
                    colour=discord.Colour.green()
                )
                embed.add_field(name="Server Update Notis being added", value=f"Server Update Notis has been added to {ctx.author}")
                await member.add_roles(role)
            await ctx.send(embed=embed)

    @commands.command()
    async def hiddencommands(self, ctx):
        guildid = 711507824919969812
        if ctx.guild.id == guildid:
            member = ctx.author
            guild = ctx.guild
            role = discord.utils.get(guild.roles, name="Hidden Command Updates")
            if role in member.roles:
                embed = discord.Embed(
                    colour=discord.Colour.green()
                )
                embed.add_field(name="Hidden Command Notis being removed", value=f"Hidden Command Notis has been removed from {ctx.author}")
                await member.remove_roles(role)
            else:
                embed = discord.Embed(
                    colour=discord.Colour.green()
                )
                embed.add_field(name="Hidden Command Notis being added", value=f"Hidden Command Notis has been added to {ctx.author}")
                await member.add_roles(role)
            await ctx.send(embed=embed)


    @commands.command()
    async def serverbotpolls(self, ctx):
        guildid = 711507824919969812
        if ctx.guild.id == guildid:
            member = ctx.author
            guild = ctx.guild
            role = discord.utils.get(guild.roles, name="Server/Bot Polls")
            if role in member.roles:
                embed = discord.Embed(
                    colour=discord.Colour.green()
                )
                embed.add_field(name="Server/Bot Polls being removed", value=f"Server/Bot Polls has been removed from {ctx.author}")
                await member.remove_roles(role)
            else:
                embed = discord.Embed(
                    colour=discord.Colour.green()
                )
                embed.add_field(name="Server/Bot Polls being added", value=f"Server/Bot Polls has been added to {ctx.author}")
                await member.add_roles(role)
            await ctx.send(embed=embed)


    @commands.command()
    async def partnershippings(self, ctx):
        guildid = 711507824919969812
        if ctx.guild.id == guildid:
            member = ctx.author
            guild = ctx.guild
            role = discord.utils.get(guild.roles, name="Partnership Pings")
            if role in member.roles:
                embed = discord.Embed(
                    colour=discord.Colour.green()
                )
                embed.add_field(name="Partner Pings being removed", value=f"Partner Pings has been removed from {ctx.author}")
                await member.remove_roles(role)
            else:
                embed = discord.Embed(
                    colour=discord.Colour.green()
                )
                embed.add_field(name="Partner Pings being added", value=f"Partner Pings has been added to {ctx.author}")
                await member.add_roles(role)
            await ctx.send(embed=embed)


    @commands.command()
    async def botupdates(self, ctx):
        guildid = 711507824919969812
        if ctx.guild.id == guildid:
            member = ctx.author
            guild = ctx.guild
            role = discord.utils.get(guild.roles, name="Bot Update Notis")
            if role in member.roles:
                embed = discord.Embed(
                    colour=discord.Colour.green()
                )
                embed.add_field(name="Bot Update Notis being removed", value=f"Bot Update Notis has been removed from {ctx.author}")
                await member.remove_roles(role)
            else:
                embed = discord.Embed(
                    colour=discord.Colour.green()
                )
                embed.add_field(name="Bot Update Notis being added", value=f"Bot Update Notis has been added to {ctx.author}")
                await member.add_roles(role)
            await ctx.send(embed=embed)


    @commands.command()
    async def onlineoffline(self, ctx):
        guildid = 711507824919969812
        if ctx.guild.id == guildid:
            member = ctx.author
            guild = ctx.guild
            role = discord.utils.get(guild.roles, name="Bot Online/Offline Notis")
            if role in member.roles:
                embed = discord.Embed(
                    colour=discord.Colour.green()
                )
                embed.add_field(name="Bot Online/Offline Notis being removed", value=f"Bot Online/Offline Notis has been removed from {ctx.author}")
                await member.remove_roles(role)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    colour=discord.Colour.green()
                )
                embed.add_field(name="Bot Online/Offline Notis being added", value=f"Bot Online/Offline Notis has been added to {ctx.author}")
                await member.add_roles(role)
                await ctx.send(embed=embed)


    @commands.command()
    async def votenotis(self, ctx):
        guildid = 711507824919969812
        if ctx.guild.id == guildid:
            member = ctx.author
            guild = ctx.guild
            role = discord.utils.get(guild.roles, name="Top.gg Vote Notis")
            if role in member.roles:
                embed = discord.Embed(
                    colour=discord.Colour.green()
                )
                embed.add_field(name="Vote Notis being removed", value=f"Vote Notis has been removed from {ctx.author}")
                await member.remove_roles(role)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    colour=discord.Colour.green()
                )
                embed.add_field(name="Vote Notis being added", value=f"Vote Notis has been added to {ctx.author}")
                await member.add_roles(role)
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
    client.add_cog(Bot_Commands(client))