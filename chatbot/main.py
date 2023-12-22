
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
load_dotenv()



chat = ChatOpenAI()


prompt = ChatPromptTemplate(
  input_variables=["content"],
  messages=[
    HumanMessagePromptTemplate.from_template("{content}")
  ]

)

chain = LLMChain(
  prompt=prompt,
  llm=chat,

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
