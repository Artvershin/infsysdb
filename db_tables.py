import sqlite3
import json

DB_PATH = "db.sqlite"
SAVE_FILE = "db_tables.json"

con = sqlite3.connect(DB_PATH)
cursor = con.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table_names = cursor.fetchall()
table_names = [tbl[0] for tbl in table_names if not tbl[0].startswith("sqlite")]
table_columns = dict()
for name in table_names:
    cursor.execute(f"PRAGMA table_info({name});")
    columns = cursor.fetchall()
    columns = [col[1] for col in columns]
    table_columns[name] = columns

with open(SAVE_FILE, 'w') as f:
    json.dump(table_columns, f, indent=4)