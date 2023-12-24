
from dotenv import load_dotenv
import os
load_dotenv()

# Langchain
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
import langchain
langchain.debug = True

text_splitter = CharacterTextSplitter(
  separator="\n",
  chunk_size=200,
  chunk_overlap=0
)

embeddings = OpenAIEmbeddings(
  base_url=os.getenv("BASE_URL")
)

loader = TextLoader('facts-embedding/facts.txt')
docs = loader.load_and_split(text_splitter=text_splitter)

db = Chroma.from_documents(
  docs,
  embedding = embeddings,
  persist_directory='facts-embedding/emb')

results = db.similarity_search_with_score("What is an interesting fact about the english language?")

for result in results:
  print("\n", result)