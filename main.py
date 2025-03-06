from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system", 
        "content": "Listar apenas os nomes dos produtos da lista, sem considerar descrição."
      },
      {
        "role": "user",
        "content": "Liste 3 produtos sustentaveis."
      }
    ]
)

print(response.choices[0].message.content)
