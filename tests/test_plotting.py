from tennis_career.cleaning import (read_match_data, tennis_match_dataframe, find_opponent_age, find_player_age, find_age_difference)
from tennis_career.plotting import plot_tennis_career_matches
from tests.test_cleaning import female_data

def test_plot_career_matches():
    female_matches = read_match_data(female_data)
    match_df = tennis_match_dataframe(female_matches)

    match_df = find_age_difference(find_player_age(find_opponent_age(match_df, "female"), "19810926"))

    figure = plot_tennis_career_matches(match_df)

    assert figure is not None
    assert len(figure.axes[0].collections) == 2