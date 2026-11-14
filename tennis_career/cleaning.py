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
