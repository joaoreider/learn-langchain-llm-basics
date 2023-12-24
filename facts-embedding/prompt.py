from dotenv import load_dotenv
import os
load_dotenv()

from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

from redundant_filter_retriever import RedudantFilterRetriever


chat = ChatOpenAI(
  base_url=os.getenv("BASE_URL")
)

embeddings = OpenAIEmbeddings(
  base_url=os.getenv("BASE_URL")
)

db = Chroma(
  persist_directory='facts-embedding/emb',
  embedding_function=embeddings
)

retriever = RedudantFilterRetriever(
  embeddings=embeddings,
  chroma=db
) # object that can take in a string and return some relevant documents
chain = RetrievalQA.from_chain_type(
  llm = chat,
  retriever = retriever,
  chain_type="stuff" # basic chain type, take some cnotext from the vector store and "stuff" it into the prompt
)

result = chain.run("What is an interesting fact about the english language?")
print(result)