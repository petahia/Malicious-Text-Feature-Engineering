from processor import Processor
from fetcher import DAL
import pandas as pd

class DataProcessing:
    def __init__(self):
        self.dal = DAL()
        data = list(self.dal.read())
        self.dataframe = pd.DataFrame(data)
        self.processor = Processor((self.dataframe))

    def activate(self):
        self.dataframe = self.processor.find_rarest_word()
        self.dataframe = self.processor.find_sentiment_word()
        self.dataframe = self.processor.detected_weapons()
        return self.dataframe




