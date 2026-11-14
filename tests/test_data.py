from tennis_career.data import format_player_name


def test_format_player_name():
    assert format_player_name("serena williams") == "SerenaWilliams"
    assert format_player_name("Serena Williams") == "SerenaWilliams"
    assert format_player_name("SerenaWilliams") == "SerenaWilliams"
    assert format_player_name("rafael nadal") == "RafaelNadal"
    assert format_player_name("RafaelNadal") == "RafaelNadal"
    assert format_player_name("Rafael Nadal") == "RafaelNadal"