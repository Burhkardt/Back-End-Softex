#Exercício 1
class Livro():
    def __init__(self, nome):
        self.nome = nome
    def ler(self):
        print(f"Lendo {self.nome}")
    def __str__(self):
        return self.nome
class Pessoa():
    def __init__(self, nome):
        self.nome = nome
        self.listaDeLivros = []
    def addLivro(self, livro):
        self.listaDeLivros.append(livro)
    def remLivro(self, livro):
        self.listaDeLivros.remove(livro)
    def listaLivros(self):
        return ", ".join(str(livro) for livro in self.listaDeLivros)
joao = Pessoa("João")
aquele = Livro("Livro")
aqueleoutro = Livro("Outro livro")
joao.addLivro(aquele)
joao.addLivro(aqueleoutro)
print(joao.listaLivros())
joao.listaDeLivros[0].ler()
joao.listaDeLivros[1].ler()

#Exercicio 2
class Onibus():
    def __init__(self, linha):
        self.linha = linha
class Aluno():
    def __init__(self, nome):
        self.nome = nome
        self.busao = None
    def rodando(self, onibus:Onibus):
        self.busao = onibus.linha
        print(f"{self.nome} está na linha {onibus.linha}")
    def desceu(self):
        print(f"{self.nome} desceu do onibus da linha {self.busao}")
        self.busao = None
tancredo = Onibus(1234)
a = Aluno("Jusé")
a.rodando(tancredo)
a.desceu()

#Exercicio 3

class Departamento():
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
    def addFunc(self, func):
        self.funcionarios.append(func)
    def listaFunc(self):
        print(", ".join(str(i) for i in self.funcionarios))

class Funcionario():
    def __init__(self, nome, funcao):
        self.nome = nome
        self.funcao = funcao
    def __str__(self):
        return self.nome

a= Funcionario("Ele", "sim")
b= Funcionario("Ele?", "não")
dep = Departamento("Abacate")
dep.addFunc(a)
dep.addFunc(b)
dep.listaFunc()

#Exercicio 4

class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao
    def __str__(self):
        return self.nome

class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []
    def adicionar_jogador(self, jogador:Jogador):
        self.jogadores.append(jogador)
    def listar_jogadores(self):
        print(", ".join(str(j) for j in self.jogadores))

jogador1 = Jogador("Carlos", "Atacante")
jogador2 = Jogador("Rafael", "Goleiro")
time = Time("Tigrão")
time.adicionar_jogador(jogador1)
time.adicionar_jogador(jogador2)
time.listar_jogadores()

#Exercicio 5
class Motor:
    def __init__(self):
        print("Motor criado!")
    def ligar(self):
        print("ligou motor")
    def desligar(self):
        print("Desligou motor")

class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.motor = Motor()
        print(f"Carro {self.modelo} criado!")

carro1 = Carro("Fusca")
carro1.motor.ligar()
carro1.motor.desligar()

#Exercicio 6
class Comodo:
    def __init__(self, nome):
        self.nome = nome
    def __str__(self):
        return self.nome

class Casa:
    def __init__(self, endereco, comodos_nomes):
        self.endereco = endereco
        self.comodos = []
    def addComodo(self, comodo:Comodo):
        self.comodos.append(comodo)
    def listarComodos(self):
        print(f"Comodos da casa: {', '.join(str(c) for c in self.comodos)}")

# Demonstração de composição
casa1 = Casa("Aquele lugar", ["Sala", "Cozinha", "Quarto", "Banheiro"])
casa1.listar_comodos()