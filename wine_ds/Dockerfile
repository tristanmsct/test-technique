FROM python:3.12-slim

ARG APP_PATH=/wine_ds/
ARG APP_USER=wine_ds
WORKDIR ${APP_PATH}

ARG INSTALL_DEV_DEPS

RUN apt-get update && apt-get upgrade -y \
    && if [ -n "$INSTALL_DEV_DEPS" ]; then $INSTALL_DEV_DEPS; fi \
	&& apt-get install git -y \
	&& rm -rf /var/lib/apt/lists/* \
	&& adduser --system --group --uid 1000 --home ${APP_PATH} ${APP_USER} \
	&& pip install --no-cache-dir 'poetry>=2.1' \
	&& poetry config virtualenvs.create false

COPY --chown=${APP_USER}:${APP_USER} pyproject.toml poetry.lock ./
COPY --chown=${APP_USER}:${APP_USER} wine_ds/ ./wine_ds/

RUN poetry install --no-interaction --no-ansi

USER ${APP_USER}

# Override me.
CMD [ "tail", "-f", "/dev/null" ]
