#!/usr/bin/env python3
"""
Created on Sat Apr 13 10:38:53 2024.

@author: Tristan Muscat
"""

import pandas as pd
from sqlalchemy import create_engine
import requests
import json
import sys

import mlflow

from wine_ds._settings import settings

n_wine = 0
if len(sys.argv) >= 2:
    n_wine = int(sys.argv[1])

# Import data
engine = create_engine(f"postgresql://postgres:admin@{settings.POSTGRESQL_HOST}:5432/postgres")

df = pd.read_sql("wine", engine)

str_json = df.loc[n_wine].drop(columns=["quality"]).to_json(None, orient="index")

headers = {
    "Content-Type": "application/json",
}

response = requests.post(f"http://{settings.API_HOST}:8000/quality", headers=headers, data=str_json)

pred = json.loads(response.content.decode("utf-8"))

# print(f"""La qualité prédite du vin n°{n_wine} est de {pred["prediction"]}""")

print(pred)
