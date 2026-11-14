from tennis_career.data import (format_player_name, find_career_data)
import pytest
from unittest.mock import patch


def test_format_player_name():
    assert format_player_name("serena williams") == "SerenaWilliams"
    assert format_player_name("Serena Williams") == "SerenaWilliams"
    assert format_player_name("SerenaWilliams") == "SerenaWilliams"
    assert format_player_name("rafael nadal") == "RafaelNadal"
    assert format_player_name("RafaelNadal") == "RafaelNadal"
    assert format_player_name("Rafael Nadal") == "RafaelNadal"

def test_invalid_player_input():
    with patch("tennis_career.data.requests.get") as fake_request:
        fake_request.return_value.status_code = 404

        with pytest.raises(ValueError):
            find_career_data("GastonSanchez")