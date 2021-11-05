import discord
from discord.ext import commands
from discord_components import *
import imdb
import json

ia = imdb.IMDb()

def get_prefix(client, message):
    with open('./prefixes.json', 'r') as f:
        prefixes = json.load(f)
    
    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix=get_prefix, help_command=None)
DiscordComponents(client)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='i>help'))
    print('We Are Online Now.')
@client.event
async def on_guild_join(guild):
    with open('./prefixes.json', 'r') as f:
        prefixes = json.load(f)
    
    prefixes[str(guild.id)] = 'i>'
    
    with open('./prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('./prefixes.json', 'r') as f:
        prefixes = json.load(f)
    
    prefixes.pop(str(guild.id))

    with open('./prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_message(msg):
    try:
        if msg.mentions[0] == client.user:
            with open('./prefixes.json', 'r') as f:
                prefixes = json.load(f)
        
            pre = prefixes[str(msg.guild.id)]
            embed = discord.Embed(
                colour = 0x3e3e3e
            )
            embed.add_field(name=None ,value='This Server Prefix Now is `{}`'.format(pre))
            await msg.channel.send(embed=embed)
    except:
        pass
            
    await client.process_commands(msg)

@client.command(name='prefix')
@commands.has_permissions(administrator = True)
async def _prefix(ctx, prefix):
    with open('./prefixes.json', 'r') as f:
        prefixes = json.load(f)
    
    prefixes[str(ctx.guild.id)] = prefix
    
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f)
    
    embed = discord.Embed(
        colour = 0x3e3e3e
    )
    embed.add_field(name=None ,value='This Server Prefix Changed To `{}`'.format(prefix))
    await ctx.send(embed = embed)

@client.command(name='help')
async def _help(ctx):
    embed = discord.Embed(
        name="Help Command",
        colour = 0x2e2e2e
    )
    embed.add_field(
        name = 'change your prefix',
        value = '''
**`prefix`** => `prefix <your prefix>`
        ''',
        inline=False
    )

    embed.add_field(
        name = 'search your movies',
        value='''
**`movie`**, **`MOVIE`**, **`film`**, **`FILM`**, **`series`**, **`SERIES`**, **`tvshow`**, **`TVSHOW`**, **`animation`**, **`ANIMATION`** => <command> <your movie> 
''',
        inline=False
    )
    
    await ctx.send(embed=embed)

@client.command(aliases = ['movie', 'MOVIE', 'film', 'FILM', 'series', 'SERIES', 'tvshow', 'TVSHOW', 'animation', 'ANIMATION'])
async def _movie(ctx, *, name_movie):
    options = []
    result_of_movie = ia.search_movie(name_movie)
    for result in result_of_movie[:10]:
        options.append(
            SelectOption(label = result['title'].title(), value = ia.get_imdbURL(result))
        )
    await ctx.send(
        "Select a Movie:",
        components = [
            Select(
                placeholder="Select Movie",
                options = options
            )
        ]
    )
    interaction = await client.wait_for('select_option')
    await interaction.send(content = f"Your Movie is:\n{interaction.values[0]}")

    
client.run('OTA1OTAxOTgyMzM2ODM5NzIx.YYQ09w.tJPJhqK_RfgnEF17dZwRwIqrE7s')