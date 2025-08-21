from fastapi import FastAPI
from manager import DataProcessing
import uvicorn

app = FastAPI()

@app.get('/get_data')
def get_json_of_data():
    return DataProcessing().activate().to_dict()



if __name__ == "__main__":
    uvicorn.run(app)
