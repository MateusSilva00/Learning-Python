try:
    print(a)
except NameError as erro:
    print("ERROR: ", erro)

try:
    a = []
    print(a[1])
except NameError as erro:
    print('Erro do desenvolvedor')
except (IndexError, KeyError) as erro:
    print("Erro de índice")
except Exception as erro:
    print("Ocorreu um erro inesperado")
