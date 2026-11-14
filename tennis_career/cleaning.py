import json
import pandas as pd

def read_match_data(js_text):
    if "var morematchmx =" not in js_text:
        raise ValueError("Unable to find match data")

    tennis_data = js_text.split("=", 1)[1]
    tennis_data = tennis_data.strip().rstrip(";")
    tennis_matches = json.loads(tennis_data)

    return tennis_matches


match_columns = ["date", "tournament", "surface", "result", "opponent", "opponent_age_or_dob"]


def tennis_match_dataframe(matches):
    match_data = []

    for match in matches:
        row = [match[0], match[1], match[2],
               match[4], match[11], match[16]]
        match_data.append(row)

    match_df = pd.DataFrame(match_data, columns=match_columns)

    return match_df

def find_opponent_age(match_df, gender):
    match_df = match_df.copy()

    if gender == "female":
        date_of_match = pd.to_datetime(match_df["date"], format="%Y%m%d")
        date_of_birth = pd.to_datetime(match_df["opponent_age_or_dob"], format="%Y%m%d")

        age_in_days = (date_of_match - date_of_birth).dt.days
        opponent_age = age_in_days / 365.25

    else:
        opponent_age = pd.to_numeric(match_df["opponent_age_or_dob"])

    match_df["opponent_age"] = opponent_age

    return match_df


def find_player_age(match_df, player_birth_date):
    date_of_match = pd.to_datetime(match_df["date"], format="%Y%m%d")
    date_of_birth = pd.to_datetime(player_birth_date, format="%Y%m%d")

    match_df["player_age"] = (date_of_match - date_of_birth).dt.days / 365.25

    return match_df

def find_age_difference(match_df):
    match_df = match_df.copy()

    match_df["age_difference"] = (match_df["player_age"] - match_df["opponent_age"])

    return match_df


