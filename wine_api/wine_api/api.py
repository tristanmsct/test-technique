#!/usr/bin/env python3
"""
Created on Sat Apr 06 15:09:04 2024.

@author: Tristan Muscat
"""

import pandas as pd
from fastapi import FastAPI
import requests
import json

from wine_api.data_models import WineInput
from wine_api._settings import settings

import mlflow

app = FastAPI()

mlflow.set_tracking_uri(f"http://{settings.MLFLOW_HOST}:5000/")
MODEL = mlflow.sklearn.load_model(f"models:/{settings.MODEL_NAME}@{settings.MODEL_VERSION}")


@app.get("/")
async def root():
    """Create root endpoint for the API"""
    return {"message": "ok"}


@app.get("/pipeline")
async def get_pipeline():
    """Display the model pipeline"""
    return str(MODEL)


@app.get("/model")
async def get_model():
    """Display the model details"""
    model_url = f"http://{settings.MLFLOW_HOST}:5000" + "/api/2.0/mlflow/registered-models/alias"
    response = requests.get(
        url=model_url,
        data=json.dumps({"name": settings.MODEL_NAME, "alias": settings.MODEL_VERSION}),
        headers={"Content-Type": "application/json"},
        timeout=10,
    )

    return response.json()


@app.post("/quality")
async def get_wine_quality(input: WineInput):
    """Predict the quality of a wine based on its attributes."""
    df = pd.json_normalize(input.__dict__)

    pred = MODEL.predict(df)

    return {"prediction": pred[0]}
