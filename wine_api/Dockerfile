FROM python:3.12-slim

ARG APP_PATH=/wine_api/
ARG APP_USER=wine_api
WORKDIR ${APP_PATH}

ARG INSTALL_DEV_DEPS

RUN apt-get update && apt-get upgrade -y \
    && if [ -n "$INSTALL_DEV_DEPS" ]; then $INSTALL_DEV_DEPS; fi \
	&& rm -rf /var/lib/apt/lists/* \
	&& adduser --system --group --uid 1000 --home ${APP_PATH} ${APP_USER} \
	&& pip install --no-cache-dir 'poetry>=2.1' \
	&& poetry config virtualenvs.create false

COPY --chown=${APP_USER}:${APP_USER} pyproject.toml poetry.lock ./
COPY --chown=${APP_USER}:${APP_USER} wine_api/ ./wine_api/

RUN poetry install --no-interaction --no-ansi

EXPOSE 8000

USER ${APP_USER}

ENTRYPOINT [ "uvicorn", "--app-dir=wine_api/", "--host=0.0.0.0", "api:app" ]
