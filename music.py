from http import client
from telnetlib import theNULL
import discord
from discord.ext import commands
from discord.ext.commands.core import command
from numpy import append
import youtube_dl
import traceback
from tabulate import TableFormat, tabulate
import time
import multiprocessing
import openai
from openai import openai_object, openai_response
from os import system
import os
import tellopy as Tello



def startup(self, ctx):
    commands = input("Enter a console command: ")
    if commands == "Call_Stack":
        for line in traceback.format_stack():
            print(line.strip())
            return
    if commands == "Processes":
        print(multiprocessing.current_process)

table = [['Song', 'Queued by', 'Duration']]
devs = {'421405605656526848', '511255636789428226'}
stacks = []

async def begin(self, ctx):
    await ctx.send
    

class roles(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def dj(self, ctx):
        await ctx.author.send("no")

class devoptions(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def pdebug(self, ctx, url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format':"bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)
        if ctx.author.id == 421405605656526848:
            await ctx.send("You are: ")
            await ctx.send(ctx.author)
            await ctx.send("You are in the channel:")
            if ctx.author.voice:
                await ctx.send(ctx.author.voice.channel)
                for line in traceback.format_stack():
                    await ctx.send(line.strip())
            else:
                await ctx.send("None")
                await ctx.send("Calling stack...: ")      
        else:
            await ctx.send("You're not a Dev.")
    
    
    @commands.command
    async def ai(self, ctx):
        await ctx.send(openai_object.OpenAIObject(api_version=1))
    
    @commands.command()
    async def debug(self,ctx):
        # if devs.index('421405605656526848', '511255636789428226') == ctx.author.id:
        if ctx.author.id == 421405605656526848 or 511255636789428226:
            await ctx.send("You are: ")
            await ctx.send(ctx.author)
            await ctx.send("You are in the channel:")
            if ctx.author.voice:
                await ctx.send(ctx.author.voice.channel)
            else:
                await ctx.send("None")
            await ctx.send("Calling stack: ")
            for line in traceback.format_stack():
                await ctx.send(line.strip())
        else:
            await ctx.send("You're not a Dev.")
    
    @commands.command()
    async def functions(self, ctx):
        await ctx.send(discord.ext)
        
    
    @commands.command()
    async def processes(self, ctx):
        await ctx.send(multiprocessing.current_process)

    @commands.command()
    async def console_commands():
        startup()


class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        # f = "Hello, ", ctx.author.name
        await ctx.send("Hello,")
        await ctx.send(ctx.author.name)
        if ctx.author.voice is None:
            await ctx.send("Join a voice channel please.")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.send("I've joined the chat. Please use `disconnect once you're done with me.")
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self, ctx):
        # h = "Goodbye, ", ctx.author.name
        await ctx.send("goodbye,")
        await ctx.send(ctx.author.name)
        await ctx.voice_client.disconnect()
    
    '''
    def startup(self, ctx):
        os.system("start /wait cmd /c {cd desktop/greatvaluerythm \n py -3 main.py")
        print("Ran")
        await consolecommands = input("Enter debug commands here: ")
        if consolecommands == "call_stacks":
            for line in traceback.format_stack():
                print(line.strip())
            else:
                print("Invalid command")
                return
        if consolecommands == "quit":
            pass
    '''
    @commands.command()
    async def restart(self, ctx):
        startup(self, ctx)

    @commands.command()
    async def play(self, ctx, url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format':"bestaudio"}
        vc = ctx.voice_client
        
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)
            
            s = ("playing", source read())
            await ctx.send(s)
            # await ctx.send(source)

    @commands.command()
    async def pause(self, ctx):
        await ctx.send("Music is paused.")


        await ctx.voice_client.pause()    @commands.command()
    async def online(self, ctx):
        await ctx.send("Internet is working if this message shows up immediately")
    
    @commands.command()
    async def resume(self, ctx):
        await ctx.send("Music has been resumed.")
        await ctx.voice_client.resume()
    
    @commands.command()
    async def queue(self, ctx):
        await ctx.send(tabulate(table, headers='firstrow'))

    @commands.command()
    async def violence(self, ctx):
        await ctx.send("Don't run this command")

    @commands.command()
    async def go(self, ctx):
       await ctx.send(">go")

def setup(client):
    client.add_cog(music(client))
    client.add_cog(devoptions(client))
    client.add_cog(roles(client))
# Note to self, ctrl+/ comments out whatever is highlighted