import json
import discord
from discord.ext import commands

import api
import utils

with open('config.json', 'r') as file:
    config = json.load(file)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot()

@bot.event
async def on_ready():
    for guild in bot.guilds:
        print(
            f'{bot.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

### Commands
@bot.slash_command(description="Use your player ID to retrieve your player stats.",guild_ids=[config["guild_id"]])
async def player_info(ctx, player_id):
    player_info = api.get_player_info(player_id)

    stripped_nick = player_info["player"]["stripped_nick"]
    joined_fuzzy = player_info["player"]["joined_fuzzy"]

    games_played = player_info["games_played"]["overall"]["games"]
    total_kills = player_info["overall_stats"]["overall"]["total_kills"]
    total_deaths = player_info["overall_stats"]["overall"]["total_deaths"]
    k_d_ratio = player_info["overall_stats"]["overall"]["k_d_ratio"]
    last_played = player_info["overall_stats"]["overall"]["last_played_fuzzy"]
    total_playing_time_in_hours = float(player_info["overall_stats"]["overall"]["total_playing_time"]) / 60 / 60


    text = f"> `{stripped_nick} ({player_id})` started playing Xonotic `{joined_fuzzy}`.\n"
    text += f"> Their playtime is `{total_playing_time_in_hours:.2f} hours` and last fragged `{last_played}`.\n\n"
    text += f"> `{stripped_nick}` entered `{games_played}` matches, killed `{total_kills}` enemies and was murdered `{total_deaths}` times.\n"
    text += f"> Their K/D is `{k_d_ratio:.2f}`.\n"
    text += f"\nAccess https://stats.xonotic.org/player/{player_id} for more info."

    
    await ctx.respond(text)

@bot.slash_command(description="Use your nickname to retrieve your player ID.",guild_ids=[config["guild_id"]])
async def retrieve_player_id(ctx, player_nickname):
    player_info = api.get_player_info_from_nick(player_nickname)
    if len(player_info) == 0:
        await ctx.respond("> Go troll someone else, **your moron!**")
        return

    text = f">>> There's {len(player_info)} {'player with a similar nickname' if len(player_info) == 1 else 'players with similar nicknames'} to `{player_nickname}` in the database.\n\n"
    if len(player_info) == 1:
        text += "There you are! You did a nice choice for your nickname!\n"
    elif len(player_info) < 7:
        text += f"You're not the only one who thinks `{player_nickname}` looks cool in a nickname...\n"
    elif len(player_info) < 15:
        text += "Well... You certainly could've been more original.\n"
    else:
        text += "Please use [Xonotic's official Player Index](https://stats.xonotic.org/players).\n"
        text += "Your nickname is WAY too common and I've got better things to do!\n"
        text += "Seeya!"
        await ctx.respond(text)
        return

    text += utils.create_table(player_info)
    await ctx.respond(text)

@bot.slash_command(description="Some, mostly irrelevant, info about this guild's, or another's, Xonotic server.",guild_ids=[config["guild_id"]])
async def server_info(ctx, server_id: discord.Option(str) = None):
    server = config["server_id"] if not server_id else server_id
    server_info = api.get_server_info(server)
    text = f">>> `{server_info['name']} ({server_info['server_id']})` was created at `{server_info['create_dt']}`.\n"
    name_server = config["server_url"] if config["server_url"] and not server_id else server_info['ip_addr']
    text += f"It runs `{server_info['revision']}` at http://{name_server}:{server_info['port']}.\n"
    text += f"Access https://stats.xonotic.org/server/{server} for more info."
    if server == config["server_id"]:
        text += f"\n\n**Thank you for joining us and keep fragging!**"
    await ctx.respond(text)

@bot.slash_command(description="Shows info on last matches.",guild_ids=[config["guild_id"]])
async def last_matches(ctx, server_id: discord.Option(int) = None):
    server_id = config["server_id"] if not server_id else server_id
    server_info = api.get_server_info(server_id)
    match_list = api.get_last_matches(server_id)
    text = f">>> Here are the last matches played at `{server_info['name']} ({server_info['server_id']})`\n"
    text += utils.create_table(match_list)
    text += f"\n\nAccess https://stats.xonotic.org/server/{server_id} for more info."
    await ctx.respond(text)

@bot.slash_command(description="So you think you're THE GOAT? Check the top scorers!",guild_ids=[config["guild_id"]])
async def top_scorers(ctx, server_id: discord.Option(int) = None):
    server_id = config["server_id"] if not server_id else server_id
    server_info = api.get_server_info(server_id)
    top_scorers = api.get_server_top_scorers(server_id)
    text = f">>> Here are the top scorers for `{server_info['name']} ({server_info['server_id']})`\n"
    text += utils.create_table(top_scorers)
    await ctx.respond(text)


bot.run(config["token"])