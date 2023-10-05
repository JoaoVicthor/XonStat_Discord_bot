import requests, re

headers = {"accept": "application/json"}

### GAME/MATCH

# curl -X GET "https://stats.xonotic.org/game/{game_id}" -H  "accept: application/json"
def get_game_info(game_id):
    url = f"https://stats.xonotic.org/game/{game_id}"
    response = requests.get(url, headers=headers)
    return response.json()


### PLAYER

# curl -X GET "https://stats.xonotic.org/player/{player_id}" -H  "accept: application/json"
def get_player_info(player_id):
    url = f"https://stats.xonotic.org/player/{player_id}"
    response = requests.get(url, headers=headers)
    return response.json()

# curl -X GET "https://stats.xonotic.org/player/{player_id}/weapons?game_type_cd={game_type}" -H  "accept: application/json"
def get_player_weapon_info(player_id, game_type = None):
    url = f"https://stats.xonotic.org/player/{player_id}/weapons"
    params = {"game_type_cd": game_type} if game_type is not None else None
    response = requests.get(url, params=params, headers=headers)
    return response.json()

# curl -X GET "https://stats.xonotic.org/players?nick={nick}" -H "accept: application/json"
def get_player_info_from_nick(nick):
    url = "https://stats.xonotic.org/players"
    params = {"nick": nick}
    response = requests.get(url, params=params, headers=headers)
    players = response.json()["players"]
    kept_keys = ["player_id", "stripped_nick", "joined_fuzzy"]
    players = [{key: str(value) for key, value in player.items() if key in kept_keys} for player in players]
    return players


### SERVER

# curl -X GET "https://stats.xonotic.org/server/{server_id}" -H  "accept: application/json"
def get_server_info(server_id):
    url = f"https://stats.xonotic.org/server/{server_id}"
    response = requests.get(url, headers=headers)
    return response.json()

# curl -X GET "https://stats.xonotic.org/server/{server_id}/topscorers" -H  "accept: application/json"
def get_server_top_scorers(server_id):
    def _strip_nick_and_int_to_str(top_scorer):
        hex_color_pattern = r'\^x?[0-9A-Fa-f]{1,3}'
        stripped_nick = re.sub(hex_color_pattern, '', top_scorer["nick"])
        top_scorer["nick"] = stripped_nick
        top_scorer["player_id"] = str(top_scorer["player_id"])
        top_scorer["score"] = str(top_scorer["score"])
        top_scorer["rank"] = str(top_scorer["rank"])
        return top_scorer
    url = f"https://stats.xonotic.org/server/{server_id}/topscorers"
    response = requests.get(url, headers=headers)
    top_scorers = response.json()["top_scorers"]
    return list(map(_strip_nick_and_int_to_str, top_scorers))

# curl -X GET "https://stats.xonotic.org/games?server_id={server_id}" -H  "accept: application/json"
def get_last_matches(server_id):
    url = f"https://stats.xonotic.org/games?server_id={server_id}"
    response = requests.get(url, headers=headers)
    matches = response.json()[:10]
    kept_keys = ["game_id", "game_type_descr", "map_name", "nick", "create_dt"]
    matches = [{key: str(value) for key, value in match.items() if key in kept_keys} for match in matches]
    return matches

# curl -X GET "https://stats.xonotic.org/topservers" -H  "accept: application/json"
def get_top_servers():
    url = f"https://stats.xonotic.org/topservers"
    response = requests.get(url, headers=headers)
    return response.json()
