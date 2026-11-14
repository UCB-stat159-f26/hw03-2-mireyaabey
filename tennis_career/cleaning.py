import json
import pandas as pd

def read_match_data(js_text):
    if "var morematchmx =" not in js_text:
        raise ValueError("Unable to find match data")

    tennis_data = js_text.split("=", 1)[1]
    tennis_data = tennis_data.strip().rstrip(";")
    tennis_matches = json.loads(tennis_data)

    return tennis_matches
