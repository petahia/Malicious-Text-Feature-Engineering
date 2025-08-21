from processor import Processor
from fetcher import DAL
import pandas as pd

class DataProcessing:
    def __init__(self):
        dal = DAL()
        self.dataframe = Processor(pd.DataFrame(dal.read()))

    def activate(self):
        self.dataframe = self.dataframe.find_rarest_word()
        self.dataframe = self.dataframe.find_sentiment_word()
        self.dataframe = self.dataframe.detected_weapons()
        return self.dataframe




print(d.to_dict())
