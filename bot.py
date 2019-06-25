#! /usr/bin/env python3.6

"""
Made by Isabel Lomas for DISCORD HACK WEEK 2019!

For some reason vscode marks "HACK" as another color than the comment color in python's multiline comments.
"""

from datetime import datetime
import discord
from discord.ext import commands
import json
import requests

c = json.load(open('config.json'))

b = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or('sdow-'), case_insensitive=True, activity=discord.Game(name='Six Degrees of Wikipedia!'))
b.remove_command('help')

@b.command(name='info')
async def i(o):
    e = discord.Embed(color=0x68ceff, description="Made by Isabel#0002", title='About SDoW')
    e.add_field(name='About', value='Six Degrees of Wikipedia (The Discord Bot) is made for Discord Hack Week in 2019.\nThe bot is based off the [Six Degrees of Wikipedia](https://sixdegreesofwikipedia.com) game.', inline=False)
    e.add_field(name='Links', value='[Discord Hack Week](https://discord.gg/hackweek)\n[discord.py](https://github.com/Rapptz/discord.py)\n[GitHub](https://github.com/Mippy/SDOW-Bot)\n[Six Degrees of Wikipedia](https://sixdegreesofwikipedia.com)\n[SDoW GitHub](https://github.com/jwngr/sdow)', inline=False)
    e.set_thumbnail(url='https://raw.githubusercontent.com/wikimedia/portals/master/dev/wikipedia.org/assets/img/Wikipedia-logo-v2.png')
    e.timestamp = datetime.utcnow()
    e.set_footer(text=f'Requested by {o.author} ({o.author.id})')
    await o.send(embed=e)

b.run(c['token'])