from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
  ChatPromptTemplate,
  HumanMessagePromptTemplate,
  MessagesPlaceholder
)
from langchain.agents import OpenAIFunctionsAgent, AgentExecutor
from tools.sql import run_query

from dotenv import load_dotenv
import os
load_dotenv()


chat = ChatOpenAI(
  base_url= os.getenv("BASE_URL"),
  api_key= os.getenv("OPENAI_API_KEY"),
)
prompt = ChatPromptTemplate(
  messages = [
  HumanMessagePromptTemplate.from_template("{input}"),
  MessagesPlaceholder(
    variable_name="agent_scratchpad"
  )
  ]
)

tools = [run_query]
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
agent_executor("How many users are in the database?")