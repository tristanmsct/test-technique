#!/usr/bin/env python3
"""
Created on Sat Apr 13 10:38:53 2024.

@author: Tristan Muscat
"""
import pandas as pd
from sqlalchemy import create_engine

from wine_ds._settings import settings

engine = create_engine(f"""postgresql://postgres:admin@{settings.POSTGRESQL_HOST}:5432/postgres""")

df = pd.read_csv("https://raw.githubusercontent.com/aniruddhachoudhury/Red-Wine-Quality/master/winequality-red.csv")

df.columns = ["_".join(col.split(" ")) for col in df.columns]

df.to_sql("wine", engine, index=False, if_exists="replace")
