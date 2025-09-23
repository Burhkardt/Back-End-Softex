#Exercício 1
class ContaBancaria():
    def __init__(self, nome, saldo, cpf):
        if saldo >= 0:
            self.nome = nome
            self.__saldo = saldo
            self.cpf = cpf
        else:
            print("Valor de saldo inválido")
    def getSaldo(self):
        return self.__saldo
    def setSaldo(self, novoSaldo):
        if novoSaldo >= 0:
            self.__saldo = novoSaldo
        else:
            print("Valor de saldo inválido")
    def alterSaldo(self, alteracao):
        valorAlterado = self.__saldo + alteracao
        if valorAlterado >= 0:
            if valorAlterado > self.__saldo:
                print(f"Depósito de {alteracao:.2f}R$ bem sucedido")
            elif valorAlterado < self.__saldo:
                print(f"Saque de {-alteracao:.2f} bem sucedido")
            else:
                print("Nenhuma alteração feita")
            self.__saldo = valorAlterado
            print(f"Seu saldo é de {self.__saldo:.2f}")

    def __str__(self):
        return f"{self.nome} possui {self.__saldo:.2f}R$"

print()
teste = ContaBancaria("João", 500, 123456789)
teste.setSaldo(1000)
print(teste)
teste.alterSaldo(-200)
teste.alterSaldo(+100)


#Crie uma classe, Pessoa, que tenha os atributos: nome, data de nascimento, cpf, identidade. 
# Deixe os atributos cpf e identidade como privado e monte os métodos setters e getters para 
# acessar e editar os valores
class Pessoa():
    def __init__(self, nome, nasc, cpf, identidade):
        self.nome = nome
        self.nasc = nasc
        self.__cpf = cpf
        self.__identidade = identidade
    def __str__(self):
        return f"{self.nome} nasceu em {self.nasc}"
    def getCPF(self):
        return self.__cpf
    def setCPF(self, cpf):
        self.__cpf = cpf
        print("CPF alterado")
    def getIdentidade(self):
        return self.__identidade
    def setIdentidade(self,ident):
        self.__identidade = ident
        print("Identidade alterada")
pessoa1 = Pessoa("João", "10/10/1969", 123456789, 1234567890)
print(pessoa1)
print(pessoa1.getIdentidade())
pessoa1.setCPF(987654321)
print(pessoa1.getCPF())