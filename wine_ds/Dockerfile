FROM ghcr.io/astral-sh/uv:python3.14-trixie

ARG APP_PATH=/wine_ds/
ARG APP_USER=wine_ds

ARG INSTALL_DEV_DEPS

# prevent python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && apt-get upgrade -y \
    && if [ -n "$INSTALL_DEV_DEPS" ]; then $INSTALL_DEV_DEPS; fi \
	&& rm -rf /var/lib/apt/lists/* \
	&& adduser --system --group --uid 1000 --home ${APP_PATH} ${APP_USER} \
    && apt-get purge -y --auto-remove \
    && rm -rf /root/.cache

# Create workdir after creating the user or it will be attributed to root
WORKDIR ${APP_PATH}
USER ${APP_USER}

COPY --chown=${APP_USER}:${APP_USER} pyproject.toml uv.lock ./
COPY --chown=${APP_USER}:${APP_USER} wine_ds/ ./wine_ds/

RUN uv sync

# Override me.
CMD [ "tail", "-f", "/dev/null" ]
