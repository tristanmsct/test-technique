#!/usr/bin/env python3
"""
Created on Sat Apr 06 15:09:04 2024.

@author: Tristan Muscat
"""

from functools import lru_cache

from pydantic_settings import BaseSettings

__all__ = ["settings"]


class Settings(BaseSettings):
    """Gather all settings for the Wine API."""

    MLFLOW_HOST: str = "localhost"
    POSTGRESQL_HOST: str = "localhost"
    API_HOST: str = "localhost"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
