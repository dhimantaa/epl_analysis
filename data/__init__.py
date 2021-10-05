from .crawler import *


def match_data(date="2021-09-18"):
    url = "https://fbref.com/en/matches/{}".format(date)
    return get_premier_league_data(get_beautiful_object(url))