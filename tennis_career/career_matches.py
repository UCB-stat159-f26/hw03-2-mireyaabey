from .data import (find_career_data, find_player_dob)
from .cleaning import (read_match_data, tennis_match_dataframe, find_opponent_age, find_player_age, find_age_difference)

def load_career_data(player_name):
    extract_raw_data = find_career_data(player_name)
    match_data = read_match_data(extract_raw_data)

    match_df = tennis_match_dataframe(match_data)

    opponent_dob = str(match_df["opponent_age_or_dob"].dropna().iloc[0])

    if len(opponent_dob) == 8 and opponent_dob.isdigit():
        gender = "female"
    else:
        gender = "male"

    player_dob = find_player_dob(player_name)

    match_df = find_age_difference(find_player_age(find_opponent_age(match_df, gender), player_dob))

    return match_df
