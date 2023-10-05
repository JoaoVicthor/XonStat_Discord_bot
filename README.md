A simple bot for querying data from Xonotic's official API.
Still a work in progress.

## Instructions
* Install dependencies using `pip3 -r requirements.txt`
* Fill `config.json` with your own data:
  * token: Your private Discord BOT token (create one at https://discord.com/developers/applications/)
  * guild_id: Your Discord Server (Guild) ID. You may have to enable Discord's developer mode to access it.
  * server_id: Your Xonotic server ID. If you're unsure, search for your server's name at https://stats.xonotic.org/servers
  * server_url: Optional (default `null`). Should be filled if you use a DNS with your server (as in `example.com`. No `http://` nor slash at the end `/`).
* Add your previously created bot to your server.
* Run `bot.py`.

## Features
All available commands use the slash (`/`) prefix and can be accessed in the UI.

Currently available commands are: 

#### - player_info (player_id)
Retrieves basic player stats from the `/player` endpoint.

#### - retrieve_player_id (player_nickname)
Gathers a list including up to 15 players from the `/player` endpoint which nicknames includes the provided string.

#### - server_info (server_id?)
Queries some info about the guild's Xonotic server.
You can use the optional `server_id` argument to retrieve info about other servers.

#### - last_matches (server_id?)
Lists the last 10 matches played on the server.
The optional `server_id` can be used to list games from other servers.

#### - top_scorers (server_id?)
Ranks the players in your server.
I bet you know what's the `server_id` for.

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
