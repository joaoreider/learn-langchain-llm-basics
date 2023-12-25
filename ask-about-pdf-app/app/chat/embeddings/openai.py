from langchain.embeddings import OpenAIEmbeddings
import os

embeddings = OpenAIEmbeddings(
  base_url= "http://llm.igmify.com:8080",
)