from abc import ABC, abstractmethod

#Exercício 1
class Pagamento(ABC):
    @abstractmethod
    def processar(ABC, valor):
        print(f"Processando transação de {valor:.2f}R$")
class CartaoCredito(Pagamento):
    ...
    def processar(ABC, valor):
        super().processar(valor)
class Boleto(Pagamento):
    ...
    def processar(ABC, valor):
        super().processar(valor)

A = CartaoCredito()
A.processar(15)

#Exercício 2
class Ligavel(ABC):
    @abstractmethod
    def ligar(self):
        print("Ligou")
class Desligavel(ABC):
    @abstractmethod
    def desligar(self):
        print("Desligou")
class Computador(Ligavel, Desligavel):
    def ligar(self):
        super().ligar()
    def desligar(self):
        super().desligar()
PC = Computador()
PC.ligar()
PC.desligar()

#Exercício 3
class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        print("Imprimindo")
class Exportavel(ABC):
    @abstractmethod
    def exportar(self):
        print("Exportando")

class Relatorio(Imprimivel,Exportavel):
    def imprimir(self):
        super().imprimir()
    def exportar(self):
        super().exportar()

relatorio = Relatorio()
relatorio.imprimir()
relatorio.exportar()

#Exercício 4
class Repositorio(ABC):
    def __init__(self):
        self.repo = dict()
    @abstractmethod
    def salvar(self, objeto):
        self.repo[str(len(self.repo))]= objeto
        print(f"Salvando {objeto}")
    @abstractmethod
    def buscar(self, id):
        print(self.repo.__getitem__(str(id)))
class RepositorioMemoria(Repositorio):
    def __init__(self):
        super().__init__()
    def salvar(self, objeto):
        super().salvar(objeto)
    #Em caso de não implementação de um dos métodos ele apresenta o erro
#   Traceback (most recent call last):
#   File "/workspaces/Back-End-Softex/AtividadesEnvio/interfaces.py", line 79, in <module>
#       rep = RepositorioMemoria()
#           ^^^^^^^^^^^^^^^^^^^^
#   TypeError: Can't instantiate abstract class RepositorioMemoria without an implementation for abstract method 'buscar'
    def buscar(self, id):
        return super().buscar(id)

rep = RepositorioMemoria()
rep.salvar("Grande teste")
rep.buscar(0)