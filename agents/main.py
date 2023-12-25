from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
  ChatPromptTemplate,
  HumanMessagePromptTemplate,
  MessagesPlaceholder
)
from langchain.agents import OpenAIFunctionsAgent, AgentExecutor
from langchain.schema import SystemMessage
from tools.sql import run_query, list_tables, describe_tables_tool

from dotenv import load_dotenv
import os
load_dotenv()


chat = ChatOpenAI(
  base_url= os.getenv("BASE_URL"),
  api_key= os.getenv("OPENAI_API_KEY"),
)

tables = list_tables()

prompt = ChatPromptTemplate(
  messages = [
  SystemMessage(content = (
    "You are an AI that has access to a SQLite database.\n"
    f"The database has tables of: {tables}\n"
    "Do not make any assumptions about what tables exist "
    "or what columns exist. Instead. use the describe_tables function.\n"
  )),
  HumanMessagePromptTemplate.from_template("{input}"),
  MessagesPlaceholder(
    variable_name="agent_scratchpad"
  )
  ]
)

tools = [run_query, describe_tables_tool]
agent = OpenAIFunctionsAgent(
  llm = chat,
  prompt = prompt,
  tools = tools
)
agent_executor = AgentExecutor(
  agent=agent,
  verbose=True,
  tools=tools
)
agent_executor("How many users are in the database that the name starts with J?")