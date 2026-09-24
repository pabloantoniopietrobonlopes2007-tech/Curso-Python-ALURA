import requests
import json

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

response = requests.get(url) #recebe os dados desse site

if response.status_code == 200:
    dados_json = response.json() #trnsforma os dados em json
    dados_restaurante = {} #cria um dicionario vazio para os dados dos restaurantes

    for item in dados_json:
        nome_restaurante = item["Company"] #pega o nome do restaurante do item atual

        if nome_restaurante not in dados_restaurante: #se esse restaurante não foi adicionado ainda, cria uma lista vazia para ele
            dados_restaurante[nome_restaurante] = []

        dados_restaurante[nome_restaurante].append({ #adiciona os dados do item à lista do restaurante atual
            "item": item["Item"],
            "price": item["price"],
            "description": item["description"]

        })

else:
    print(f"Erro ao fazer a requisição. Código de status: {response.status_code}")


for nome_restarante, dados in dados_restaurante.items():
    nome_arquivo = f"{nome_restarante}.json" #cria o nome do arquivo com o nome do restaurante

    with open(nome_arquivo, "w") as arquivo: #abre o arquivo para escrita
        json.dump(dados, arquivo, indent=4)