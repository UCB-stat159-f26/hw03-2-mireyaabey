import requests


def format_player_name(name):
    name = name.strip()

    if " " in name:
        name = name.title()
        name = name.replace(" ", "")
    else:
        name = name[0].upper() + name[1:]

    return name


def find_career_data(player_name):
    name = format_player_name(player_name)
    url = f"https://www.tennisabstract.com/jsmatches/{name}Career.js"

    response = requests.get(url, timeout=15)

    if response.status_code != 200:
        raise ValueError(f"Player name not found: {player_name}")

    return response.text

def find_player_dob(player_name, gender):
    player_name = format_player_name(player_name)

    url = f"https://www.tennisabstract.com/jsmatches/{player_name}.js"
    response = requests.get(url, timeout=15)

    if response.status_code != 200:
        raise ValueError(f"Could not find player: {player_name}")

    page = response.text
    birth_date = page.split("var dob=")[1]
    birth_date = birth_date.split(";")[0]

    return birth_date.strip()