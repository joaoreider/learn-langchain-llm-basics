import sqlite3

from langchain.tools import Tool
from typing import List
from pydantic.v1 import BaseModel
try:
  conn = sqlite3.connect("agents/db.sqlite")
  print("Opened database successfully")
except Exception as e:
  print("Error opening database")
  raise e

def list_tables():
  c = conn.cursor()
  c.execute("SELECT name FROM sqlite_master WHERE type='table';")
  rows = "\n".join([x[0] for x in c.fetchall() if x[0] is not None])
  print(rows)
  return 

def run_sql(query):
  c = conn.cursor()
  try:
    c.execute(query)
    return c.fetchall()
  except sqlite3.OperationalError as err:
    return f"The following error occured: {str(err)}"

def describe_tables(table_names):
  c = conn.cursor()
  tables = ', '.join("'"+ table + "'" for table in table_names)
  rows = c.execute(f"SELECT sql FROM sqlite_master WHERE name IN ({tables});")
  return "\n".join([row[0] for row in rows if row[0] is not None])


class RunQueryArgsSchema(BaseModel):
  query: str

class DescribeTablesArgsSchema(BaseModel):
  table_names: List[str]

run_query = Tool.from_function(
    name="run_sqlite_query",
    description="Run a sqlite query.",
    func=run_sql,
    args_schema=RunQueryArgsSchema,
)

describe_tables_tool = Tool.from_function(
    name="describe_tables",
    description="Given a list of table names, return the schema of those tables.",
    func=describe_tables,
    args_schema=DescribeTablesArgsSchema,
)