#Exercício 1 e 2
class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\n"
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
pessoa1 = Pessoa("João", 25)
print(pessoa1)
pessoa1.apresentar()
print()

#exercício 3 e 4
class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def __str__(self):
        return f"Marca: {self.marca} \nModelo: {self.modelo} \nAno: {self.ano}\n"
    
carro1 = Carro("Fiat", "UNO", 1984)
carro2 = Carro("Fiat","Sienna", 2006)
carro3 = Carro("Aquele lá", "Aquele mesmo", 1)
print(carro1)
print(carro2)
print(carro3)
carro3.ano = 2000
print(carro3)

#Exercício 5 e 6
class ContaBancaria():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def sacar(self,valor):
        if valor <= 0:
            print("Valor de saque inválido")
            return None
        if valor > self.saldo:
            print("Transação inválida")
            return False
        else:
            self.saldo -= valor
            print(f"Transação concluída com sucesso, seu novo saldo é de {self.saldo}")
            return True
    def depositar(self, valor):
        if valor <= 0:
            print("Valor de depósito inválido")
            return None
        self.saldo += valor
        print(f"Valor de {valor} depositado.\nSeu novo saldo é de {self.saldo}")
    def __str__(self):
        return f"Nome:{self.titular} \nSaldo: {self.saldo}\n"
Jorge = ContaBancaria("Jorge", 2000)
Jorge.depositar(500)
print(Jorge)
Jorge.depositar(-100)
Jorge.sacar(0)
Jorge.sacar(2500)
print(Jorge.sacar(2))

#Exercício 7 e 8
class Aluno():
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    def __str__(self):
        return f"Aluno: {self.nome} - Nota: {self.nota}"
class Turma():
    def __init__(self, nomeTurma):
        self.nomeTurma = nomeTurma
        self.alunos = []
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
a = Aluno("Maria", 9.5)
b = Aluno("José", 7.8)
c = Aluno("Jorge", 4)
turmaA = Turma("A")
turmaA.adicionar_aluno(a)
turmaA.adicionar_aluno(b)
turmaA.adicionar_aluno(c)
print(a)

#Exercício 9
class Cachorro():
    especie = "Canis familiaris"
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
dog = Cachorro("Pitágoras", 475)
print(dog.especie)
print(Cachorro.especie)