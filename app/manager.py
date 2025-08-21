from processor import Processor
from fetcher import DAL
import pandas as pd

class DataProcessing:


    def __init__(self):
        self.dataframe = Processor(pd.DataFrame(DAL.read(self)))

    def activate(self):
        self.dataframe = self.dataframe.find_rarest_word()
        self.dataframe = self.dataframe.find_sentiment_word()
        self.dataframe = self.dataframe.detected_weapons()
        return self.dataframe



d = DataProcessing()

print(d)
