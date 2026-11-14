from tennis_career.cleaning import read_match_data, tennis_match_dataframe


def test_read_match_data():
    sample_data = 'var morematchmx = [["19951030", "Canadian Open", "Carpet"]];'

    matches = read_match_data(sample_data)

    assert len(matches) == 1
    assert matches[0][0] == "19951030"
    assert matches[0][1] == "Canadian Open"
	assert matches[0][2] == "Carpet"

