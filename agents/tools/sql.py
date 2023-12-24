import sqlite3

from langchain.tools import Tool

conn = sqlite3.connect('db.sqlite')

def run_sql(query):
    c = conn.cursor()
    c.execute(query)
    return c.fetchall()

run_query = Tool.from_function(
    name="run_sqlite_query",
    description="Run a sqlite query.",
    func=run_sql,
)