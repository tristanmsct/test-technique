#!/usr/bin/env python3
"""
Created on Sat Apr 06 15:09:04 2024.

@author: Tristan Muscat
"""

from functools import lru_cache

from pydantic_settings import BaseSettings


__all__ = ["settings"]


class Settings(BaseSettings):
    """Gather all settings for the Cat API."""

    MLFLOW_HOST: str = "localhost"

    MODEL_NAME: str = "wine_quality"
    MODEL_VERSION: str = "production"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
