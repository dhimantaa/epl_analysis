import data


def test_match_data():
    date = "2021-09-18"
    url = "https://fbref.com/en/matches/{}".format(date)
    df = data.get_premier_league_data(data.get_beautiful_object(url))
    if not df.empty:
        print("TEST PASSED test_match_data")
    else:
        print("TEST FAILED test_match_data")


def test_player_data():
    year = 2019
    fbref_url = data.player_link()
    ul = data.return_way_back_date_url(fbref_url, year=year)
    if data.return_way_back_data_url(ul, fbref_url, year=year):
        print("TEST PASSED test_player_data")
    else:
        print("TEST FAILED test_player_data")


test_match_data()
test_player_data()
