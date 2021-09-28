class Pessoa(object):
    __nome = ""
    __idade = -1
    __sexo = ''

    def __init__(self):
        """ Método construtor"""

    def cadastrar(self):
        # Método cadastrar: permite receber os dados de uma pessoa
        self.__nome = input("Digite o seu nome:")
        while self.__idade < 0:
            try:
                self.__idade = int(input("Digite sua idade: "))
            except ValueError:
                print("Digite um número inteiro !")
        self.__sexo = input("Sexo: M para masculino ou F para feminino: ")
        self.__sexo = self.__sexo.upper()
        if self.__sexo != 'F':
            self.__sexo = 'M'
        
    def mostrar(self):
        # Método mostrar: apresenta os dados cadastro de uma pessoa
        if self.__sexo == 'F' and self.__idade > 30:
            print(self.__nome + 'idade secreta ' + self.__sexo)
        else:
            print(self.__nome + ' ' + str(self.__idade) + ' ' + self.__sexo)

PESSOAS = list()
for i in range(0, 3):
    OBJ = Pessoa()
    OBJ.cadastrar()
    PESSOAS.append(OBJ)

for PESSOA in PESSOAS:
    PESSOA.mostrar()

print('Linha 38 ' + str(PESSOAS))
print('Linha 39 ' + str(PESSOAS[0]))
print('Linha 40 ' + str(PESSOAS[0].__dict__))
print('Linha 41 ' + str(PESSOAS[0].__dict__.keys()))
print('Linha 42 ' + str(PESSOAS[0].__dict__.values()))
PESSOAS[0]._Pessoa__idade = 'Sem Idade'
print('Linha 43 ' + str(PESSOAS[0]._Pessoa__idade))
PESSOAS[0]._Pessoa__apelido = 'Zé Pequeno'
print('Linha 44 ' + str(PESSOAS[0].__dict__))
