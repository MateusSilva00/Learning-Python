class Person(object):
    __name = ""
    __age = -1
    __sex = ''

    def __init__(self):
        """ Método construtor"""

    def register(self):
        # Método register: permite receber os dados de uma pessoa
        self.__name = input("Digite o seu name:")
        while self.__age < 0:
            try:
                self.__age = int(input("Digite sua age: "))
            except ValueError:
                print("Digite um número inteiro !")
        self.__sex = input("sex: M para masculino ou F para feminino: ")
        self.__sex = self.__sex.upper()
        if self.__sex != 'F':
            self.__sex = 'M'
        
    def mostrar(self):
        # Método mostrar: apresenta os dados cadastro de uma pessoa
        if self.__sex == 'F' and self.__age > 30:
            print(self.__name + 'age secreta ' + self.__sex)
        else:
            print(self.__name + ' ' + str(self.__age) + ' ' + self.__sex)

PERSONS = list()
for i in range(0, 3):
    OBJ = Person()
    OBJ.register()
    PERSONS.append(OBJ)

for PERSON in PERSONS:
    PERSON.mostrar()

print('Line 38 ' + str(PERSONS))
print('Line 39 ' + str(PERSONS[0]))
print('Line 40 ' + str(PERSONS[0].__dict__))
print('Line 41 ' + str(PERSONS[0].__dict__.keys()))
print('Line 42 ' + str(PERSONS[0].__dict__.values()))
PERSONS[0]._Person__age = 'No age'
print('Line 43 ' + str(PERSONS[0]._Person__age))
PERSONS[0]._Person__apelido = 'Lil Joseph'
print('Line 44 ' + str(PERSONS[0].__dict__))
