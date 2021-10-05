import data
import datetime


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
            for date in self.date_range:
                print(date.strftime("%Y-%m-%d"))
                df = data.match_data(date.strftime("%Y-%m-%d"))
                print(df.head())
        else:
            pass

    def run(self):
        pass
