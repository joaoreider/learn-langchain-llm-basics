from langchain.embeddings import OpenAIEmbeddings
import os

embeddings = OpenAIEmbeddings(
  openai_api_base= "http://llm.igmify.com:8080",
)