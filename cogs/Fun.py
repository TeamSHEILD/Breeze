import json
from itertools import cycle
import discord
from discord.ext import commands, tasks
import random
from discord.ext.commands.cooldowns import BucketType
from discord.utils import get
from discord.ext import commands
import time
import aiohttp
from discord import Webhook, AsyncWebhookAdapter
import sys, traceback
import asyncio
import aiohttp
import requests
import re
from fake_useragent import UserAgent
import subprocess
import json
import datetime
import shutil
import requests
import random
import ratelimiter
import logging
import sqlite3
import youtube_dl
import os
from os import system
from gtts import gTTS
import urllib.parse
import traceback
#import pendulum
#import pyfiglet
from discord import Spotify
#import dbl

class Fun_Commands(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def meme(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/memes/new.json?sort=top') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=0x3498DB
                    )
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)


    @commands.command()
    async def chatrevive(self, ctx):
        await ctx.message.delete()
        responces = ['Who is your favorate superhero? ', 'Who is the most powerful superhero and why? ', 'What would the perfect weekend be? ', 'What is your favorate video game? ', 'What is your favorate food? ', 'If you could have any car in the world what would it be? ', 'Whats better tiktok or vine? ', 'Whats better console or PC? ', 'What do you prefer online school or being in school? ', 'What is your favorate sport? ', 'Who is your favorate pro player?', 'Dyno, Mee6, or me? (Breeze)', 'Who is the best staff in this server? ', 'Iphone or Android and why? ', 'Xbox or PS? ', 'What is your dream job? ', 'Would you rather live by the beach or the mountians? ', 'Which is better cookies or icecream? ', 'Minecraft or Roblox? ', 'TV show or movies? ', 'Book or movie? ', 'What is your favorate way to pass time? ', 'Whats the most addicting app? ', 'What is the funniest joke you know? ', 'Who is your favorate actor? ', 'What is the strangest dream you have had? ', 'Where is the most beautiful place you have been? ', 'What animal or insect do you wish humans could eradicate and why? ', 'What is the most disgusting habit some people have? ', 'What is the silliest fear you have? ', 'Who is the funniest person you’ve met? ', 'What weird or useless talent do you have? ', 'What’s the most underrated or overrated TV show? ']
        say = random.choice(responces)
        embed = discord.Embed(
            colour=0x3498DB,
            title=f'{say}'
        )
        await ctx.send(embed=embed)

    
    @commands.command()
    async def welcome(self, ctx):
        await ctx.message.delete()
        await ctx.send('<a:Welcome1_Breeze:734860668569911420><a:Welcome2_Breeze:734860759435313226>')


    #@commands.command()
    #async def reddit(self, ctx, *, subreddit):
        #async with aiohttp.ClientSession() as cs:
            #async with cs.get(f'https://www.reddit.com/r/{subreddit}/new.json?sort=top') as r:
                #res = await r.json()
                #embed = discord.Embed(
                    #title=f"Reddit Post From - {subreddit}",
                    #color=0x3498DB
                #)
                #embed.timestamp = datetime.datetime.utcnow()
                #embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                #await ctx.send(embed=embed)
                #print(res)

    @commands.command()
    async def reddit(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.red(),
            title=f':x: Command Being Edited :x:'
        )
        await ctx.send(embed=embed)


    @commands.command()
    async def remind(self, ctx, secs: int, *, reminder):
        minutes = secs * 60
        if secs > 1:

            embed = discord.Embed(
                colour=0x3498DB,
                title=f'Reminder set for {secs} mins from now!'
            )
            await ctx.send(embed=embed)
        if secs == 1:

            minute = discord.Embed(
                colour=0x3498DB,
                title=f'Reminder set for {secs} min from now!'
            )
            await ctx.send(embed=minute)
        await asyncio.sleep(minutes)
        remind_message = discord.Embed(
            colour=0x3498DB,
            title=f'Reminder - {reminder}!'
        )
        await ctx.send(f'{ctx.author.mention}', embed=remind_message)


    @commands.command()
    async def math(self, ctx):

        mem = ctx.author
        
        try:
            problem = str(ctx.message.clean_content.replace(f"{ctx.prefix}math", ""))
            
            #If a problem isn't given
            if problem == "":
                e = discord.Embed(
                    description=f":x: You Need To Put An Actual Problem :x:", 
                    color=discord.Colour.red())
                await ctx.send(embed=e)
                return
            
            #If the user's problem is too long
            if len(problem) > 500:
                e = discord.Embed(
                    description=f":x: That Problem Is Too Long :x:", 
                    color=0x3498DB)
                await ctx.send(embed=e)
                return
              
            problem = problem.replace("÷", "/").replace("x", "*").replace("•", "*").replace("=", "==").replace("π", "3.14159")
            
            #Iterate through a string of invalid
            #Chracters
            for letter in "abcdefghijklmnopqrstuvwxyz\\_`,@~<>?|'\"{}[]":
                
                #If any of those characters are in user's math
                if letter in problem:
                    e = discord.Embed(
                        description=f":x: That Math Problem Has Invalid Characters :x:", 
                        color=discord.Colour.red())
                    await ctx.send(embed=e)
                    return
            #Make embed
            e = discord.Embed(
                timestamp=datetime.datetime.utcnow())

            #Make fields   
            fields = [
                     ("Problem Given", problem, True), 
            
                      ("Answer", 
                      f"{str(round(eval(problem), 4))}", True)
                      ]
            #Add the fields
            for n, v, i in fields:
                e.add_field(
                    name=n, 
                    value=v, 
                    inline=i)
            
            e.set_footer(
                text=mem, 
                icon_url=mem.avatar_url)
            
            #Send embed
            await ctx.send(embed=e)
            
        #If the problem is unsolvable
        except Exception:
            e = discord.Embed(
                description=f":x: Something Went Wrong :x:", 
                color=discord.Colour.red())
            await ctx.send(embed=e)


    @commands.command(aliases=["aboutuser", "about_user", "userinfo", "user_info", "whoisme"])
    async def whois(self, ctx, member: discord.Member = None):
        member = member if member else ctx.author
        embed = discord.Embed(

                colour=member.colour,
                timestamp=ctx.message.created_at

            )

        roles = [role for role in member.roles]

        lenroles = len(roles) - 1

        embed.set_author(name=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar_url)

        embed.add_field(name="User Name", value=member.name, inline=False)
        embed.add_field(name="ID", value=member.id, inline=False)
        embed.add_field(name="Account Created", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name="Member Joined", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name=f"Roles ({lenroles})", value=" ".join(sorted([r.mention for r in member.roles if r != ctx.guild.default_role], reverse=False)), inline=False)
        embed.add_field(name="Top Role", value=member.top_role.mention, inline=False)
        embed.add_field(name="Bot?", value=member.bot, inline=False)

        await ctx.send(embed=embed)



    @commands.command(aliases=["avatar", "useravatar", "userpfp", "profilepicture", "profile_picture"])
    async def pfp(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        embed = discord.Embed(
            title=f"{member}'s Profile Picture",
            colour=member.colour
        )
        embed.set_image(url=member.avatar_url)
        embed.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["confession", "makeconfession", "addconfession"])
    async def confess(self, ctx, *, content: str):
        await ctx.message.delete()
        embed = discord.Embed(
            title="Someone made a confession!",
            colour=0x3498DB
        )
        embed.add_field(name="Confession", value=content)
        print(f'{ctx.author} made a confession! Confession: {content}')
        await ctx.send(embed=embed)


    @commands.command(aliases=["rick", "roll" "getrick", "getricked", "rickastley", "astley"])
    async def rickroll(self, ctx, member: discord.Member):
        member = ctx.author if not member else member
        if member.id == 693661517824131172:
            embed = discord.Embed(
                title=f":x: You cant rick the master rick roller! :x:",
                colour=discord.Colour.red()
        )
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"You just got rick rolled {member.mention}!",
                        file=discord.File(r"/home/container/Pictures and Videos/Get Ricked.mp4"))


    @commands.command(aliases=["bruh"])
    async def facepalm(self, ctx):
        await ctx.send(file=discord.File(
            r"/home/container/Pictures and Videos/Facepalm.mp4"))


    @commands.command(aliases=["basketballgame", "trey", "basket", "mynameistrey"])
    async def basketball(self, ctx):
        await ctx.send(file=discord.File(r"/home/container/Pictures and Videos/Basketball Game.mp4"))


    @commands.command(aliases=["well", "wellno", "noshit", "really"])
    async def wellnoshit(self, ctx):
        await ctx.send(file=discord.File(r"/home/container/Pictures and Videos/Well No Shit.mp4"))


    @commands.command()
    async def dumb(self, ctx):
        await ctx.send(file=discord.File(r"/home/container/Pictures and Videos/Dumb.mp4"))


    @commands.command(aliases=["greatpoint"])
    async def goodpoint(self, ctx):
        await ctx.send(file=discord.File(r"/home/container/Pictures and Videos/GoodPoint.gif"))


    @commands.command(aliases=["cf", "cointoss", "coin_toss", "coin", "coin_flip", "headsortails", "random_coin", "randomcoin"])
    async def coinflip(self, ctx):
        sides = ["**HEADS**", "**TAILS**"]
        randomcoin = random.choice(sides)
        await ctx.send(f"The coin landed on {randomcoin}!")


    @commands.command(aliases=["finddad", "wheredad", "milk", "dadlocator"])
    async def dad(self, ctx):
        embed=discord.Embed(
            title=":x: ERROR DAD NOT FOUND :x:",
            colour=discord.Colour.red()
        )
        await ctx.send(embed=embed)


    @commands.command(name="8ball")
    async def ball(self, ctx, *, message):
        answers = random.choice(["It is certain", "Without a doubt", "You may rely on it", "Yes definitely", "It is decidedly so", "As I see it, yes", "Most likely", "Yes", "Outlook good", "Signs point to yes", "Reply hazy try again", "Better not tell you now", "Ask again later", "Cannot predict now", "Concentrate and ask again", "Don’t count on it", "Outlook not so good", "My sources say no", "Very doubtful", "My reply is no"])
        embed = discord.Embed(
            title=f'{answers}',
            colour=0x3498DB
        )
        await ctx.send(embed=embed)


    @commands.command()
    async def pp(self, ctx):
        member = ctx.author
        if member.id == 693661517824131172:
            await ctx.message.delete()
            embedd = discord.Embed(
                colour=discord.Colour.blue()
            )
            embedd.add_field(name=f"{ctx.author}'s pp size", value="8============D")
            await ctx.send(embed=embedd)
            return
        else:
            pp_sizes = ['8=D', '8===D', '8====D', '8=======D', '8=====D', '8==========D', '8========D', '8==D']
            await ctx.message.delete()
            sizes = random.choice(pp_sizes)
            embed = discord.Embed(
                colour=0x3498DB
            )
            embed.add_field(name=f"{ctx.author}'s pp size", value=sizes)
            await ctx.send(embed=embed)


    @commands.Cog.listener(name='on_message')
    async def hello_mention(self, message):
        if f"Hello <@!709775179303223387>" in message.content:
            embed = discord.Embed(
                colour=0x3498DB,
                title=f'Hello {message.author}!'
            )
            await message.channel.send(embed=embed)


    @commands.Cog.listener(name='on_message')
    async def disboard_bump(self, message):
        if message.content.startswith('!d bump'):
            message_cooldown = commands.CooldownMapping.from_cooldown(1.0, 7200.0, commands.BucketType.user)
            bucket = message_cooldown.get_bucket(message)
            retry_after = bucket.update_rate_limit()
            if retry_after:
                pass
            else:
                await asyncio.sleep(7200)
                embed = discord.Embed(
                    colour=0x3498DB,
                    title=f'The Bump Is Now Available! Do !d bump'
                )
                await message.channel.send(embed=embed)

    @commands.Cog.listener(name='on_message')
    async def noice_message(self, message):
        if message.content.startswith('noice'):
            await message.channel.send('<:Noice_Breeze:734860593424629811>')

    @commands.Cog.listener(name='on_message')
    async def noice_message2(self, message):
        if message.content.startswith('Noice'):
            await message.channel.send('<:Noice_Breeze:734860593424629811>')


    @commands.Cog.listener(name='on_message')
    async def hello_mentionv2(self, message):
        if f"Hello <@!709775179303223387>" in message.content:
            embed = discord.Embed(
                colour=0x3498DB,
                title=f'Hello {message.author}!'
            )
            await message.channel.send(embed=embed)
        

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
    client.add_cog(Fun_Commands(client))