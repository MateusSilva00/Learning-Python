import random as rd
import string

inteiro = rd.randint(10,20)
fluatuante = rd.uniform(10, 29)
fluatant = rd.random() #Entre 0 e 1

integer = rd.randrange(900, 999, 10)

lista = ["Metallica", "Angra", "Megadeth", "Blind Guardian", "Kreator"]

print(inteiro, fluatuante, fluatant, integer)
print(rd.choices(lista, k = 3))
print(rd.sample(lista, 2)) # Não retorno valores repetidos

# Embaralha a lista
rd.shuffle(lista)
print(lista)

# Gera senha aleatória
letra = string.ascii_letters
digitos = string.digits
caracters = "!@#$%+=-&*^"
geral = letra + digitos + caracters
senha = "".join(rd.choices(geral, k = 20))
print(senha)