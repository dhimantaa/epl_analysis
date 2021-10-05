import bs4
import json
import requests
import warnings
import pandas as pd
from bs4 import BeautifulSoup


def get_beautiful_object(link):
    """
    This function will return soup object from the url
    :param link: string
    :return: beautifulsoup object
    """

    warnings.filterwarnings("ignore")
    page = requests.get(link)
    return BeautifulSoup(page.content, 'html.parser')


def get_premier_league_data(soup, league_id="div_sched_11160"):
    """
    Give you the league data as per the date
    :param soup: object with date
    :param league_id: div id of the league
    :return: DataFrame
             columns
                1 - gameweek
                2 - time
                3 - team_a
                4 - squad_a
                5 - xg_a
                6 - score
                7 - xg_b
                8 - team_b
                9 - squad_b
                10- attendance
                11- venue
                12- referee
                13- match_report
    """
    df = pd.DataFrame()
    for i in soup.find("div", {"id": league_id}):
        tdlist = BeautifulSoup(str(i)).findAll('td')
        if tdlist:
            gameweek = ([td.text for td in tdlist if 'gameweek' in td.attrs.values()])
            time = ([td.text for td in tdlist if 'time' in td.attrs.values()])
            team_a = ([td.text for td in tdlist if 'squad_a' in td.attrs.values()])

            squad_a = (
                [
                    "https://fbref.com/" + td.contents[0].attrs['href'] for td in tdlist if
                    'squad_a' in td.attrs.values()
                ]
            )

            xg_a = ([td.text for td in tdlist if 'xg_a' in td.attrs.values()])
            score = ([td.text for td in tdlist if 'score' in td.attrs.values()])
            xg_b = ([td.text for td in tdlist if 'xg_b' in td.attrs.values()])
            team_b = ([td.text for td in tdlist if 'squad_b' in td.attrs.values()])

            squad_b = (
                [
                    "https://fbref.com/" + td.contents[0].attrs['href'] for td in tdlist if
                    'squad_b' in td.attrs.values()
                ]
            )

            attendance = ([td.text for td in tdlist if 'attendance' in td.attrs.values()])
            venue = ([td.text for td in tdlist if 'venue' in td.attrs.values()])
            referee = ([td.text for td in tdlist if 'referee' in td.attrs.values()])

            match_report = (
                [
                    "https://fbref.com/" + td.contents[0].attrs['href'] for td in tdlist if
                    'match_report' in td.attrs.values()
                ]
            )

            notes = ([td.text for td in tdlist if 'notes' in td.attrs.values()])
            sort_show = ([td.text for td in tdlist if 'sort_show' in td.attrs.values()])

            df['gameweek'] = gameweek
            df['time'] = time
            df['team_a'] = team_a
            df['squad_a'] = squad_a
            df['xg_a'] = xg_a
            df['score'] = score
            df['xg_b'] = xg_b
            df['team_b'] = team_b
            df['squad_b'] = squad_b
            df['attendance'] = attendance
            df['venue'] = venue
            df['referee'] = referee
            df['match_report'] = match_report

    return df


def player_link(words="ro", name="Cristiano Ronaldo"):
    """
    This function will create the player profile link
    words: string intials of player name
    name: string player name
    return: fbref link
    """
    url = "https://fbref.com/en/players/{}/".format(words)
    soup = get_beautiful_object(url)
    for i in soup.find("div", {"class": "section_content"}):
        if not isinstance(i, bs4.element.NavigableString):
            if name in i.contents[0].text:
                return "https://fbref.com{}".format(i.contents[0].attrs["href"])


def return_way_back_date_url(fbref_url, year=2021):
    """
    This function will return the wayback date link to capture point in time data
    fbref_url: string
    year: int
    return: way back link for point in time data
    """
    return "https://web.archive.org/__wb/calendarcaptures/2?url={0}&date={1}&groupby=day".format(fbref_url, year)


def return_way_back_data_url(ul, fbref_url, year=2019):
    """
    This function will return the wayback data link to capture point in time data
    ul: string wayback date link
    return: wayback data link
    """
    data_url = []
    json_data = json.loads(requests.get(ul).text)
    if not json_data:
        return None
    for date in json_data["items"]:
        if len(str(date[0])) == 3:
            up_date = str(year) + "0" + str(date[0])
        else:
            up_date = str(year) + str(date[0])
        data_url.append("https://web.archive.org/web/{0}/{1}".format(up_date, fbref_url))
    return data_url





