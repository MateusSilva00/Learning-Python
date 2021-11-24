"""
Comma Separated Values - CSV (Valores separados por virgula)
É um formato de dados muito usado em tabelas (excel, google sheets), bases de dados, clientes de email, etc
"""
import csv

with open('modulos\clientes.csv' , 'r') as arquivo:
    #dados = csv.reader(arquivo)
    #dados = csv.DictReader(arquivo)

    #for dado in dados:
    #    print(dado['Nome'], dado['Sobrenome'], dado['E-mail'], dado['Telefone'])
    dados = [x for x in csv.DictReader(arquivo)]

with open("modulos\clientes2.csv", 'w') as arquivo:
    escreve = csv.writer(
        arquivo, 
        delimiter=',',
        quotechar='"',
        quoting = csv.QUOTE_ALL
    )

    chaves = dados[0].keys()
    chaves = list(chaves)
    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3]
        ]
    )


    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )