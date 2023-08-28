import os
import requests

try:
    import discord
    import ssl
    import base64
    import json
    import uuid
    import colorama
    import asyncio
    import random
    import string
    import ctypes
    import datetime
    import time
    import json
    import re
    import aiohttp
    import validators
    import io
    import tempfile
    import openai
    import pytube
    import logging
    from discord import app_commands, Color, Embed, HTTPException
    from discord.ext import commands, tasks
    from discord import ButtonStyle, SelectOption, ui
    from colorama import Fore
    from datetime import datetime
    from itertools import cycle
    from asyncio import sleep
    from bs4 import BeautifulSoup
    from gtts import gTTS
    from urllib.parse import urlencode
    from discord import Embed, Color
    from pytube import Playlist
    from typing import List, Union
except ImportError:
    os.system("pip install discord")
    os.system("pip install ssl")
    os.system("pip install base64")
    os.system("pip install json")
    os.system("pip install uuid")
    os.system("pip install colorama")
    os.system("pip install asyncio")
    os.system("pip install random")
    os.system("pip install string")
    os.system("pip install ctypes")
    os.system("pip install datetime")
    os.system("pip install time")
    os.system("pip install json")
    os.system("pip install re")
    os.system("pip install aiohttp")
    os.system("pip install validators")
    os.system("pip install io")
    os.system("pip install tempfile")
    os.system("pip install openai")
    os.system("pip install pytube")
    os.system("pip install logging")
    os.system("pip install discord.py")
    os.system("pip install colorama")
    os.system("pip install datetime")
    os.system("pip install asyncio")
    os.system("pip install bs4")
    os.system("pip install gTTS")
    os.system("pip install urllib")
    os.system("pip install pytube")
    os.system("pip install typing")
    
    import discord
    import ssl
    import base64
    import json
    import uuid
    import colorama
    import asyncio
    import random
    import string
    import ctypes
    import datetime
    import time
    import json
    import re
    import aiohttp
    import validators
    import io
    import tempfile
    import openai
    import pytube
    import logging
    from discord import app_commands, Color, Embed, HTTPException
    from discord.ext import commands, tasks
    from discord import ButtonStyle, SelectOption, ui
    from colorama import Fore
    from datetime import datetime
    from itertools import cycle
    from asyncio import sleep
    from bs4 import BeautifulSoup
    from gtts import gTTS
    from urllib.parse import urlencode
    from discord import Embed, Color
    from pytube import Playlist
    from typing import List, Union


# Create necessary directories
base_dir = os.path.dirname(os.path.abspath(__file__))
settings_dir = os.path.join(base_dir, "Mad Hatter Settings")
avatars_dir = os.path.join(settings_dir, "Avatars")
tts_audio_dir = os.path.join(settings_dir, "TTS_AUDIO")

for directory in [settings_dir, avatars_dir, tts_audio_dir]:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Fetch proxies from the URL
proxies_url = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all'
response = requests.get(proxies_url)
proxies = response.text

# Create or update files
files_to_create = [
    ('Mad Hatter Settings/settings.json', f"""\
[💰Mad Hatter Settings💰]
[token]: TOKEN HERE
[prefix]: PREFIX HERE
[update]: VERSION HERE
[logchannel]: MODERATOR CHANNEL ID HERE
[sleepseconds]: SLEEP SECONDS HERE
[avatarsleepminutes]: AVATAR CHANGE SLEEP SECONDS HERE
[custompingmsg]: MESSAGE TO REPLY WHEN BOT IS PINGED HERE
[openapikey]: OPEN API KEY FOR CHATGPT HERE
[instagramuser]: IG USERNAME HERE
[instagrampass]: IG PW HERE
[Spotify_Client_ID]: SPOTIFY CLIENT ID HERE
[Spotify_Client_Secret]: SPOTIFY CLIENT SECRET HERE"""
    ),
    ('Mad Hatter Settings/reaction_roles.txt', ''),
    ('Mad Hatter Settings/proxy.txt', proxies),
    ('Mad Hatter Settings/levels.txt', ''),
    ('Mad Hatter Settings/custom_role.txt', ''),
    ('Mad Hatter Settings/8ballresponses.txt', """\
It is certain.
It is decidedly so.
Without a doubt.
Yes, definitely.
You may rely on it.
As I see it, yes.
Most likely.
Outlook good.
Yes.
Signs point to yes.
Reply hazy, try again.
Ask again later.
Better not tell you now.
Cannot predict now.
Concentrate and ask again.
Don't count on it.
My reply is no.
My sources say no.
Outlook not so good.
Very doubtful."""),
    ('Mad Hatter Settings/status.txt', """\
@akwh !
Wonderland :)
Welcome!
Use my slash cmds!"""
    ),
]

for file_path, default_content in files_to_create:
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(default_content)

# Download avatars and save to Avatars directory
avatar_urls = [
    "https://media.discordapp.net/attachments/1007355142221332530/1140525633089306707/avatar5.png?width=207&height=368",
    "https://media.discordapp.net/attachments/1007355142221332530/1140525633512935545/avatar7.png?width=294&height=368",
    "https://media.discordapp.net/attachments/1007355142221332530/1140525633772986428/avatar8.png?width=276&height=368",
    "https://media.discordapp.net/attachments/1007355142221332530/1140525633978499132/avatar9.png?width=368&height=368",
    "https://media.discordapp.net/attachments/1007355142221332530/1140525634330824764/avatar0.png",
    "https://media.discordapp.net/attachments/1007355142221332530/1140525634595070002/avatar4.png?width=294&height=368"
]

for index, avatar_url in enumerate(avatar_urls):
    response = requests.get(avatar_url)
    if response.status_code == 200:
        avatar_filename = os.path.join(avatars_dir, f"avatar{index}.png")
        with open(avatar_filename, "wb") as avatar_file:
            avatar_file.write(response.content)

# Read values from settings.json
file_path = os.path.join(settings_dir, "settings.json")
if os.path.exists(file_path):
    with open(file_path) as f:
        config_lines = f.readlines()

    # Extract values from settings.json
    madhatter_settings = config_lines[0].strip()[1:-1]
    token = config_lines[1].strip().split(": ")[1]
    prefix = config_lines[2].strip().split(": ")[1]
    update = config_lines[3].strip().split(": ")[1]
    logchannel = config_lines[4].strip().split(": ")[1]
    sleepseconds = config_lines[5].strip().split(": ")[1]
    avatarsleepminutes = config_lines[6].strip().split(": ")[1]
    custompingmsg = config_lines[7].strip().split(": ")[1]
    openapikey = config_lines[8].strip().split(": ")[1]
    instagramuser = config_lines[9].strip().split(": ")[1]
    instagrampass = config_lines[10].strip().split(": ")[1]
    Spotify_Client_ID = config_lines[11].strip().split(": ")[1]
    Spotify_Client_Secret = config_lines[12].strip().split(": ")[1]

ssl._create_default_https_context = ssl._create_unverified_context
api = None
REACTION_ROLES_FILE = "Mad Hatter Settings/reaction_roles.txt"
CUSTOM_ROLE_FILE = "Mad Hatter Settings/custom_role.txt"
reaction_roles = {}
custom_role_name = {}
custom_roles = []
strikes = {}
proxies = []
custom_role_name = {}
counting_channel_id = None
count = 0
is_counting = False
highest_count = 0
openai.api_key = openapikey
queue = []  # List to store the queued streams
is_playing = False  # Flag to track if audio is currently playing
SONGS_PER_PAGE = 5
# XP required to level up
XP_PER_LEVEL = 100

# Dictionary to store user data
user_data = {}
levels_file_path = "Mad Hatter Settings/levels.txt"


# Set up the bot
intents = discord.Intents.all()
MadHatter = commands.Bot(command_prefix=prefix, intents=intents)
clear = lambda: os.system('cls')

# Set up avatar changing loop
avatars = [f for f in os.listdir(avatars_dir) if f.startswith("avatar")]
@tasks.loop(minutes=60)
async def change_avatar():
    new_avatar = random.choice(avatars)
    avatar_path = os.path.join(avatars_dir, new_avatar)
    with open(avatar_path, "rb") as f:
        try:
            await MadHatter.user.edit(avatar=f.read())
        except discord.HTTPException as e:
            if e.code == 50035:
                print(f"[ {Fore.RED}X {Fore.RESET}] {Fore.MAGENTA} MAKE THE AVATAR CHANGE LONGER.{Fore.RESET}")


status_file_path = os.path.join(settings_dir, "status.txt")
statuses = []
if os.path.exists(status_file_path):
    with open(status_file_path, 'r', encoding='utf-8') as status_file:
        statuses = [line.strip() for line in status_file.readlines()]

statuscycle = cycle(statuses)

@tasks.loop(seconds=2)
async def change_status():
    await MadHatter.change_presence(activity=discord.Game(next(statuscycle)))

response = requests.get("https://pastebin.com/raw/ubQ93uG7")
if response.status_code == 200:
    welcome_text = response.text


if os.path.exists(CUSTOM_ROLE_FILE):
  with open(CUSTOM_ROLE_FILE, "r") as file:
    for line in file:
      line = line.strip()
      if ":" not in line:
        continue
      booster_id, rolename = line.split(":", 1)
      custom_role_name[int(booster_id)] = rolename

# Load levels from file on bot startup
def load_levels():
    try:
        with open(levels_file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                username, user_id, xp, level, messages, last_message = line.strip().split(":")
                user_data[user_id] = {
                    "username": username,
                    "xp": int(xp),
                    "level": int(level),
                    "messages": int(messages),
                    "last_message": last_message  # Store last message content
                }
    except FileNotFoundError:
        # Create the levels file if not found
        os.makedirs(os.path.dirname(levels_file_path), exist_ok=True)
        with open(levels_file_path, "w") as file:
            pass
 
# Save levels to file on bot shutdown
def save_levels():
    with open(levels_file_path, "w") as file:
        for user_id, data in user_data.items():
            file.write(f"{data['username']}:{user_id}:{data['xp']}:{data['level']}:{data['messages']}:{data['last_message']}\n")

async def level_up(user, channel):
    try:
        user_id = str(user.id)
        user_data[user_id]["xp"] -= XP_PER_LEVEL
        user_data[user_id]["level"] += 1
        
        # Retrieve last message content
        last_message = user_data[user_id]["last_message"]
        
        mention = f"<@{user_id}>"
        
        last_message_url = f"https://discord.com/channels/{channel.guild.id}/{channel.id}/{user_data[user_id]['last_message']}"
        
        embed = discord.Embed(
            title="Level Up!",
            description=f"Congratulations {mention}! You've leveled up to level {user_data[user_id]['level']}!\n\nLast Message: ```{last_message}```",
            color=discord.Color.green()
        )
        
        embed.set_thumbnail(url=user.avatar.url)  # Set user's avatar as thumbnail
        embed.set_author(name=channel.guild.name, icon_url=channel.guild.icon.url)  # Set guild name and icon
        embed.set_footer(text="Requested At", icon_url=MadHatter.user.avatar.url)
        embed.timestamp = datetime.utcnow()  # Set the timestamp to the current time
        
        await channel.send(embed=embed)  # Send the embed to the channel
    except Exception as e:
        print("An error occurred in the level_up function:")
        print(e)

@MadHatter.event
async def on_ready():
    clear()
    print(f"{Fore.MAGENTA}{welcome_text}{Fore.RESET}")
    print(f"                                  		Logged in as: {Fore.GREEN}{MadHatter.user.name}\n		                                {Fore.RESET}Instagram Logged in as: {Fore.GREEN}{instagramuser}{Fore.RESET}")
    
    try:
        synced = await MadHatter.tree.sync()
        print(
            f"{Fore.GREEN}                                  		Synced{Fore.WHITE} {len(synced)} command(s)"
        )
    except Exception as e:
        print(e)
    
    change_status.start()  # Start the status loop when the MadHatter is ready
    change_avatar.start()  # Start the avatar loop when the MadHatter is ready

    


# All OF THE EVENTS ARE DOWN HERE, DO NOT PASTE ANYTHING ABOVE THIS.

@MadHatter.event
async def on_message(message):
    if not message.author.bot:
        user_id = str(message.author.id)
        if user_id not in user_data:
            user_data[user_id] = {
                "username": message.author.name,
                "xp": 0,
                "level": 1,
                "messages": 0,
                "last_message": None  # Initialize last message as None
            }
        
        gained_xp = random.randint(1, 3)  # Random XP between 1 and 5 per message
        user_data[user_id]["xp"] += gained_xp
        user_data[user_id]["messages"] += 1
        user_data[user_id]["last_message"] = message.content  # Store last message content
        
        if user_data[user_id]["xp"] >= XP_PER_LEVEL:
            await level_up(message.author, message.channel)  # Level up if XP threshold is reached
        
        save_levels()  # Update the levels file
    
    if "discord.gg" in message.content and "discord.gg/wFQJ356WF9" not in message.content:
        await message.delete()

        current_time = datetime.now().strftime("%H:%M:%S")

        warning_embed = discord.Embed(
            title="Advertising Warning",
            description=f"Hey {message.author.mention}, please refrain from posting Discord server invites.",
            color=discord.Color.red()
        )
        warning_embed.set_author(name=message.guild.name, icon_url=message.guild.icon.url)
        warning_embed.set_footer(
            text=f"Sent by {MadHatter.user.name} at {current_time}",
            icon_url=MadHatter.user.avatar.url
        )
        await message.channel.send(content=message.author.mention, embed=warning_embed)
    elif "server invite" in message.content:
        current_time = datetime.now().strftime("%H:%M:%S")
        
        server_invite_embed = discord.Embed(
            title="Server Invite Link",
            color=discord.Color.green()
        )
        server_invite_embed.set_author(name=message.guild.name, icon_url=message.guild.icon.url)
        server_invite_embed.set_footer(
            text=f"Sent by {MadHatter.user.name} at {current_time}",
            icon_url=MadHatter.user.avatar.url
        )
        server_invite_embed.add_field(
            name="Current Guild's Server Link",
            value="https://discord.gg/wFQJ356WF9",
            inline=False
        )
        await message.channel.send(embed=server_invite_embed)
    else:
        await MadHatter.process_commands(message)

@MadHatter.event
async def on_role_create(role):
  channel_id = 1094688186493566986  # Channel ID where the embed will be sent

  embed = discord.Embed(
    title="Role Created",
    description=f"The role '{role.name}' has been created.",
    color=discord.Color.green())

  author = role.guild.me
  embed.set_author(name=author.name, icon_url=author.avatar_url)

  embed.set_footer(text="Wonderland💫", icon_url=author.guild.icon_url)

  try:
    channel = await MadHatter.fetch_channel(channel_id)
    await channel.send(embed=embed)
  except discord.HTTPException as e:
    print(f"Failed to send the embed: {e}")
    
@MadHatter.event
async def on_role_delete(role):
  channel_id = 1094688186493566986  # Channel ID where the embed will be sent

  embed = discord.Embed(
    title="Role Deleted",
    description=f"The role '{role.name}' has been deleted.",
    color=discord.Color.red())

  author = role.guild.me
  embed.set_author(name=author.name, icon_url=author.avatar_url)

  embed.set_footer(text="Wonderland💫", icon_url=author.guild.icon_url)

  channel = MadHatter.get_channel(channel_id)
  await channel.send(embed=embed)

snipe_message_content = None
snipe_message_author = None

@MadHatter.event
async def on_message_delete(message):  #Checking if any messages get deleted.
  channelaudit = MadHatter.get_channel(1094688186493566986)
  embed = discord.Embed(
    title=f"{message.author}'s Message was deleted.",
    description=
    f"Deleted Message: {message.content}\nAuthor: {message.author.mention}\nLocation: {message.channel.mention}",
    timestamp=datetime.now(),
    color=discord.Colour.red())
  embed.set_author(name=message.author.name,
                   icon_url=message.author.display_avatar)
  await channelaudit.send(embed=embed)

@MadHatter.event
async def on_message_edit(before, after):
  try:
    channelaudit = MadHatter.get_channel(1094688186493566986)

    # Check if the message edit is not due to link conversion and not made by the bot itself
    if before.content != after.content or before.embeds != after.embeds and before.author != MadHatter.user:
      embed = discord.Embed(
        title=f"{before.author} Edited their message",
        description=
        f"Before: {before.content}\nAfter: {after.content}\nAuthor: {before.author.mention}\nLocation: {before.channel.mention}",
        timestamp=datetime.now(),
        color=discord.Colour.blue())
      embed.set_author(name=after.author.name,
                       icon_url=after.author.display_avatar)
      await channelaudit.send(embed=embed)
  except:
    pass

@MadHatter.event
async def on_guild_channel_create(channel):
  channelaudit = MadHatter.get_channel(1094688186493566986)
  embed = discord.Embed(title=f"Channel {channel.mention} was created",
                        timestamp=datetime.now(),
                        color=discord.Colour.green())

  # Set author information
  author = channel.guild.me  # Assuming the MadHatter is the one sending the message
  async for entry in channel.guild.audit_logs(
      limit=1, action=discord.AuditLogAction.channel_create):
    created_by_user = entry.user
    author = created_by_user
    break  # Only retrieve the first entry

  embed.set_author(name=author.name,
                   icon_url=author.avatar.url or author.default_avatar_url)

  # Set footer information
  embed.set_footer(text="Wonderland💫")

  await channelaudit.send(embed=embed)
  
@MadHatter.event
async def on_guild_channel_delete(channel):
  channelaudit = MadHatter.get_channel(1094688186493566986)
  embed = discord.Embed(title=f"Channel ``{channel.name}`` was deleted",
                        timestamp=datetime.now(),
                        color=discord.Colour.red())

  # Set author information
  author = channel.guild.me  # Assuming the MadHatter is the one sending the message
  async for entry in channel.guild.audit_logs(
      limit=1, action=discord.AuditLogAction.channel_delete):
    deleted_by_user = entry.user
    author = deleted_by_user
    break  # Only retrieve the first entry

  embed.set_author(name=author.name,
                   icon_url=author.avatar.url or author.default_avatar_url)

  # Set footer information
  embed.set_footer(text="Wonderland💫")

  await channelaudit.send(embed=embed)

@MadHatter.event
async def on_user_update(before, after):
  if before.avatar != after.avatar:  # Check if the profile picture has changed
    channel = MadHatter.get_channel(1094688186493566986)
    embed = discord.Embed(
      title=f"User changed profile!",
      description=
      f"Username Before: {before.name}\nUsername After: {after.name}\nDiscrim Before: {before.discriminator}\nDiscrim After: {after.discriminator}",
      timestamp=datetime.now(),
      color=discord.Colour.green())

    if str(after.avatar).endswith(
        '.gif'):  # Check if the new profile picture is animated (GIF)
      embed.set_thumbnail(url=str(after.display_avatar))
    else:
      embed.set_thumbnail(url=after.display_avatar)

    await channel.send(embed=embed)
    
@MadHatter.event
async def on_member_unban(guild, user):
  channel = MadHatter.get_channel(1094688186493566986)
  embed123 = discord.Embed(
    title="Unbanned!",
    description=
    f"**{user}** has been unbanned successfully.\nInside **{guild}**",
    timestamp=datetime.now(),
    color=discord.Colour.green())
  await channel.send(embed=embed123)
  
@MadHatter.event
async def on_user_update(before, after):
  if before.avatar != after.avatar:  # Check if the profile picture has changed
    channel = MadHatter.get_channel(1094688186493566986)
    embed = discord.Embed(
      title=f"User changed profile!",
      description=
      f"Username Before: {before.name}\nUsername After: {after.name}\nDiscrim Before: {before.discriminator}\nDiscrim After: {after.discriminator}",
      timestamp=datetime.now(),
      color=discord.Colour.green())

    if str(after.avatar).endswith(
        '.gif'):  # Check if the new profile picture is animated (GIF)
      embed.set_thumbnail(url=str(after.display_avatar))
    else:
      embed.set_thumbnail(url=after.display_avatar)

    await channel.send(embed=embed)


@MadHatter.event
async def on_member_join(member):
  channel = MadHatter.get_channel(1128750055801757957)
  embed = discord.Embed(
    title=
    f'Welcome to {member.guild.name} <a:6_floatingheart:963808375840337990> \n',
    color=0x9208ea)
  embed.add_field(name="\n𝐌𝐞𝐦𝐛𝐞𝐫", value=f"{member.mention}", inline=False)
  embed.set_thumbnail(url=member.avatar.url)
  embed.add_field(name="\n𝗜𝗗", value=member.id, inline=False)
  creation_date = member.created_at.strftime("%d/%m/%Y %H:%M:%S")
  embed.add_field(name="\n𝗖𝗿𝗲𝗮𝘁𝗶𝗼𝗻 𝗗𝗮𝘁𝗲", value=creation_date, inline=False)
  embed.set_footer(
    text=f'{member.guild.name}',
    icon_url=
    "https://i.pinimg.com/736x/6c/45/b2/6c45b24e8ffc0bc3a1a8d70e8f6c725f.jpg")
  await channel.send(embed=embed)  #Sends a welcome message to #Welcome Channel
  await member.send(
    f"I am Mad Hatter, and welcome {member.mention} to **{member.guild.name}.**\nRemember to use the <#963487085594042368> channel to gain access to the whole server.\nEnjoy your stay at **{member.guild.name}**! <a:6_floatingheart:963808375840337990>"
  )  #DM the member upon arrival to the server.
  await member.send(
    f"||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _https://media.tenor.com/XPvqU-vtvpsAAAAC/alice-in-wonderland-mad-hatter.gif"
  )

@MadHatter.listen("on_message")
async def pingReplier(message):
  sleep_seconds = sleepseconds
  message_to_reply = custompingmsg
  if f'<@{1106995171280814091}>' in str(message.content):
    async with message.channel.typing():
      await asyncio.sleep(0.1)
      msg = await message.reply(message_to_reply, delete_after=2)
      
@MadHatter.listen("on_message")
async def pingReplier(message):
  if f'game' in str(message.content):
    async with message.channel.typing():
      await asyncio.sleep(0.1)
      msg = await message.reply("Can I join in?", delete_after=2)
      
@MadHatter.listen("on_message")
async def pingReplier(message):
  if f'help' in str(message.content):
    async with message.channel.typing():
      await asyncio.sleep(0.1)
      msg = await message.reply(
        "Use my prefix ***/*** to see all commands silly!", delete_after=5)
      
@MadHatter.listen("on_message_delete")
async def on_message_delete(message):
  global snipe_message_content
  global snipe_message_author

  snipe_message_content = message.content
  snipe_message_author = message.author.mention


# Event listener to handle reaction add
@MadHatter.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
  if payload.message_id in reaction_roles:
    reaction_role = reaction_roles[payload.message_id]
    if str(payload.emoji) == reaction_role["emoji"]:
      guild = MadHatter.get_guild(payload.guild_id)
      member = guild.get_member(payload.user_id)
      role = guild.get_role(reaction_role["role_id"])
      await member.add_roles(role)


# Event listener to handle reaction remove
@MadHatter.event
async def on_raw_reaction_remove(payload: discord.RawReactionActionEvent):
  if payload.message_id in reaction_roles:
    reaction_role = reaction_roles[payload.message_id]
    if str(payload.emoji) == reaction_role["emoji"]:
      guild = MadHatter.get_guild(payload.guild_id)
      member = guild.get_member(payload.user_id)
      role = guild.get_role(reaction_role["role_id"])
      await member.remove_roles(role)




  # All OF THE COMMANDS ARE DOWN HERE.

@MadHatter.tree.command(
  name="snipe", description="A command to snipe a recently deleted message.")
async def snipe(interaction: discord.Interaction):
  if snipe_message_content == None:
    await interaction.response.send_message(
      "There is no deleted messages to snipe.")
  else:
    embed = discord.Embed(title="Mad Hatter Sniped!",
                          description=f"**Message**:\n{snipe_message_content}",
                          color=0x9208ea,
                          timestamp=datetime.now())
    embed.set_image(
      url="https://media.tenor.com/KtfhXv5J1UEAAAAM/kill-boys-kill.gif")
    embed.add_field(name=f"Sent by:\n", value=f"{snipe_message_author}")
    embed.set_footer(text=f"Wonderland💫")
    embed.set_author(name=interaction.user,
                     icon_url=interaction.user.avatar.url)
    await interaction.response.send_message(embed=embed)
    
@MadHatter.tree.command(name="tts",
                        description="Send a text-to-speech audio file")
async def tts_command(interaction: discord.Interaction, *, text: str):
  # Generate the text-to-speech audio
  tts = gTTS(text)

  # Create the directory for temporary audio files if it doesn't exist
  temp_dir = "Mad Hatter Settings/TTS_AUDIO"
  os.makedirs(temp_dir, exist_ok=True)

  # Save the audio to a temporary file with the user-provided text as the filename
  temp_filename = f"{temp_dir}/{text.replace(' ', '_')}.mp3"
  tts.save(temp_filename)

  # Send the audio file as a message attachment
  await interaction.channel.send(file=discord.File(temp_filename))

  # Delete the temporary file
  os.remove(temp_filename)
  
@MadHatter.tree.command(name="chatgpt",
                        description="A command to ask GPT 3.5 a question.")
async def chatgpt(interaction: discord.Interaction, question: str):
  response = openai.Completion.create(engine='text-davinci-003',
                                      prompt=question,
                                      max_tokens=100,
                                      n=1,
                                      stop=None,
                                      temperature=0.7)
  await interaction.response.send_message(response.choices[0].text.strip())
  
@MadHatter.tree.command(name="stealemote",
                        description="A command to steal and rename an emoji.")
async def stealemote(interaction: discord.Interaction, emote: str,
                     emote_name: str):
  try:
    emote_url = emote or emote_name
    emote_match = re.match(r"<a?:([a-zA-Z0-9_]+):(\d+)>",
                           emote_url)  # Check if emote_url matches the pattern
    if not emote_match:
      raise Exception("Invalid emote provided")
    original_emote_name = emote_match.group(1)
    emote_id = emote_match.group(2)
    emote_extension = ".gif" if emote.startswith("<a:") else ".png"
    emote_url = f"https://cdn.discordapp.com/emojis/{emote_id}{emote_extension}"
    sanitized_emote_name = sanitize_emote_name(emote_name)

    if not (2 <= len(sanitized_emote_name) <= 32):
      raise Exception(
        "Emote name must be between 2 and 32 characters in length")

    await download_and_upload_emote(interaction.guild, emote_url,
                                    sanitized_emote_name)

    # Get the uploaded custom emoji
    emojis = await interaction.guild.fetch_emojis()
    uploaded_emote = discord.utils.get(emojis, name=sanitized_emote_name)

    # Change the emoji name
    await uploaded_emote.edit(name=sanitized_emote_name)

    # Create a random color for the embed
    embed_color = Color(random.randint(0, 0xFFFFFF))

    # Create the embed and set the color and description
    embed = Embed(color=embed_color)
    embed.description = f"Emote {uploaded_emote} uploaded successfully!"

    # Set the footer with "Wonderland💫" and current date and time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    embed.set_footer(text=f"Wonderland💫 | {current_time}")

    # Set the author to the interaction user with their avatar as the author avatar
    author = interaction.user
    embed.set_author(name=author.name, icon_url=author.avatar.url)

    # Get the channel with the specific ID
    channel = interaction.guild.get_channel(1094688186493566986)

    # Send the embed to the specified channel
    await interaction.response.send_message(content="", embed=embed)

    # Send a response to the interaction user
    await channel.send(content="", embed=embed)
  except Exception as e:
    error_response = f"An error occurred: {str(e)}"
    await interaction.response.send_message(content=error_response)

def sanitize_emote_name(emote_name):
  sanitized_name = "".join(c for c in emote_name if c.isalnum() or c.isspace())
  sanitized_name = sanitized_name[:32]
  return sanitized_name

async def download_and_upload_emote(guild, emote_url, emote_name):
  async with aiohttp.ClientSession() as session:
    async with session.get(emote_url) as response:
      if response.status == 200:
        emote_bytes = await response.read()
        emote = await guild.create_custom_emoji(name=emote_name,
                                                image=emote_bytes)
      else:
        raise Exception("Failed to download the emote")


@MadHatter.tree.command(
    name="timeout",
    description="A command to time out a user for a specified amount of time."
)
async def timeout(interaction: discord.Interaction, member: discord.Member, duration: int):
    timeout_role = discord.utils.get(interaction.guild.roles, name="Timeout")

    if timeout_role is None:
        # Create Timeout Role
        timeout_role = await interaction.guild.create_role(
            name="Timeout",
            color=discord.Color.gold(),
            reason="Timeout role creation"
        )

        # Find Server Booster Role
        booster_role = discord.utils.get(interaction.guild.roles, name="Server Booster")

        if booster_role:
            # Calculate the position of the Timeout role
            timeout_position = booster_role.position - 1
            await timeout_role.edit(position=timeout_position)

    # Remove the role "@.gg/wFQJ356WF9" from the user
    role_to_remove = discord.utils.get(interaction.guild.roles, id=999539519466520659)  # Replace 1234567890 with the actual role ID
    if role_to_remove:
        await member.remove_roles(role_to_remove)

    # Make the channel with ID "963487085594042368" not visible when the user is in timeout
    timeout_channel = interaction.guild.get_channel(963487085594042368)  # Replace 963487085594042368 with the actual channel ID
    if timeout_channel:
        await timeout_channel.set_permissions(timeout_role, view_channel=False)

    # Add Timeout Role
    await member.add_roles(timeout_role)

    # Send initial timeout message as a response to the interaction
    embed = discord.Embed(
        title="Timeout",
        description=f"{member.mention} has been put in timeout for {duration} minute(s).",
        color=discord.Color.orange()
    )
    embed.set_footer(text=f"Wonderland💫")
    embed.timestamp = datetime.now()
    await interaction.response.send_message(embed=embed)

    # Create temporary channel for the user under the category "Jail⛓️"
    category_name = "Jail⛓️"
    category = discord.utils.get(interaction.guild.categories, name=category_name)

    if category is None:
        # Create the category if it doesn't exist
        category = await interaction.guild.create_category(category_name)

    channel_name = f"{member.name} - Jail Cell ⛓️🧑⛓️"
    overwrites = {
        interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),
        member: discord.PermissionOverwrite(read_messages=True, read_message_history=True)
    }
    timeout_channel = await interaction.guild.create_text_channel(channel_name, overwrites=overwrites, category=category)

    # Send violation message to the temporary channel
    violation_message = f"You have violated the terms of service and received a timeout punishment."
    await timeout_channel.send(member.mention + " " + violation_message)

    # Create and send the embed to the temporary channel
    embed = discord.Embed(
        title="Server Rules <:iconic_pastelstars1:963549054481084456>",
        description="Please read and follow these rules to ensure a positive and enjoyable experience in our Discord server.",
        color=discord.Color.orange()
    )
    
    # Add rules as fields in the embed
    embed.add_field(name="1. Be Respectful", value="Treat others with kindness, respect, and consideration. Do not engage in harassment, discrimination, or personal attacks.", inline=False)
    embed.add_field(name="2. No NSFW Content", value="Do not share or post any explicit, adult, or NSFW (Not Safe for Work) content. This includes images, videos, links, or discussions.", inline=False)
    embed.add_field(name="3. Use Appropriate Language", value="Keep the language clean and appropriate. Do not use excessive profanity, offensive slurs, or engage in toxic behavior.", inline=False)
    embed.add_field(name="4. No Spamming or Advertising", value="Do not spam the chat, flood with excessive messages, or promote/advertise external links, products, or services without permission.", inline=False)
    embed.add_field(name="5. Respect Privacy", value="Do not share personal information of others without their consent. Respect the privacy and confidentiality of fellow members.", inline=False)
    embed.add_field(name="6. Follow Discord Terms of Service", value="Abide by the Discord Terms of Service (https://discord.com/terms) and Community Guidelines (https://discord.com/guidelines).", inline=False)
    embed.add_field(name="7. No Trolling or Disruptive Behavior", value="Do not engage in trolling, instigating arguments, or intentionally disrupting the peace and harmony of the server.", inline=False)
    embed.add_field(name="8. No Unauthorized Bots or Self-Bots", value="Do not use or create bots that violate Discord's Terms of Service. Only authorized bots are allowed in the server.", inline=False)
    embed.add_field(name="9. Use Relevant Channels", value="Post messages, media, or discussions in their appropriate channels. Avoid off-topic conversations or discussions in the wrong channels.", inline=False)
    embed.add_field(name="10. Listen to Staff", value="Respect and follow the instructions of server staff members. They are here to ensure a positive and enjoyable experience for everyone.", inline=False)
    embed.add_field(name="11. Report Violations", value="If you witness any rule violations or inappropriate behavior, report it to a staff member through DMs or the designated reporting channel.", inline=False)
    embed.add_field(name="12. No Impersonation", value="Do not impersonate other members, staff, or well-known personalities. Be yourself and maintain authenticity.", inline=False)
    embed.add_field(name="13. No Spoilers", value="Avoid sharing spoilers without proper warning. Respect others' enjoyment of movies, TV shows, books, games, or any other form of media.", inline=False)
    embed.add_field(name="14. Have Fun!", value="Enjoy your time in the server, make friends, participate in activities, and contribute positively to the community.", inline=False)
    
    # Set the footer and image
    embed.set_footer(text=f"You will serve your sentence. | Timeout Duration: {duration} minute(s) ")
    embed.set_image(url="https://i.gifer.com/QsBC.gif")  # Replace with the actual image URL

    await timeout_channel.send(embed=embed)

    # Convert duration from minutes to seconds
    timeout_seconds = duration * 60

    # Wait for the specified duration
    await asyncio.sleep(timeout_seconds)

    # Remove Timeout Role after Duration
    await member.remove_roles(timeout_role)

    # Add the role "@.gg/wFQJ356WF9" back to the user
    role_to_add = discord.utils.get(interaction.guild.roles, id=999539519466520659)  # Replace 1234567890 with the actual role ID
    if role_to_add:
        await member.add_roles(role_to_add)

    # Delete the temporary channel
    await timeout_channel.delete()

    # Delete the jail category if it was created for the timeout
    if category is not None and len(category.channels) == 0:
        await category.delete()

    # Restore visibility of the channel when timeout ends
    if timeout_channel:
        await timeout_channel.set_permissions(timeout_role, view_channel=True)

    # Notify Member after Timeout Ends
    embed = Embed(
        title="Timeout Ended",
        description=f"{member.mention}, your timeout of {duration} minute(s) has ended.",
        color=Color.green()
    )
    embed.set_footer(text="Wonderland💫")
    embed.timestamp = datetime.now()
    await member.send(embed=embed)

@MadHatter.tree.command(
  name="create_webhook",
  description="A command to create a webhook with a custom avatar and name.")
async def create_webhook(interaction: discord.Interaction, name: str,
                         avatar_url: str):
  guild = interaction.guild
  channel_id = 1094688186493566986  # Replace with your desired channel ID
  current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  async with aiohttp.ClientSession() as session:
    async with session.get(avatar_url) as response:
      avatar_data = await response.read()

  webhook = await interaction.channel.create_webhook(name=name,
                                                     avatar=avatar_data)

  # Construct the embed for the specified channel
  embed_channel = discord.Embed(title="Webhook Created",
                                color=discord.Color.green())
  embed_channel.add_field(name="Name", value=name, inline=False)
  embed_channel.add_field(name="Avatar URL", value=avatar_url, inline=False)
  embed_channel.add_field(name="Webhook URL", value=webhook.url, inline=False)
  embed_channel.set_author(name=interaction.user, icon_url=interaction.user.avatar.url)
  embed_channel.set_footer(text=f"Wonderland💫 | {current_time}")

  # Construct the embed for the interaction chat
  embed_interaction = discord.Embed(title="Webhook Created",
                                    color=discord.Color.green())
  embed_interaction.add_field(name="Name", value=name, inline=False)
  embed_interaction.add_field(name="Avatar", value="", inline=False)
  embed_interaction.set_author(name=interaction.user, icon_url=interaction.user.avatar.url)
  embed_interaction.set_image(url=avatar_url)
  embed_interaction.set_footer(text=f"Wonderland💫 | {current_time}")

  # Send the embed as a reply in the interaction chat
  await interaction.response.send_message(embed=embed_interaction)

  # Send the additional embed to the specified channel
  channel = MadHatter.get_channel(channel_id)
  await channel.send(embed=embed_channel)
  
@MadHatter.tree.command(description="To see if I am active, use this command!"
                        )  # To see if the MadHatter is active.
async def hello(interaction: discord.Interaction):
  await interaction.response.send_message(
    f"Hello {interaction.user.mention} I am a new bot in development.",
    ephemeral=True)
  

@MadHatter.tree.command(name="ping",
                        description="Pings Mad Hatter to see if he is online.")
async def ping(interaction: discord.Interaction):
  embed = discord.Embed(
    title="Pong🏓",
    description=
    f"On some shit... Mad Hatter's ping is: **{round(MadHatter.latency * 1000)}ms**",
    color=discord.Colour.green())
  embed.set_image(
    url=
    "https://ultimatedisneymoviemarathon.files.wordpress.com/2013/10/images-alice-wonderland-g1.jpg"
  )
  embed.set_footer(text=f"Requested by {interaction.user}",
                   icon_url=interaction.user.avatar.url)
  await interaction.response.send_message(embed=embed, ephemeral=True)

@MadHatter.tree.command(
  name='sync',
  description='Sync all of new commands to discords api - Owner only'
)  #To resync all commands to discord's api.
async def sync(interaction: discord.Interaction):
  if interaction.user.id == 176217706440294400:
    synced = await MadHatter.tree.sync()
    await interaction.response.send_message(
      f"Synced {len(synced)} command(s)! {interaction.user.mention}")
  else:
    await interaction.response.send_message(
      'You must be the owner to use this command!', ephemeral=True)
    
@MadHatter.tree.command(name="members",
                        description="Displays the member count.")
async def members(interaction: discord.Interaction):
  await interaction.response.send_message(
    f'Currently there are, `{interaction.guild.member_count}` members within **{interaction.guild.name}**.',
    ephemeral=True)
  
@MadHatter.tree.command(
  description="A command to purge 'x' amount of messages.")
async def purge(interaction: discord.Interaction, amount: str):
  deleted = await interaction.channel.purge(limit=int(amount) + 1)
  actual_deleted = len(deleted) - 1
  msg = await interaction.channel.send(f"Purged {actual_deleted} messages.")
  await asyncio.sleep(1)

@MadHatter.tree.command(name="nuke",
                        description="A command to nuke a text channel.")
async def nuke(interaction: discord.Interaction):
  guild = interaction.guild
  channel = interaction.channel

  # Create a new channel with the same name and permissions
  new_channel = await channel.clone(reason="Nuke command")

  # Delete the original channel
  await channel.delete(reason="Nuke command")

  # Send the message to the new channel
  await new_channel.send(f"{new_channel.mention} `Nuked by {interaction.user}`"
                         )

@MadHatter.tree.command(name="lookup",
                        description="Lookup another user's information.")
async def lookup(interaction: discord.Interaction,
                 user: discord.Member = None):
  if user == None:
    user = interaction.user
  rlist = []
  for role in user.roles:
    if role.name != "@everyone":
      rlist.append(role.mention)

    b = ", ".join(rlist)

  embed = discord.Embed(colour=user.color)
  embed.set_author(name=f"Information about - {user}"),
  embed.set_thumbnail(url=user.avatar.url)
  embed.add_field(name='Username:', value=user.display_name, inline=False)
  embed.add_field(name='Discord ID:', value=user.id, inline=False)
  embed.add_field(name='Account creation:',
                  value=user.created_at,
                  inline=False)
  embed.add_field(name='Joined server:', value=user.joined_at, inline=False)
  embed.add_field(name="Bot", value=user.bot, inline=False)
  await interaction.response.send_message(embed=embed, ephemeral=True)
  
@MadHatter.tree.command(
  name="avatar",
  description="A command to get a specified users avatar, or yourself.")
async def avatar(interaction: discord.Interaction,
                 username: discord.Member = None):
  if username == None:
    embed = discord.Embed(
      title="Mad Hatter! [ERROR] ❌",
      description="Please specify a member to get their avatar",
      color=0xe74c3c)
    embed.set_image(url=interaction.user.avatar.url)
    embed.add_field(name=f"\n{interaction.user}'s Avatar", value="")
    embed.set_footer(
      text=f"{interaction.guild.name} | Requested by {interaction.user} ")
    await interaction.response.send_message(embed=embed, ephemeral=True)
  else:
    userAvatarURL = username.avatar.url
    embed = discord.Embed(title='{}\'s Avatar'.format(username.name),
                          color=0x9208ea)
    embed.set_image(url='{}'.format(userAvatarURL))
    embed.set_footer(
      text=f"{interaction.guild.name} | Requested by {interaction.user} ")
    await interaction.response.send_message(embed=embed, ephemeral=True)
    
@MadHatter.tree.command(name="changenick",
                        description="A command to change a users nickname.")
async def change(interaction: discord.Interaction, member: discord.Member,
                 nick: str):
  await member.edit(nick=nick)
  await interaction.response.send_message(
    f"Successfully nicknamed {member} to {nick}", ephemeral=True)
  
@MadHatter.tree.command(
  name="version",
  description="A command to check Mad Hatter's current update.")
async def version(interaction: discord.Interaction):
  await interaction.response.send_message(
    f"I am currently using patch, {update}.")


@MadHatter.tree.command(
  name="circus", description="A command to upload clips to my discord server.")
async def circus(interaction: discord.Interaction, game: str, clipname: str,
                 link: str):
  clipchannel = MadHatter.get_channel(1001905092225675356)
  embed = discord.Embed(color=0x9208ea, timestamp=datetime.now())
  embed.set_author(
    name=f"Successfully clipped, {game}!",
    icon_url="https://media4.giphy.com/media/xT1XGSMV4l7QU3sAzC/giphy.gif")
  embed.set_footer(text=f"Uploader: {interaction.user}")
  await clipchannel.send(
    f"**{clipname}**||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _{link}"
  )
  await clipchannel.send(embed=embed)
  await interaction.response.send_message(
    f"Successfully uploaded a clip!\nGame: **{game}**\nClip Title: **{clipname}**\nUploaded to: **{clipchannel.mention}**",
    ephemeral=True)
  
@MadHatter.tree.command(name="addrole",
                        description="Add a role to another user.")
async def addrole(interaction: discord.Interaction, member: discord.Member,
                  role: discord.Role):
  await member.add_roles(role)
  channel = MadHatter.get_channel(1094688186493566986)
  embed = discord.Embed(
    title="Added a Role!",
    description=f"{member.mention} **was given:** {role.mention}",
    timestamp=datetime.now(),
    color=discord.Colour.green())
  embed.set_author(name=interaction.user, icon_url=interaction.user.avatar.url)
  embed.set_footer(text="Wonderland💫")
  await interaction.response.send_message(embed=embed)
  await channel.send(embed=embed)
  
@MadHatter.tree.command(name="removerole",
                        description="Remove a role to another user.")
async def addrole(interaction: discord.Interaction, member: discord.Member,
                  role: discord.Role):
  await member.remove_roles(role)
  channel = MadHatter.get_channel(1094688186493566986)
  embed = discord.Embed(
    title="Removed a Role!",
    description=f"{member.mention} **lost the role:** {role.mention}",
    timestamp=datetime.now(),
    color=discord.Colour.red())
  embed.set_author(name=interaction.user, icon_url=interaction.user.avatar.url)
  embed.set_footer(text="Wonderland💫")
  await interaction.response.send_message(embed=embed)
  await channel.send(embed=embed)

@MadHatter.tree.command(name="ban",
                        description="A command to ban another user.")
async def ban(interaction: discord.Interaction, member: discord.Member,
              reason: str, duration: str, delete_messages: int):
  await member.send(
    f"Do not direct message <@176217706440294400> for a ban appeal, cry your heart out to his moderators so you get pity."
  )

  # Delete Messages
  if delete_messages > 0:
    await interaction.channel.purge(limit=delete_messages,
                                    check=lambda m: m.author == member)

  embed = discord.Embed(
    title="Banned!",
    description=
    f"**User:** {member.mention}\n**Reason:** {reason}\n**Duration:** {duration}",
    timestamp=datetime.now(),
    color=discord.Colour.red())
  embed.set_author(name=interaction.user, icon_url=interaction.user.avatar.url)
  embed.set_footer(text="Wonderland💫")
  await interaction.response.send_message(embed=embed)

  embed = discord.Embed(
    title="You have been banned!",
    description=
    f"***Reason:*** ```{reason}```\n***Guild:*** ```{interaction.guild.name}```\n***Banned by:*** ```{interaction.user}```\n***Duration:*** ```{duration}```",
    timestamp=datetime.now(),
    color=discord.Colour.green())
  embed.set_author(name=f"You have violated our TOS.",
                   icon_url=interaction.user.avatar.url)
  await member.send(embed=embed)
  await interaction.guild.ban(member, reason=f"{reason}")
  
@MadHatter.tree.command(
  name="unban", description="A command to unban another user (use their ID)")
async def unban(interaction: discord.Interaction, userid: str, reason: str):
  guild = interaction.guild
  user = discord.Object(id=userid)
  await guild.unban(user=user, reason=reason)
  unbanembed = discord.Embed(
    title=f"Unbanned!",
    description=f"**User:** <@{userid}>\n**Reason:** {reason}",
    timestamp=datetime.now(),
    color=discord.Colour.green())
  unbanembed.set_author(name=interaction.user,
                        icon_url=interaction.user.avatar.url)
  unbanembed.set_footer(text="Wonderland💫")
  await interaction.response.send_message(embed=unbanembed)

@MadHatter.tree.command(name="coinflip",
                        description="A command to flip a coin.")
async def coinflip(interaction: discord.Interaction):
  n = random.randint(0, 1)
  embed = discord.Embed(title="Coinflip", color=0x9208ea)
  embed.add_field(name="`What shall it be?`", value="", inline=False)
  embed.set_thumbnail(
    url="https://media.tenor.com/bd3puNXKLwUAAAAC/coin-toss.gif")
  embed.set_footer(text=f"Wonderland | Requested by {interaction.user}")
  message = await interaction.channel.send(embed=embed)

  await asyncio.sleep(1.5)

  new_embed = discord.Embed(title="Coinflip", color=0x9208ea)
  new_embed.add_field(
    name="`What shall it be?`",
    value=f"Result: {'**Heads**' if n == 1 else '**Tails**'}")
  new_embed.set_thumbnail(
    url="https://media.tenor.com/bd3puNXKLwUAAAAC/coin-toss.gif")
  new_embed.set_footer(text=f"Wonderland | Requested by {interaction.user}")

  await message.edit(embed=new_embed
                     )  # Update the original message with the new embed
  

@MadHatter.tree.command(
  name="blunt", description="A command to pass a blunt to another user.")
async def blunt(interaction: discord.Interaction, user: discord.Member = None):
  if user is None:
    embed = discord.Embed(
      title="The Blunt Rotation",
      description="You got no friends? or are you a lone wolf.",
      color=0x2ecc71,
      timestamp=datetime.now())
    embed.add_field(name=f"There is no one to pass to...",
                    value="Maybe, you should take another hit.")
    embed.set_image(
      url="https://i.kym-cdn.com/photos/images/facebook/002/410/683/01d.jpg")
    embed.set_footer(text=f"Wonderland💫")
    await interaction.response.send_message(embed=embed)
  else:
    embed = discord.Embed(title=f"The Blunt Rotation",
                          description="",
                          color=0x2ecc71,
                          timestamp=datetime.now())
    embed.add_field(name=f"{interaction.user} Passed to:",
                    value=f"{user.mention} It's your turn to take a toke.")
    embed.set_image(
      url=
      "https://media.tenor.com/DWU1rRs2tZ8AAAAd/pass-the-joint-wiz-khalifa.gif"
    )
    embed.set_footer(text=f"Wonderland💫")
    await interaction.response.send_message(embed=embed)
    

@MadHatter.tree.command(
  name="customrole",
  description="A command for boosters to create a custom role.")
async def customrole(interaction: discord.Interaction, rolename: str,
                     rolecolor: str):
  booster_id = interaction.user.id

  # Check if user already has a custom role
  with open(CUSTOM_ROLE_FILE, "r") as file:
    for line in file:
      line = line.strip()
      if ":" not in line:
        continue
      user_id, _ = line.split(":", 1)
      if int(user_id) == booster_id:
        await interaction.response.send_message(
          "You have already created a custom role.")
        return

  guild = interaction.guild
  existing_role = discord.utils.get(guild.roles, name=rolename)
  if existing_role:
    await interaction.response.send_message(
      "A role with that name already exists.")
  else:
    new_role = await guild.create_role(name=rolename,
                                       color=discord.Color(int(rolecolor, 16)))

    # Find the position of the role given to server boosters
    server_booster_role = discord.utils.get(guild.roles, name="Server Booster")
    if server_booster_role:
      position = server_booster_role.position
      await new_role.edit(position=position)
    else:
      # If "Server Booster" role doesn't exist, place the new role at the bottom
      position = len(guild.roles)
      await new_role.edit(position=position)

    await interaction.user.add_roles(new_role)
    await interaction.response.send_message(
      f"Created and assigned the role {new_role.mention} to {interaction.user.mention}."
    )

    # Save custom role to file
    with open(CUSTOM_ROLE_FILE, "a") as file:
      file.write(f"{booster_id}:{rolename}\n")
      
@MadHatter.tree.command(
  name="deletecustomrole",
  description="A command for boosters to delete their custom role.")
async def deletecustomrole(interaction: discord.Interaction):
  booster_id = interaction.user.id
  found = False
  with open(CUSTOM_ROLE_FILE, "r") as file:
    lines = file.readlines()

  with open(CUSTOM_ROLE_FILE, "w") as file:
    for line in lines:
      line = line.strip()
      if ":" not in line:
        continue
      user_id, rolename = line.split(":", 1)
      if int(user_id) == booster_id:
        found = True
        guild = interaction.guild
        custom_role = discord.utils.get(guild.roles, name=rolename)
        if custom_role:
          await interaction.user.remove_roles(custom_role)
          await custom_role.delete()
          await interaction.response.send_message(
            "Your custom role has been deleted.")
        else:
          await interaction.response.send_message(
            "Your custom role doesn't exist.")
      else:
        file.write(f"{user_id}:{rolename}\n")

  if not found:
    await interaction.response.send_message(
      "You haven't created a custom role.")
   
    
@MadHatter.tree.command(
  name="8-ball", description="A command to ask MadHatter's 8-Ball a question.")
async def eightball(interaction: discord.Interaction, question: str):
  # Construct the file path
  base_dir = os.path.dirname(os.path.abspath(__file__))
  settings_dir = os.path.join(base_dir, "Mad Hatter Settings")
  file_path = os.path.join(settings_dir, "8ballresponses.txt")

  # Read the responses from the text file
  with open(file_path, "r") as file:
    responses = file.read().splitlines()

  # Randomly select a response
  response = random.choice(responses)

  # Randomly choose a color
  color = Color.random()
  # Create an embed with Alice in Wonderland theme
  embed = Embed(
    title="🔮  8-Ball",
    description=f"**Question:** {question}\n\n**Answer:** {response}",
    color=color)
  embed.set_author(
    name="Mad Hatter's 8-Ball",
    icon_url=
    "https://static.wikia.nocookie.net/disneyheroesbattlemode/images/8/87/Disney_heroes_battle_mode_mad_hatter.png/revision/latest?cb=20190425210729"
  )
  embed.set_thumbnail(
    url="https://media.tenor.com/SjdVQ6k3s2gAAAAC/alice-in-wonderland-amaze.gif"
  )

  await interaction.response.send_message(embed=embed)
  

@MadHatter.tree.command()
async def pinmessage(interaction: discord.Interaction, message_link: str):
  try:
    message_id = int(message_link.split('/')[-1])
  except (ValueError, IndexError):
    await interaction.response.send_message("Invalid message link.")
    return

  channel = interaction.channel
  message = await channel.fetch_message(message_id)
  if message is None:
    await interaction.response.send_message("Message not found.")
    return

  target_channel = MadHatter.get_channel(967137851399606352)
  if target_channel is None:
    await interaction.response.send_message("Invalid target channel ID.")
    return

  try:
    await message.pin()

    # Generate random color for the embed
    color = discord.Color(random.randint(0, 0xFFFFFF))

    embed = discord.Embed(description=message.content, color=color)
    embed.set_author(name=f"Pinned {message.author.display_name}'s message:",
                     icon_url=message.author.avatar.url)

    if message.attachments:
      # Assuming only one image is attached to the message
      embed.set_image(url=message.attachments[0].url)

    timestamp = message.created_at.strftime("%Y-%m-%d %H:%M:%S")
    embed.set_footer(text=f"Wonderland💫 | {timestamp}")

    await target_channel.send(embed=embed)
    await interaction.response.send_message("Message pinned")
  except discord.Forbidden:
    await interaction.response.send_message(
      "I don't have permission to pin messages or send messages to the target channel."
    )
    
@MadHatter.tree.command()
async def skin(ctx: discord.Interaction, username: str):
  username = ctx.data["options"][0]["value"]
  response = requests.get(f'https://api.ashcon.app/mojang/v2/user/{username}')

  if response.status_code == 200:
    data = response.json()
    skin_url = data["textures"]["skin"]["url"]
    head_url = f"https://mc-heads.net/head/{username}"

    embed = discord.Embed(title=f"", color=0x00ff00)
    embed.set_image(url=skin_url)
    embed.set_author(name=f"Minecraft Skin for {username}", icon_url=head_url)

    await ctx.response.send_message(embed=embed)
  else:
    await ctx.response.send_message(
      content=f"Failed to retrieve skin for {username}")

@MadHatter.tree.command(name="minecraftlookup")
async def minecraft_info(ctx: discord.Interaction, username: str):
  username = ctx.data["options"][0]["value"]
  response = requests.get(f'https://api.ashcon.app/mojang/v2/user/{username}')

  if response.status_code == 200:
    data = response.json()
    uuid = data["uuid"]
    username = data["username"]
    skin_url = f'https://api.ashcon.app/mojang/v2/user/{username}'

    embed = discord.Embed(title=f"Minecraft Player Information",
                          color=0x00ff00)
    embed.add_field(name="Username", value=username, inline=False)
    embed.add_field(name="UUID", value=uuid, inline=False)
    embed.set_thumbnail(url=skin_url)

    if "created_at" in data:
      created_at = data["created_at"]
      if created_at is not None and len(created_at) > 10:
        created_at = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%fZ")
        created_at = created_at.strftime("%Y-%m-%d %H:%M:%S UTC")
      elif created_at is not None:
        created_at = datetime.strptime(created_at, "%Y-%m-%d")
        created_at = created_at.strftime("%Y-%m-%d")
      else:
        created_at = "Unknown"

      embed.add_field(name="Account Created", value=created_at, inline=False)

    await ctx.response.send_message(embed=embed)
  else:
    await ctx.response.send_message(
      content=f"Failed to retrieve information for {username}")
    
@MadHatter.tree.command(name="songartwork",
                        description="Get the album artwork of a song")
async def song_artwork_command(interaction: discord.Interaction, *,
                               song_title: str):
  # Spotify API credentials
  client_id = Spotify_Client_ID
  client_secret = Spotify_Client_Secret

  # Base64 encode the client ID and client secret
  credentials = base64.b64encode(
    f'{client_id}:{client_secret}'.encode('ascii')).decode('ascii')

  # Make a POST request to get the access token
  auth_url = 'https://accounts.spotify.com/api/token'
  headers = {'Authorization': f'Basic {credentials}'}
  data = {'grant_type': 'client_credentials'}
  response = requests.post(auth_url, headers=headers, data=data)

  if response.status_code == 200:
    # Extract the access token from the response
    access_token = response.json()['access_token']

    # Make a GET request to search for the song
    search_url = f'https://api.spotify.com/v1/search?q={song_title}&type=track&limit=1'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(search_url, headers=headers)

    if response.status_code == 200:
      data = response.json()

      if 'tracks' in data and 'items' in data['tracks'] and len(
          data['tracks']['items']) > 0:
        track = data['tracks']['items'][0]
        album_name = track['album']['name']
        album_artwork_url = track['album']['images'][0]['url']
        album_url = track['album']['external_urls']['spotify']
        song_artwork_url = track['album']['images'][1]['url']

        # Create and send an embed with the song and album artwork
        embed = discord.Embed(title=album_name,
                              url=album_url,
                              color=random.choice([
                                discord.Color.blue(),
                                discord.Color.green(),
                                discord.Color.red(),
                                discord.Color.orange()
                              ]))
        embed.set_image(url=song_artwork_url)
        embed.set_footer(text=f"{interaction.guild.name}")
        embed.set_author(name=interaction.user.name,
                         icon_url=interaction.user.avatar.url)
        embed.timestamp = datetime.now()

        # Create a view and add the button to it
        view = discord.ui.View()
        view.add_item(
          discord.ui.Button(style=discord.ButtonStyle.link,
                            url=album_artwork_url,
                            label="View Album Artwork"))

        await interaction.channel.send(embed=embed, view=view)
      else:
        await interaction.channel.send(
          "Sorry, I couldn't find the album artwork for that song.")
    else:
      await interaction.channel.send(
        "An error occurred while searching for the song.")
  else:
    await interaction.channel.send("Failed to authenticate with Spotify.")
    
@MadHatter.tree.command(name="playlistinfo",
                        description="Get information about a Spotify playlist")
async def playlist_info_command(interaction: discord.Interaction,
                                playlist_link: str):
  # Spotify API credentials
  client_id = Spotify_Client_ID
  client_secret = Spotify_Client_Secret

  # Get Spotify access token
  credentials = base64.b64encode(
    f"{client_id}:{client_secret}".encode()).decode()
  headers = {
    "Authorization": f"Basic {credentials}",
  }
  data = {
    "grant_type": "client_credentials",
  }
  response = requests.post("https://accounts.spotify.com/api/token",
                           headers=headers,
                           data=data)
  token_data = response.json()
  access_token = token_data.get("access_token")

  if access_token:
    # Extract the playlist ID from the link
    playlist_id = playlist_link.split("/")[-1]

    # Make a request to the Spotify API to get information about the playlist
    api_url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(api_url, headers=headers)
    data = response.json()

    # Check if the API request was successful and the playlist was found
    if response.status_code == 200:
      playlist_name = data["name"]
      playlist_owner = data["owner"]["display_name"]
      playlist_owner_url = data["owner"]["external_urls"]["spotify"]
      playlist_description = data["description"]
      playlist_tracks = data["tracks"]["total"]
      playlist_url = data["external_urls"]["spotify"]
      playlist_image = data["images"][0]["url"]
      playlist_collaborators = data.get("collaborative", [])

      # Check if the playlist has collaborators
      if isinstance(playlist_collaborators, list):
        playlist_collaborators = [
          collaborator["display_name"]
          for collaborator in playlist_collaborators
        ]
      else:
        playlist_collaborators = []

      # Create and send an embed with the playlist information
      embed = discord.Embed(title=playlist_name,
                            description=playlist_description,
                            url=playlist_url)
      embed.set_author(name=f"Created by: {playlist_owner}",
                       url=playlist_owner_url)
      embed.add_field(name="Total Tracks", value=playlist_tracks)
      embed.set_image(url=playlist_image)
      embed.color = discord.Color(random.randint(0, 0xFFFFFF))
      embed.set_footer(text=interaction.guild.name,
                       icon_url=interaction.guild.icon.url)
      await interaction.channel.send(embed=embed)
    else:
      await interaction.channel.send(
        "Sorry, I couldn't find information about that playlist.")
  else:
    await interaction.channel.send(
      "Sorry, failed to authenticate with the Spotify API.")
    

@MadHatter.tree.command(name="reactionroles",
                        description="Set reaction roles for a message")
async def reaction_roles_command(interaction: discord.Interaction, emoji: str,
                                 message_link: str, role: discord.Role):
  # Extract the message ID from the message link
  message_id = int(message_link.split("/")[-1])

  try:
    # Fetch the message using the message ID
    message = await interaction.channel.fetch_message(message_id)
  except discord.NotFound:
    await interaction.channel.send("Invalid message link.")
    return

  # Add the reaction role
  try:
    await message.add_reaction(emoji)
    await interaction.channel.send(
      f"Reaction role set for {emoji} on message {message_link}.\n"
      f"Users who react with {emoji} will be given the {role.mention} role.")

    # Store the reaction role data in the dictionary
    reaction_roles[message_id] = {"emoji": emoji, "role_id": role.id}

    # Save the reaction role data to the file
    save_reaction_roles()

  except discord.HTTPException:
    await interaction.channel.send(
      "Failed to add the reaction role. Please make sure the emoji is valid.")
    
# Load the reaction role data from the file on bot startup
def load_reaction_roles():
  if not os.path.isfile(REACTION_ROLES_FILE):
    # Create an empty file if it doesn't exist
    with open(REACTION_ROLES_FILE, "w") as file:
      pass

  try:
    with open(REACTION_ROLES_FILE, "r") as file:
      data = file.read()
      if data:
        global reaction_roles
        reaction_roles = eval(data)
  except FileNotFoundError:
    pass


# Save the reaction role data to the file
def save_reaction_roles():
  with open(REACTION_ROLES_FILE, "w") as file:
    file.write(repr(reaction_roles))
    

@MadHatter.tree.command()
async def send_reset(interaction: discord.Interaction, email: str):
    head = {
        "user-agent": f"Instagram 150.0.0.0.000 Android (29/10; 300dpi; 720x1440; {''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}/{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}; en_GB;)"
    }
    data = {
        "_csrftoken": "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=32)),
        "user_email": email,
        "guid": uuid.uuid4(),
        "device_id": uuid.uuid4()
    }
    thumbnail_url = "https://images-ext-2.discordapp.net/external/nIuNzX4Kzn-kVvICbRVB3fKg7JBMXFEHkBgLUtK2mVw/https/i.pinimg.com/originals/f0/50/68/f0506872304938bac12ea31c78df9156.gif"
    try:
        req = requests.post("https://i.instagram.com/api/v1/accounts/send_password_reset/", headers=head, data=data)
        if 'Please wait a few minutes before you try again.' in req.text:
            embed = discord.Embed(title="Error", description="Error sending reset. Please try again later.", color=discord.Color.red())
            embed.set_thumbnail(url=thumbnail_url)
            embed.set_author(name=f"{interaction.user.name} - Instagram Bot", icon_url=interaction.user.avatar.url)
            embed.set_footer(text="Wonderland💫 | " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            await interaction.response.send_message(embed=embed)
        elif 'obfuscated_email' in req.text:
            embed = discord.Embed(title="Success", description="Reset link sent.", color=discord.Color.green())
            embed.set_thumbnail(url=thumbnail_url)
            embed.set_author(name=f"{interaction.user.name} - Instagram Bot", icon_url=interaction.user.avatar.url)
            embed.add_field(name="Username", value=f"[{email}](https://www.instagram.com/{email})", inline=False)
            embed.set_footer(text="Wonderland💫 | " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            await interaction.response.send_message(embed=embed)
        else:
            embed = discord.Embed(title="Unknown Error", color=discord.Color.dark_grey())
            embed.set_thumbnail(url=thumbnail_url)
            embed.set_author(name=f"{interaction.user.name} - Instagram Bot", icon_url=interaction.user.avatar.url)
            embed.set_footer(text="Wonderland💫 | " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            await interaction.response.send_message(embed=embed)
    except requests.exceptions.RequestException:
        embed = discord.Embed(title="Error", description="Error sending request.", color=discord.Color.red())
        embed.set_thumbnail(url=thumbnail_url)
        embed.set_author(name=f"{interaction.user.name} - Instagram Bot", icon_url=interaction.user.avatar.url)
        embed.set_footer(text="Wonderland💫 | " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        await interaction.response.send_message(embed=embed)
        
@MadHatter.tree.command()
async def join(interaction: discord.Interaction):
    channel = interaction.user.voice.channel
    voice_client = interaction.guild.voice_client

    if not voice_client:
        await channel.connect()
        

@MadHatter.tree.command()
async def leave(interaction: discord.Interaction):
    voice_client = interaction.guild.voice_client

    if voice_client:
        await voice_client.disconnect()
        
@MadHatter.tree.command()
async def play(interaction: discord.Interaction, url: str):
    voice_client = interaction.guild.voice_client

    if not voice_client:
        if interaction.user.voice and interaction.user.voice.channel:
            channel = interaction.user.voice.channel
            await channel.connect()
        else:
            await interaction.channel.send("You are not in a voice channel.")
            return

    if "youtube.com/playlist" in url:
        try:
            playlist = pytube.Playlist(url)
            playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
            playlist._video_urls = [f"https://www.youtube.com{url}" for url in playlist._video_regex.findall(playlist.html)]
            queue.extend(playlist._video_urls)
            await interaction.channel.send(f"Added {len(playlist._video_urls)} songs from the playlist to the queue.")
        except Exception as e:
            await interaction.channel.send("An error occurred while processing the playlist.")
            print(f"Error occurred: {str(e)}")
            return
    else:
        queue.append(url)
        await interaction.channel.send(f"`{url}` has been added to the queue.")

    if not is_playing:
        await play_audio(interaction)
        
async def play_audio(interaction: discord.Interaction):
    global is_playing

    if not queue:
        await interaction.channel.send("The queue is empty. Use the `/play` command to add a video URL.")
        return

    if not is_playing:
        is_playing = True
        url = queue[0]
        try:
            video = pytube.YouTube(url)
            audio_stream = video.streams.filter(only_audio=True).first()
            audio_file = audio_stream.download(output_path="MadHatter Music/")
            voice_client = interaction.guild.voice_client

            def after_playing(err):
                if len(queue) > 0:
                    queue.pop(0)
                if len(queue) > 0 and voice_client and voice_client.is_connected():
                    next_url = queue[0]
                    next_video = pytube.YouTube(next_url)
                    next_audio_stream = next_video.streams.filter(only_audio=True).first()
                    next_audio_file = next_audio_stream.download(output_path="MadHatter Music/")
                    voice_client.play(discord.FFmpegPCMAudio(next_audio_file), after=after_playing)
                    MadHatter.loop.create_task(interaction.channel.send(f"Now playing: `{next_video.title}`"))
                else:
                    global is_playing
                    is_playing = False
                    if voice_client and voice_client.is_connected():
                        MadHatter.loop.create_task(voice_client.disconnect())
                        channel = voice_client.channel
                    if video:
                        print(f"[INFO] Song finished playing: {video.title}")
                    else:
                        print("[INFO] Song finished playing")
                    MadHatter.loop.create_task(interaction.channel.send("The queue is empty. Use the `/play` command to add a video URL."))
                    print(f"[INFO] MadHatter disconnected from voice channel: {channel.name} (ID: {channel.id})")

            voice_client.play(discord.FFmpegPCMAudio(audio_file), after=after_playing)
            await interaction.channel.send(f"Now playing: `{video.title}`")

            # Print voice channel information and current song
            channel = voice_client.channel
            print(f"[INFO] MadHatter connected to voice channel: {channel.name} (ID: {channel.id})")
            print(f"[INFO] Now playing: {video.title}")

        except pytube.exceptions.PytubeError as e:
            await interaction.channel.send("An error occurred while playing the audio.")
            print(f"Error occurred: {str(e)}")

@MadHatter.tree.command()
async def view_queue(interaction: discord.Interaction):
    guild = interaction.guild
    user = interaction.user

    if not queue:
        await interaction.channel.send("The queue is empty.")
    else:
        embed = discord.Embed(title="Current Queue", color=discord.Color.blue())
        embed.set_footer(text=f"{guild.name} |  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        embed.set_author(name=user.display_name, icon_url=user.avatar.url)

        if queue:
            first_song_url = queue[0]
            first_song = pytube.YouTube(first_song_url)
            embed.set_thumbnail(url=first_song.thumbnail_url)

        for i, url in enumerate(queue):
            video = pytube.YouTube(url)
            inline = (i + 1) % 5 == 0  # Set inline to True every 5 songs
            embed.add_field(name=f"Song {i+1}", value=f"[{video.title}]({url})", inline=inline)

        await interaction.channel.send(embed=embed)
        

@MadHatter.tree.command()
async def remove_from_queue(interaction: discord.Interaction, index: int):
    if not queue:
        await interaction.channel.send("The queue is empty.")
    else:
        try:
            index = int(index)
            if index < 1 or index > len(queue):
                await interaction.channel.send("Invalid index.")
            else:
                removed_url = queue.pop(index - 1)
                await interaction.channel.send(f"`{removed_url}` has been removed from the queue.")
        except ValueError:
            await interaction.channel.send("Invalid index.")

@MadHatter.tree.command()
async def skip(interaction: discord.Interaction):
    voice_client = interaction.guild.voice_client

    if voice_client and voice_client.is_playing():
        voice_client.stop()
        await interaction.channel.send("Skipping the current audio.")

@MadHatter.tree.command()
async def pause(interaction: discord.Interaction):
    voice_client = interaction.guild.voice_client

    if voice_client and voice_client.is_playing():
        voice_client.pause()
        await interaction.channel.send("Pausing the current audio.")

@MadHatter.tree.command()
async def resume(interaction: discord.Interaction):
    voice_client = interaction.guild.voice_client

    if voice_client and voice_client.is_paused():
        voice_client.resume()
        await interaction.channel.send("Resuming the audio.")

@MadHatter.tree.command()
async def play_queue(interaction: discord.Interaction):
    if not queue:
        await interaction.channel.send("The queue is empty.")
    else:
        voice_client = interaction.guild.voice_client
        if not voice_client or not voice_client.is_playing():
            await play_audio(interaction)
            
@MadHatter.tree.command()
async def socks4(interaction: discord.Interaction):
    proxy_list = fetch_proxies("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all")
    await send_proxy_list(interaction, proxy_list, "SOCKS4")

@MadHatter.tree.command()
async def https(interaction: discord.Interaction):
    proxy_list = fetch_proxies("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all")
    await send_proxy_list(interaction, proxy_list, "HTTPS")

@MadHatter.tree.command()
async def socks5(interaction: discord.Interaction):
    proxy_list = fetch_proxies("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all")
    await send_proxy_list(interaction, proxy_list, "SOCKS5")

@MadHatter.tree.command(name="deleterole")
async def delete_role(interaction: discord.Interaction, role: discord.Role):
    if role.permissions >= interaction.guild.me.guild_permissions:
        await interaction.response.send_message("I don't have sufficient permissions to delete that role.")
        return
    
    await role.delete()
    await interaction.response.send_message(f"Role {role.name} has been deleted from the server.")

@MadHatter.tree.command(name="levelsearch")
async def search(interaction: discord.Interaction, user: discord.User = None):
    if user is None:
        await interaction.response.send_message("Please provide a user to search for.")
        return
    
    user_id = str(user.id)
    if user_id in user_data:
        data = user_data[user_id]
        last_message = data['last_message']
        
        embed = discord.Embed(
            title="Search Result",
            description=f"Username: {data['username']}\nLevel: {data['level']}\nCurrent XP: {data['xp']}\nMessages Sent: {data['messages']}",
            color=discord.Color.blue()
        )
        
        if last_message:
            last_message_url = f"https://discord.com/channels/{interaction.guild.id}/{interaction.channel.id}/{interaction.message.id}"
            embed.add_field(name="Last Message", value=f"[{last_message}]({last_message_url})", inline=False)
        
        embed.set_thumbnail(url=user.avatar.url)  # Set user's avatar as thumbnail
        embed.set_author(name=interaction.guild.name, icon_url=interaction.guild.icon.url)  # Set guild name and icon
        embed.set_footer(text="Requested At", icon_url=MadHatter.user.avatar.url)
        embed.timestamp = datetime.utcnow()  # Set the timestamp to the current time
        
        await interaction.response.send_message(embed=embed)
    else:
        no_info_embed = discord.Embed(
            title="Search Result",
            description="No information found for the specified user.",
            color=discord.Color.red()
        )
        no_info_embed.set_footer(text="Requested At", icon_url=MadHatter.user.avatar.url)
        no_info_embed.timestamp = datetime.utcnow()  # Set the timestamp to the current time
        await interaction.response.send_message(embed=no_info_embed)

@MadHatter.tree.command(name="levelprofile")
async def profile(interaction: discord.Interaction):
    user_id = str(interaction.author.id)
    if user_id in user_data:
        data = user_data[user_id]
        last_message = data['last_message']
        
        embed = discord.Embed(
            title="Profile",
            description=f"Username: {data['username']}\nLevel: {data['level']}\nCurrent XP: {data['xp']}\nMessages Sent: {data['messages']}",
            color=discord.Color.blue()
        )
        
        if last_message:
            last_message_url = f"https://discord.com/channels/{interaction.guild.id}/{interaction.channel.id}/{interaction.message.id}"
            embed.add_field(name="Last Message", value=f"[View Last Message]({last_message_url})", inline=False)
        
        embed.set_thumbnail(url=interaction.author.avatar.url)  # Set user's avatar as thumbnail
        embed.set_author(name=interaction.guild.name, icon_url=interaction.guild.icon.url)  # Set guild name and icon
        embed.set_footer(text="Requested At", icon_url=MadHatter.user.avatar.url)
        embed.timestamp = datetime.utcnow()  # Set the timestamp to the current time
        
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message("You haven't earned any XP yet.")

try:
    load_reaction_roles()
    load_levels()
    MadHatter.run(token)
except discord.errors.LoginFailure:
    clear()
    print(f"[ {Fore.RED}X{Fore.RESET} ] {Fore.MAGENTA} You did not set up your Discord token accordingly in {Fore.RESET}'{Fore.RED}{settings_dir}{Fore.RESET}'")
    input()
