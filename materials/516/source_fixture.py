import sqlite3
def database(path):
    db=sqlite3.connect(path)
    db.executescript('CREATE TABLE selected(check_id TEXT PRIMARY KEY,run_id TEXT);CREATE TABLE waivers(run_id TEXT PRIMARY KEY,until INTEGER,revoked INTEGER);')
    return db
