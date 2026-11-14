from tennis_career.cleaning import (read_match_data, tennis_match_dataframe, find_opponent_age, find_player_age, find_age_difference)
import pandas as pd

female_data = '''
var morematchmx = [
["19951030", "Canadian Open", "Carpet", "W", "L", "", "", "WC", "Q1", "6-1 6-1", "3", "Anne Miller", "149", "7", "", "R", "19770119", "", "USA", "0", "", "", "", "", "", "", "1995-W-WT-CAN-02A-1995-013"],
["19970307", "Indian Wells", "Hard", "W", "L", "", "", "WC", "Q1", "6-4 6-0", "3", "Alexia Dechaume Balleret", "87", "", "", "R", "19700503", "", "FRA", "0", "", "", "", "", "", "", "1997-W-WT-USA-02A-1997-006"],
["19970804", "Manhattan Beach", "Hard", "W", "L", "", "", "WC", "Q3", "7-6 4-6 6-3", "3", "Magui Serna", "54", "6", "", "L", "19790301", "167", "ESP", "0", "", "", "", "", "", "", "1997-W-WT-USA-07A-1997-026"]
];
'''

male_data = '''
var morematchmx = [
["20010910", "Spain F10", "Hard", "S", "L", "", "", "WC", "R32", "2-6 7-5 6-2", "3", "Guillermo Platel", "731", "", "", "R", "22.264202601", "", "ESP", "0", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "2001-M-FU-ESP-10A-2001-002", "", "1", "1"],
["20010917", "Seville CH", "Clay", "C", "L", "", "", "WC", "R16", "3-6 6-1 6-3", "3", "Stefano Galvani", "161", "2", "", "R", "24.2902121834", "178", "ITA", "0", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "2", "", "", "", "2001-784-024", "", "2", "2"],
["20010917", "Seville CH", "Clay", "C", "W", "", "", "WC", "R32", "6-4 6-4", "3", "Israel Matos Gil", "751", "", "Q", "U", "18.7597535934", "", "ESP", "0", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "2001-784-015", "", "1", "1"]
];
'''

def test_read_match_data():
    matches = read_match_data(female_data)

    assert len(matches) == 3
    assert matches[0][0] == "19951030"
    assert matches[0][1] == "Canadian Open"
    assert matches[0][2] == "Carpet"

def test_tennis_match_dataframe():
    matches = read_match_data(female_data)
    match_df = tennis_match_dataframe(matches)

    assert len(match_df) == 3
    assert match_df["result"][0] == "L"
    assert match_df["opponent_age_or_dob"][0] == "19770119"

def test_female_opponent_age():
    matches = read_match_data(female_data)
    match_df = tennis_match_dataframe(matches)

    find_age = find_opponent_age(match_df, "female")

    assert round(find_age["opponent_age"][0], 1) == 18.8

def test_male_opponent_age():
    matches = read_match_data(male_data)
    match_df = tennis_match_dataframe(matches)

    find_age = find_opponent_age(match_df, "male")

    assert round(find_age["opponent_age"][0], 2) == 22.26

def test_player_age():
    matches = read_match_data(female_data)
    match_df = tennis_match_dataframe(matches)

    player_dob = "19810926"
    player_age = find_player_age(match_df, player_dob)

    assert round(player_age["player_age"][0], 1) == 14.1


def test_age_difference():
    matches = read_match_data(female_data)
    match_df = tennis_match_dataframe(matches)

    match_df = find_opponent_age(match_df, "female")
    match_df = find_player_age(match_df, "19810926")

    age_difference = find_age_difference(match_df)

    assert round(age_difference["age_difference"][0], 1) == -4.7