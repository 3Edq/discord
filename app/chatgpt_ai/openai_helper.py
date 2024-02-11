from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def chatgpt_response(prompt):
  from openai._client import OpenAI
  client = OpenAI()
  
  response = client.chat.completions.create(
    model='gpt-4',
    messages=[
      {"role": "system", "content": "You are a helpful agent to respond message in Japanese"},
      {"role": "user", "content": prompt},
    ]
    
  )
  print(response.choices[0].message.content)
  return response.choices[0].message.content

if __name__ == '__main__':
  res = chatgpt_response('')
  print(res)