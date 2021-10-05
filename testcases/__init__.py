import data.crawler as cw


def test_match_data():
    date = "2021-09-18"
    url = "https://fbref.com/en/matches/{}".format(date)
    df = cw.get_premier_league_data(cw.get_beautiful_object(url))
    if df:
        print("TEST PASSED test_match_data")


def test_player_data():
    year = 2019
    fbref_url = cw.player_link()
    ul = cw.return_way_back_date_url(fbref_url, year=year)
    if cw.returnwaybackDataurl(ul):
        print("TEST PASSED test_player_data")
