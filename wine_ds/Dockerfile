FROM python:3.12-slim

ARG APP_PATH=/wine_ds/
ARG APP_USER=wine_ds

ARG INSTALL_DEV_DEPS

# prevent python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    TORCH_HOME="/app/torch_cache"

RUN apt-get update && apt-get upgrade -y \
    && if [ -n "$INSTALL_DEV_DEPS" ]; then $INSTALL_DEV_DEPS; fi \
	&& apt-get install git -y \
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
COPY --chown=${APP_USER}:${APP_USER} wine_ds/ ./wine_ds/

RUN poetry install --no-interaction --no-ansi

# Override me.
CMD [ "tail", "-f", "/dev/null" ]
