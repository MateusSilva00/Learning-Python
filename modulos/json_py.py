"""
Javascript Object Notation - JSON
JSON (JavaScript Objetict Notation) é um formato de troca de dados entre sistemas e programas muito leve
e de fácil utilização. Muito utilizado por APIS
DUMPS / dump
PYTHON          JSON
dict             object
list, tuple      array
str              string
int, float       number
True             true
False            false
None             NULL
"""
from dados import *
import json

lista = [1, 2, 3, 4, 5, 6]
dadosJson = json.dumps(lista)
print(type(dadosJson))

dictio = json.dumps(clientes_dicionario, indent=4)
print(type(dictio))

dictio2 = json.loads(clientes_json)

for chave, valor in dictio2.items():
    print(chave)
    print(valor)


# Salvar em um arquivo
with open('clients.json', 'r') as arquivo:
    dados = json.load(arquivo)

print(dados)