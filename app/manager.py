from processor import Processor
from fetcher import CRUD
import pandas as pd


class DataProcessing:
    def __init__(self,data):
        self.data = pd.DataFrame(data)


    def activate(self):
        self.data = self.data
