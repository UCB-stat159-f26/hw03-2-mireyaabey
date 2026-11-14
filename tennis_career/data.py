import requests


def format_player_name(name):
    name = name.strip()

    if " " in name:
        name = name.title()
        name = name.replace(" ", "")
    else:
        name = name[0].upper() + name[1:]

    return name


def fetch_career_data(player_name):
    name = format_player_name(player_name)
    url = f"https://www.tennisabstract.com/jsmatches/{name}Career.js"

    response = requests.get(url, timeout=15)

    if response.status_code != 200:
        raise ValueError(f"Could not find player: {player_name}")

    return response.text
