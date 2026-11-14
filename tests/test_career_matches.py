from tennis_career import career_matches
from tests.test_cleaning import female_data

def test_load_career_data(monkeypatch):
    monkeypatch.setattr(career_matches, "find_career_data", lambda name: female_data)
    monkeypatch.setattr(career_matches, "find_player_dob", lambda name: "19810926")

    result = career_matches.load_career_data("Serena Williams")

    assert len(result) == 3
    assert "player_age" in result.columns
    assert "age_difference" in result.columns