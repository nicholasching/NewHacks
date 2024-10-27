from typing import Union
import csv
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/get_data", response_model=List[Dict[str,str]])
def read_item():
    sender = []
    with open('spam_rankings.csv', newline='') as csvfile:
  # Create a reader object
        csv_reader = csv.DictReader(csvfile)
        for i in csv_reader:
            sender.append(i)
    return sender

if __name__ =="__main__":
    uvicorn.run(app,host="localhost", port=8080) 
