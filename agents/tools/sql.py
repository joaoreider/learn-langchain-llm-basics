import sqlite3

from langchain.tools import Tool

try:
  conn = sqlite3.connect("agents/db.sqlite")
  print("Opened database successfully")
except Exception as e:
  print("Error opening database")
  raise e


def run_sql(query):
  c = conn.cursor()
  c.execute(query)
  return c.fetchall()

run_query = Tool.from_function(
    name="run_sqlite_query",
    description="Run a sqlite query.",
    func=run_sql,
)