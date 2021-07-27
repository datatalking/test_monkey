# PATH ~/sbox/test/pandas_sqlite_dbase/read_sql_query.py

import pandas as pd
import sqlite3

conn = sqlite3.connect("flights.db")
df = pd.read_sql_query("SELECT * FROM airlines LIMIT 5;", conn)
df