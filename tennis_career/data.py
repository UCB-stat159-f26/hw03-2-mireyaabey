import requests


def format_player_name(name):
    name = name.strip()
    name = name.title()
    name = name.replace(" ", "")
    return name


def fetch_career_data(player_name):
    name = format_player_name(player_name)
    url = f"https://www.tennisabstract.com/jsmatches/{name}Career.js"

    response = requests.get(url, timeout=15)

    if response.status_code != 200:
        raise ValueError(f"Could not find player: {player_name}")

    return response.text
