#!/usr/bin/env/python3
import sys
import os

argumentos = sys.argv
qtdArgumetos = len(argumentos)

if qtdArgumetos <= 1:
    print("Faltando argumentos: ")
    print("-a", "Para listar todos os arquivos nesta pasta", sep='\t')
    print("-d", "Para listar todos os diretórios nesta pasta", sep='\t')
    sys.exit()

onlyArq = False
onlyDir = True

if '-a' in argumentos:
    onlyArq = True
if '-d' in argumentos:
    onlyDir = True

for arquivo in os.listdir('.'):
    if onlyArq:
        if os.path.isfile(arquivo):
            print(arquivo)
    
    if onlyDir:
        if os.path.isdir(arquivo):
            print(arquivo)