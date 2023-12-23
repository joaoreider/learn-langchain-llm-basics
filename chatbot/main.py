
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationSummaryMemory
from dotenv import load_dotenv
import os
load_dotenv()



chat = ChatOpenAI(
  base_url=os.getenv("BASE_URL"),
  verbose=True
)

memory = ConversationSummaryMemory(
  # chat_memory=FileChatMessageHistory("chatbot/chat_history.json"),
  memory_key="messages", 
  return_messages=True,
  llm=chat
)

prompt = ChatPromptTemplate(
  input_variables=["content", "messages"],
  messages=[
    MessagesPlaceholder(variable_name="messages"),
    HumanMessagePromptTemplate.from_template("{content}")
  ]

)

chain = LLMChain(
  prompt=prompt,
  llm=chat,
  memory=memory,
  verbose=True

)


while True:
  content: str = input("You: ")
  if content == "exit":
    break
  try:
    result = chain({"content": content})
    print("Bot: ", result["text"])
  except Exception as e:
    print(e)
    break
