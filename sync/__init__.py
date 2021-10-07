import os
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


def create_dir(path):
    """
    To create directory to ump the data
    :param path:
    :return:
    """
    try:
        if not os.path.exists(path):
            os.makedirs(path)
        return True
    except Exception as e:
        return False


def check_file(file_path):
    """
    Check if file exsist
    :param file_path:
    :return:
    """
    if os.path.isfile(file_path):
        return True
    else:
        return False


class SYNC:
    def __init__(self, date_range):
        """
        :param date_range:
        """
        self.date_range = date_range
        self.config = configuration.Parser().read()

    def sync(self):
        """
        Sync the data to the local
        :return:
        """

        for date in self.date_range:
            str_date = date.strftime("%Y-%m-%d")
            path = "{0}\{1}".format(self.config['SYNC']['PATH'], str_date)
            if create_dir(path):
                df = data.match_data(str_date)
                if not check_file("{0}\{1}.csv".format(path,str_date)):
                    df.to_csv("{0}\{1}.csv".format(path, str_date))
                for match_index in range(0, len(df['match_report'].tolist())):
                    filename = "{0}_{1}".format(df['team_a'].tolist()[match_index], df['team_b'].tolist()[match_index])
                    dt = pd.read_html(df['match_report'].tolist()[match_index])
                    for d in range(0, len(dt)):
                        if not check_file(f"{path}\{filename}_{DATA_MAPPING[d]}_match_report.csv"):
                            dt[d].to_csv(
                                f"{path}\{filename}_{DATA_MAPPING[d]}_match_report.csv"
                            )
                print("Data dump successful for the date {}".format(str_date))
            else:
                pass

