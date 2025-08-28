#!/usr/bin/env python3
"""
Created on Sat Apr 13 11:24:33 2024.

@author: Tristan Muscat
"""

import pandas as pd
from sqlalchemy import create_engine

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler
from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import train_test_split

import mlflow
from mlflow import MlflowClient

from wine_ds._settings import settings

# Import data
engine = create_engine(f"""postgresql://postgres:admin@{settings.POSTGRESQL_HOST}:5432/postgres""")

df = pd.read_sql("wine", engine)

X_train, X_test, y_train, y_test = train_test_split(df.drop(columns=["quality"]), df["quality"], train_size=0.8)

mlflow.set_tracking_uri(f"http://{settings.MLFLOW_HOST}:5000/")
mlflow.set_experiment(experiment_name="Default")
client = MlflowClient()

mlflow.autolog()

with mlflow.start_run() as run:
    # Create pipeline
    ml_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", RobustScaler()),
            ("regressor", RandomForestRegressor()),
        ]
    )

    ml_pipeline.fit(X_train, y_train)

    ml_pipeline.score(X_test, y_test)

    run_id = run.info.run_id

    model_uri = f"runs:/{run_id}/model"
    model_version = mlflow.register_model(model_uri, "wine_quality")
    client.set_registered_model_alias("wine_quality", "production", model_version.version)
