A simple bot for querying data from Xonotic's official API.
Still a work in progress.

## Instructions
* Install dependencies using `pip3 -r requirements.txt`.
* Fill `config.json` with your own data:
  * token: Your private Discord BOT token (create one at `https://discord.com/developers/applications/`).
  * guild_id: Your Discord Server (Guild) ID. You may have to enable Discord's developer mode to access it.
  * server_id: Your Xonotic server ID. If you're unsure, search for your server's name at `https://stats.xonotic.org/servers`.
  * server_url: Optional. Should be filled if you use a DNS with your server (as in `example.com`. No `http://` nor slash at the end `/`).
  * server_image_url: Optional server-specific picture for `server_info` embeds when your own server is queried.
  * thumbnail_url: Optional Xonotic icon URL for Discord embeds.
* Add your previously created bot to your server.
* Run `bot.py`.

## Features
All available commands use the slash (`/`) prefix and can be accessed in the UI.

Currently available commands are: 

#### - player_info (player_id)
Retrieves basic player stats from the `/player` endpoint.

<img
  src="https://raw.githubusercontent.com/JoaoVicthor/XonStat_Discord_bot/main/previews/player_info.png"
  alt="player_info output example"
  style="display: inline-block; margin: 0 auto; max-width: 408px">

#### - retrieve_player_id (player_nickname)
Gathers a list including up to 15 players from the `/player` endpoint which nicknames includes the provided string.

<img
  src="https://raw.githubusercontent.com/JoaoVicthor/XonStat_Discord_bot/main/previews/retrieve_player_id.png"
  alt="retrieve_player_id output example"
  style="display: inline-block; margin: 0 auto; max-width: 558px">

#### - server_info (server_id?)
Queries some info about the guild's Xonotic server.
You can use the optional `server_id` argument to retrieve info about other servers.

<img
  src="https://raw.githubusercontent.com/JoaoVicthor/XonStat_Discord_bot/main/previews/server_info.png"
  alt="server_info output example"
  style="display: inline-block; margin: 0 auto; max-width: 438px">

#### - last_matches (server_id?)
Lists the last 10 matches played on the server.
The optional `server_id` can be used to list games from other servers.

<img
  src="https://raw.githubusercontent.com/JoaoVicthor/XonStat_Discord_bot/main/previews/last_matches.png"
  alt="last_matches output example"
  style="display: inline-block; margin: 0 auto; max-width: 1158px">

#### - top_scorers (server_id?)
Ranks the players in your server.
I bet you know what's the `server_id` for.

<img
  src="https://raw.githubusercontent.com/JoaoVicthor/XonStat_Discord_bot/main/previews/top_scorers.png"
  alt="top_scorers output example"
  style="display: inline-block; margin: 0 auto; max-width: 937px">

#### - votable_cvars
Reads `cvars.json` and shows a list of available votable commands on the Xonotic server.

<img
  src="https://raw.githubusercontent.com/JoaoVicthor/XonStat_Discord_bot/main/previews/votable_cvars.png"
  alt="votable_cvars output example"
  style="display: inline-block; margin: 0 auto; max-width: 599px">

## Probable future features
* Get info about specific matches
* Localization to Brazilian Portuguese
* Info on weapons used by players (Currently not all weapons have all stats)
* Logging
* Integration with Xonotic Server logs

## Contact
With all of that out of the way...
What about a DM match?

Feel free to join us at `Servidor do Samura`!
https://stats.xonotic.org/server/42896

Also, here's our Discord server if you're interested.
https://discord.gg/d7QHcsT
