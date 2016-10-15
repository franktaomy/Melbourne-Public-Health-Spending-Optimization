#!/usr/bin/env python
import pprint
import sqlite3

def test_query():
  # Location of database file
  database_file = "database.db"

  # Open SQLite database connection
  conn = sqlite3.connect(database_file)
  cur = conn.cursor()

  # Sample query
  result = cur.execute("SELECT * FROM data LIMIT 5")
  pprint.pprint(cur.fetchall())

test_query()
