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


class Admin_Commands(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if member == ctx.author:
            noturself = discord.Embed(
                colour=discord.Colour.red(),
                title=f':x: You Cant Ban Yourself Silly :x:'
                )
            await ctx.send(embed=noturself)
            return
        try:
            userbanned = discord.Embed(
                colour=discord.Colour.red()
            )
            userbanned.add_field(name=f"Banned By {ctx.author}", value=f"""Server - {ctx.guild.name}
    Reason For Ban - {reason}""")
            embed = discord.Embed(
                colour=discord.Colour.green(),
                title=f"Banned {member} :airplane:"
            )
            await member.send(embed=userbanned)
            await member.ban(reason=f"Breeze Bot Ban | Banned By {ctx.author.name} | Reason {reason}")
            await ctx.send(embed=embed)
            return
        except discord.Forbidden:
            embed = discord.Embed(
                colour=discord.Colour.green(),
                title=f"Banned {member} :airplane:"
            )
            await member.ban(reason=f"Breeze Bot Ban | Banned By {ctx.author.name} | Reason {reason}")
            await ctx.send(embed=embed)
            return
        else:
            notbanned = discord.Embed(
                colour=discord.Colour.red(),
                title=f':x: Could Not Ban {member} :x:'
            )
            await ctx.send(embed=notbanned)
            return



    @commands.command(aliases=["removeban"])
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def unban(self, ctx, *, memberid: int):
        if memberid == ctx.author.id:
            noturself = discord.Embed(
                colour=discord.Colour.red(),
                title=f':x: You Cant Unban Yourself Silly :x:'
                )
            await ctx.send(embed=noturself)
            return
        user = await self.client.fetch_user(memberid)
        embed = discord.Embed(
            colour=discord.Colour.green(),
            title=f"Unbanned {user} :airplane:"
        )
        await ctx.guild.unban(user)
        await ctx.send(embed=embed)


    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if member == ctx.author:
            noturself = discord.Embed(
                colour=discord.Colour.red(),
                title=f':x: You Cant Kick Yourself Silly :x:'
                )
            await ctx.send(embed=noturself)
            return
        try:
            userkick = discord.Embed(
                colour=discord.Colour.red()
            )
            userkick.add_field(name=f"Kicked By {ctx.author}", value=f"""Server - {ctx.guild.name}
    Reason For Kick - {reason}""")
            kick = discord.Embed(
                title=f"Kicked {member} :airplane:",
                colour=discord.Colour.green()
            )
            await member.send(embed=userkick)
            await member.kick(reason=f"Breeze Bot Kick | Responsible User  {ctx.author.name} | Reason  {reason}")
            await ctx.send(embed=kick)
            return
        except discord.Forbidden:
            embed = discord.Embed(
                colour=discord.Colour.green(),
                title=f"Kicked {member} :airplane:"
            )
            await member.kick(reason=f"Breeze Bot Kick | Kicked By {ctx.author.name} | Reason {reason}")
            await ctx.send(embed=embed)
            return
        else:
            notkicked = discord.Embed(
                colour=discord.Colour.red(),
                title=f':x: Could Not Kick That {member} :x:'
            )
            await ctx.send(embed=notkicked)

        


    @commands.command(aliases=["changeprefix", "prefixchange", "newprefix", "new_prefix"])
    @commands.has_permissions(manage_channels=True)
    async def prefix(self, ctx, prefix):
        embed = discord.Embed(
            title="You did not send a valid prefix!",
            colour=discord.Colour.red()
        )
        if not prefix:
            return await ctx.send(embed=embed)
        if len(prefix) > 7:
            too_long = discord.Embed(
                colour=discord.Colour.red(),
                title=f'That prefix is too long!'
            )
            await ctx.send(embed=too_long)
            return
        list = self.client.cur.execute(f"SELECT * FROM prefix WHERE guild={ctx.guild.id}").fetchall()
        try:
            if list == []:
                prefix_changed1 = discord.Embed(
                title=f"Prefix changed to `{prefix}`",
                colour=0x3498DB
            )
                await ctx.send(embed=prefix_changed1)
                self.client.cur.execute(f"INSERT INTO prefix(guild, prefix) VALUES({ctx.guild.id}, '-')")
                self.client.con.commit()
            else:
                self.client.cur.execute(f"UPDATE prefix SET prefix = '{prefix}' WHERE guild = {ctx.guild.id}")
                self.client.con.commit()
                prefix_changed2 = discord.Embed(
                    title=f"Prefix changed to `{prefix}`",
                    colour=0x3498DB
                )
                await ctx.send(embed=prefix_changed2)
        except Exception as e:
            print(e)



    @commands.command(aliases=["send"])
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def say(self, ctx, channel: discord.TextChannel = None, *, content: str):
        channel = channel if channel else ctx.channel
        await ctx.message.delete()
        await channel.send(content)


    @commands.command(aliases=["clear"])
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def purge(self, ctx, *, amount=5):
        if amount > 10000:
            embed=discord.Embed(
                title=f':x: The Maximum Purge For Maximum Performance Is 10k :x:',
                colour=discord.Colour.red()
            )
            await ctx.send(embed=embed)
        else:
            await ctx.message.delete()
            await ctx.channel.purge(limit=amount)


    @commands.command(aliases=["addrole", "removerole"])
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def role(self, ctx, user: discord.Member, role: discord.Role):
        if role in user.roles:
            await user.remove_roles(role)
        else:
            await user.add_roles(role)
        embed = discord.Embed(
            colour=discord.Colour.green()
        )
        embed.add_field(name="Role being added/removed", value=f"Role being added/removed from {user}")
        await ctx.send(embed=embed)
        


    @commands.command(aliases=["roleall", "giverolleall", "roleeveryone", "everyonerole", "allroleadd", "roleaddall"])
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def allrole(self, ctx, role: discord.Role):
        embed = discord.Embed(
            colour=discord.Colour.green()
        )
        embed.add_field(name="Role being added", value="Role being added to all users (This may take awhile depending on how many people are in this server)")
        await ctx.send(embed=embed)
        guild = ctx.guild
        for member in guild.members:
            await member.add_roles(role)
            


    @commands.command(aliases=["removeroleall", "roleremoveeveryone", "everyoneroleremove", "roleallremove", "roleremoveall"])
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def allroleremove(self, ctx, role: discord.Role):
        embed = discord.Embed(
            colour=discord.Colour.green()
        )
        embed.add_field(name="Role being removed", value="Role being removed from all users (This may take awhile depending on how many people are in this server)")
        guild = ctx.guild
        await ctx.send(embed=embed)
        for member in guild.members:
            await member.remove_roles(role)


    @commands.command(aliases=["moveto", "move_to", "movechannel", "move_channel"])
    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    async def move(self, ctx, member: discord.Member, channel: discord.VoiceChannel):
        await ctx.message.delete()
        await member.move_to(channel, reason=None)


    @commands.command(aliases=['pm'])
    @commands.has_permissions(manage_messages=True)
    async def dm(self, ctx, member: discord.Member, *, text):
        await ctx.message.delete()
        await member.send(f"Message from {ctx.author}: {text}")

    
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
        else:
            raise error
        return

        


def setup(client):
    client.add_cog(Admin_Commands(client))