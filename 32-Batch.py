import pandas as pd
import joblib
import requests
from flask import  jsonify
from datetime import timedelta, datetime
from prefect import task, Flow
from prefect.schedules import IntervalSchedule

@task(max_retries=3, retry_delay=timedelta(5))
def predict(input_data_path:str):
    classifier = joblib.load('classifier.pkl')
    df = pd.read_csv(input_data_path)
    prediction = classifier.predict(df)
    return jsonify({'prediction': list(prediction)})
  
  
@task(max_retries=3, retry_delay=timedelta(5))
def save_prediction(data, output_data_path:str):
    with open(output_data_path, 'w') as f:
      f.write(data)

    
schedule = IntervalSchedule(
    start_date=datetime.utcnow() + timedelta(seconds=5),
    interval=timedelta(days=1),
)

with Flow("predictions", schedule=schedule) as flow:
    df_h = pd.read_csv("HourlyDataset.csv", index_col=0)
    df_h = df_h.set_index('Date')
    data = df_h[['Return', 'Return-7', 'Return-30', 'Return_eth', 'Return_bnb', 'Return_ada', 'Return_lite']]
    
    prediction = predict("data")
    save_prediction(prediction, "./output_data.csv")