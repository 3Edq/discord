from llama_index import ListIndex, SimpleWebPageReader
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

def llama_response(prompt):
  documents = SimpleWebPageReader(html_to_text=True).load_data(
    ["https://www.smbcnikko.co.jp/first/stock/",
     "https://faq.rakuten-sec.co.jp/"]
)
  index = ListIndex.from_documents(documents)
  query_engine = index.as_query_engine()
  response = query_engine.query(prompt)
  
  return f"**{response}**"