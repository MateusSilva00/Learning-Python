import os
from locale import setlocale, LC_ALL

setlocale(LC_ALL, "PT_BR.UTF-8")

#findPath = "C:/Users/mateu/Documents"
#findTerm = ".pdf"

findPath = input("Digite um caminho: ")
findTerm = input("Digite um termo ou extensão: ")

def formatSize(size):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if size < kilo: 
        text = 'B'
    elif size < mega:
        size /= kilo
        text = 'K'
    elif size < giga:
        size /= mega
        text = 'M'
    elif size < tera:
        size /= giga
        text = 'G'
    elif size < peta:
        size /= tera
        text = 'T'
    else:
        size /= peta
        text = 'P'
    
    size = round(size, 2)
    return f'{size}{text}'.replace('.',',')

count = 0
for root, dirs, files in os.walk(findPath):
    for file in files:
        if findTerm in file:
            try:
                count += 1
                fullPath = os.path.join(root, file)
                arqName, arqExt = os.path.splitext(file)
                size = os.path.getsize(fullPath)
                print("Encontrei o arquivo: ", file)
                print("Caminho: ", fullPath)
                print("Nome: ", arqName)
                print("Extensao: ", arqExt)
                print("Tamanho: ", formatSize(size))
            except PermissionError as e:
                print("Sem permissões!")
            except FileNotFoundError as e:
                print("Arquivo não encontrado")
            except Exception as e:
                print("Erro desconhecido: ", e)
            print()

print("\n",f'{count} arquivo(s) encontrados')
