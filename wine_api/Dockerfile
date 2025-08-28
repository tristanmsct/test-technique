FROM python:3.12-slim

ARG APP_PATH=/wine_api/
ARG APP_USER=wine_api

ARG INSTALL_DEV_DEPS

# prevent python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    TORCH_HOME="/app/torch_cache"

RUN apt-get update && apt-get upgrade -y \
    && if [ -n "$INSTALL_DEV_DEPS" ]; then $INSTALL_DEV_DEPS; fi \
	&& rm -rf /var/lib/apt/lists/* \
	&& adduser --system --group --uid 1000 --home ${APP_PATH} ${APP_USER} \
	&& pip install --no-cache-dir 'poetry==2.1.4' \
	&& poetry config virtualenvs.create false \
    && apt-get purge -y --auto-remove \
    && rm -rf /root/.cache

# Create workdir after creating the user or it will be attributed to root
WORKDIR ${APP_PATH}
USER ${APP_USER}

COPY --chown=${APP_USER}:${APP_USER} pyproject.toml poetry.lock ./
COPY --chown=${APP_USER}:${APP_USER} wine_api/ ./wine_api/

RUN poetry install --no-interaction --no-ansi

EXPOSE 8000

ENTRYPOINT [ "poetry", "run", "uvicorn", "--app-dir=wine_api/", "--host=0.0.0.0", "api:app" ]
