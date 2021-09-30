class Carro(object):
    totalCarros = 0

    # Construtor
    def __init__(self, modelo: str = None, ano: int = None, preco: float = None, cor: str = None):
        if modelo is None:
            self.modelo = "Fusca"
            self.vel_max = 80
            self.ano = 1981
            self.preco = 5000
            self.cor = "Azul"
        
        else:
            self.modelo = modelo
            self.vel_max = 180
            self.ano = ano
            self.preco = preco
            self.cor = cor
        self.__class__.totalCarros += 1
    
    # Destrutor
    def __del__(self):
        self.__class__.totalCarros -= 1
        print("Removendo {}: endereco {}".format(self.modelo, id(self)))
    

    def getModelo(self) -> str:
        return str(self.modelo)
    
    def setModelo(self, modelo: str):
        if type(modelo) is str:
            self.modelo = modelo
    
    def getCor(self) -> str:
        return str(self.cor)
    
    def setCor(self, novaCor: str):
        if type(novaCor) is str:
            self.cor = novaCor
    
    def getPreco(self) -> int:
        return str(self.preco)
    
    def setPreco(self, novoPreco: int):
        if type(novoPreco) is int:
            self.preco = novoPreco
        elif type(novoPreco) is str:
            try:
                self.preco = int(novoPreco)
            except ValueError:
                pass
    
    def getAno(self) -> str:
        return str(self.ano)
    
    def setAno(self, novoAno: int):
        if type(novoAno) is int:
            self.ano = novoAno
        elif type(novoAno) is str:
            try:
                self.ano = int(novoAno)
            except ValueError:
                pass
    
    def __repr__(self) -> None:
        return '<{}: {} - {} - ${}>\n'.format(self.modelo, self.ano, self.cor, self.preco)

    @classmethod
    def total(cls) -> None:
        # Método da classe
        print("Total de carros: " + str(cls.totalCarros))

    @staticmethod
    def stotal(classCarro) -> None:
        # Método estático
        print("Total de carros: " + str(classCarro.__class__.totalCarros))

if __name__ == "__main__":
    
    ESTACIONAMENTO = list()

    for i in range(0, 3):
        OBJ = Carro()
        ESTACIONAMENTO.append(OBJ)
    
    ESTACIONAMENTO[0].setModelo("Monza")
    ESTACIONAMENTO[0].setCor("Azul")
    ESTACIONAMENTO[0].setAno("2000")
    ESTACIONAMENTO[0].setPreco("477123")

    Carro.total()
    del ESTACIONAMENTO[1]

    for CARRO in ESTACIONAMENTO:
        print(CARRO.getModelo() + ' ' + CARRO.getAno() + ' ' + CARRO.getPreco())
    
    Carro.stotal(ESTACIONAMENTO[0])
