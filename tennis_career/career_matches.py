from .data import find_career_data
from .cleaning import (read_match_data, tennis_match_dataframe, find_opponent_age, find_player_age, find_age_difference)

def load_career_data(player_name, player_birth_date, gender):
    extract_raw_data = find_career_data(player_name)
    match_data = read_match_data(extract_raw_data)

    match_df = tennis_match_dataframe(match_data)
    match_df = find_opponent_age(match_df, gender)
    match_df = find_player_age(match_df, player_birth_date)
    match_df = find_age_difference(match_df)

    return match_df