from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

class DAL:
    def __init__(self):
        self.user = os.getenv('user')
        self.password = os.getenv('pass')
        self.DBname = os.getenv('DBname')
        self.client = MongoClient(os.getenv('connection_string'))
        self.database = self.client['IranMalDB']
        self.collection = self.database['tweets']


    def read(self):
        result = self.collection.find({},{'_id':0})
        return result

