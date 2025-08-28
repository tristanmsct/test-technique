FROM python:3.12-slim

ARG APP_PATH=/mlflow/
ARG APP_USER=mlflow
WORKDIR ${APP_PATH}

RUN pip install mlflow

ENV BACKEND_URI sqlite:///mlflow.db

EXPOSE 5000

CMD mlflow ui --backend-store-uri $BACKEND_URI --host 0.0.0.0
