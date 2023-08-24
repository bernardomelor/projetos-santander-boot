import pandas as pd
import openai

df = pd.read_csv('userinfo.txt')
kcal_diario = df["KcalDia"].tolist()
lista_compras = []

openai_api_key = "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"
openai.api_key = openai_api_key

def gen_shoplist(kcal_diario):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
          "role": "system",
          "content": "Você é um nutricionista especialista em musculação e dietas de baixo custo."
      },
      {
          "role": "user",
          "content": f"Crie uma lista de compras para uma dieta de uma semana com quatro refeições diárias considerando {kcal_diario} calorias por dia e especificando os pratos a serem feitos."
      }
    ]
  )
  return completion.choices[0]

lista_compras = lista_compras.append(gen_shoplist)
print(lista_compras)