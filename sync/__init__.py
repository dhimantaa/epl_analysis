import data
import configuration
import pandas as pd


DATA_MAPPING = [
    'team_a',
    'team_b',
    'statistics',
    'team_a_player_summary',
    'team_a_passing',
    'team_a_pass_type',
    'team_a_defensive_action',
    'team_a_possession',
    'team_a_misc',
    'team_a_gk_stats',
    'team_b_player_summary',
    'team_b_passing',
    'team_b_pass_type',
    'team_b_defensive_action',
    'team_b_possession',
    'team_b_misc',
    'team_b_gk_stats',
    'shot_summary_both',
    'shot_summary_team_a',
    'shot_summary_team_b'
]


class SYNC:
    def __init__(self, date_range):
        """
        :param date_range:
        """
        self.date_range = date_range
        self.config = configuration.Parser().read()

    def sync(self):
        """

        :return:
        """

        for date in self.date_range:

            str_date = date.strftime("%Y-%m-%d")
            df = data.match_data(str_date)
            df.to_csv("data/dump/{}.csv".format(str_date))
            for match_index in range(0, len(df['match_report'].tolist())):
                dt = pd.read_html(df['match_report'].tolist()[match_index])
                for d in range(0, len(dt)):
                    dt[d].to_csv(
                        f"{self.config['SYNC']['PATH']}{DATA_MAPPING[d]}_match_{match_index}_{str_date}.csv"
                    )
            print("Data dump successful for the date {}".format(str_date))