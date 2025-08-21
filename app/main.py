from fastapi import FastAPI
from manager import DataProcessing
import uvicorn

app = FastAPI()
proc = DataProcessing()

@app.get('/')
def hello():
    return ('Hello and welcome to the Tweet Analysis Project endpoint!'
            'enter /get_data to get the information.')

@app.get('/get_data')
def get_json_of_data():
    df = proc.activate()
    return df.to_dict(orient='records')

if __name__ == "__main__":
    uvicorn.run('main:app',port=8000,reload=True)


