from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-3.5-turbo"

def categoriza_produto(nome_produto, lista_categorias_possiveis):
  prompt_sistema = f"""
          Você é um categorizador de produtos.
          Você deve assumir as categorias presentes na lista abaixo.

          # Lista de Categorias Válidas
          {lista_categorias_possiveis.split(',')}

          # Formato da Saída
          Produto: Nome do Produto
          Categoria: apresente a categoria do produto

          # Exemplo de Saída
          Produto: Escova elétrica com recarga solar
          Categoria: Eletrônicos Verdes
  """

  response = client.chat.completions.create(
      model=modelo,
      temperature=0, # 0 para resposta mais precisa
      max_tokens=200, # quantidade de tokens
      messages=[
        {
          "role": "system", 
          "content": prompt_sistema
        },
        {
          "role": "user",
          "content": nome_produto
        }
      ]
  )

  return response.choices[0].message.content


categorias_validas = input("Informe categorias validas separadas por virgula:")

while True:
  nome_produto = input("Informe o nome do produto:")
  texto_resposta = categoriza_produto(nome_produto, categorias_validas)
  print(texto_resposta)
  print("--------------------------------")