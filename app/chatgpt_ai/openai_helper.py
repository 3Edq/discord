from dotenv import load_dotenv
import openai
import os
from llama_index import ListIndex, SimpleWebPageReader,download_loader,GPTVectorStoreIndex
load_dotenv()

openai.api_key = os.getenv('CHATGPT_API_KEY')

def chatgpt_response(prompt):
  
    SimpleWebPageReader = download_loader("SimpleWebPageReader")
    loader = SimpleWebPageReader()
    documents = loader.load_data(urls=['https://news.yahoo.co.jp/articles/6bba0b1661ad80a578430f033eb1952809c8f4fb'])
    index = GPTVectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    response = query_engine.query(prompt)
  
    return f"**{response}**"
    
if __name__ == '__main__':
  res = chatgpt_response('')
  print(res)