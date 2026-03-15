FROM python:3.14-slim

ARG APP_PATH=/mlflow/
ARG APP_USER=mlflow
WORKDIR ${APP_PATH}

RUN pip install --no-cache-dir mlflow==3.10.1

ENV BACKEND_URI=sqlite:///mlflow.db

EXPOSE 5000

CMD ["sh", "-c", "mlflow server --backend-store-uri=$BACKEND_URI --host=0.0.0.0"]
