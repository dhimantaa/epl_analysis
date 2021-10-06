import sync
import datetime
import pandas as pd


class ModelA:
    """
    This model will predict the match score of english premier league
    """
    def __init__(self, start_date=None, end_date=None):
        """
        Once the object created it start dumps the data
        :param start_date:
        :param end_date:
        """

        if start_date and end_date:
            self.start_date = datetime.datetime.strptime(start_date, "%Y%m%d")
            self.end_date = datetime.datetime.strptime(end_date, "%Y%m%d")
            self.date_range = [
                self.start_date + datetime.timedelta(days=x) for x in range(0, (self.end_date - self.start_date).days)
            ]
            synchronization = sync.SYNC(self.date_range).sync()
        else:
            pass

    def run(self):
        pass
