
from dotenv import load_dotenv
import os
load_dotenv()

# Langchain
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings

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
print(docs)