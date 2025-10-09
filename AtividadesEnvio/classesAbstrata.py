#Exercício 1
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome
    @abstractmethod
    def falar():
        pass
class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca
    def falar(self):
        print("Au au")
class Gato(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca
    def falar(self):
        print("Meow")
A = Cachorro("Pitágoras", "Caramelo")
B = Gato("Aristóteles", "Laranja")
A.falar()
B.falar()

#Exercício 2
try:
    testeerro = Animal("Falha")
except:
    print("Não é possível instanciar classe abstrata")

#Exercício 3
class FormaGeometrica(ABC):
    @abstractmethod
    def area():
        ...
    @abstractmethod
    def perimetro():
        ...
class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base*self.altura
    def perimetro(self):
        return self.base*2+self.altura*2
R = Retangulo(5,10)
print(R.area())
print(R.perimetro())

#Exercício 4
class Transporte(ABC):
    @abstractmethod
    def mover():
        ...
    @abstractmethod
    def parar():
        ...


'''class Carro(Transporte):
    def mover():
        print("vrum")

    Colocando desta forma o console apresenta o seguinte erro:
    Traceback (most recent call last):
    File "/workspaces/Back-End-Softex/AtividadesEnvio/classesAbstrata.py", line 75, in <module>
        teste = Carro()
                ^^^^^^^
    TypeError: Can't instantiate abstract class Carro without an implementation for abstract method 'parar'
'''

print("Todas as instâncias do método abstrato devem existir na classe concreta")
class Carro(Transporte):
    def mover(self):
        print("vrum")
    def parar(self):
        print("parou")
teste = Carro()
teste.mover()
teste.parar()