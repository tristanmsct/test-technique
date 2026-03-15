#!/usr/bin/env python
"""
Created on 2026-03-15.

@author: Tristan Muscat
@email: tristan.muscat@pm.me
"""

import sys

from loguru import logger
from wine_api._settings import settings

_APP_LOG_FORMAT: str = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> |"
    "<level>{level: <8}</level> |"
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> |"
    "<level>{message}</level> | {extra}"
)

logger.remove(0)

logger.add(
    sys.stderr,
    format=_APP_LOG_FORMAT,
    level=settings.LOG_LEVEL,
)
