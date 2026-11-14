from tennis_career.cleaning import read_match_data, tennis_match_dataframe


def test_read_match_data():
    sample_data = 'var morematchmx = [["19951030", "Canadian Open", "Carpet"]];'

    matches = read_match_data(sample_data)

    assert len(matches) == 1
    assert matches[0][0] == "19951030"
    assert matches[0][1] == "Canadian Open"
    assert matches[0][2] == "Carpet"

def test_tennis_match_dataframe():
    sampled_match = [
        "19951030", "Canadian Open", "Carpet", "W", "L",
        "", "", "WC", "Q1", "6-1 6-1", "3",
        "Anne Miller", "149", "7", "", "R", "19770119"]

    matches = [sampled_match]
    match_df = tennis_match_dataframe(matches)

    assert len(match_df) == 1
    assert match_df["result"][0] == "L"
    assert match_df["opponent_age_or_dob"][0] == "19770119"
