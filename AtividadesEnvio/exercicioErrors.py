
#Exercício 1
while True:
    try:
        x1 = int(input("Digite um número inteiro: "))
        break
    except:
        print("Valor inválido")
print(x1)
print()
#Exercício 2
try:
    x2 = float(input("Digite o primeiro valor a ser multiplicado: "))
    y2 = float(input("Digite o segundo valor a ser multiplicado: "))
except:
    print("Algum valor inserido é inválido")
print(f"{x2*y2}\n")

#Exercício 3
x3 = input("Digite um número inteiro: ")
try:
    x3 = int(x3)
except:
    print("Disse que deveria ser inteiro")
print(x3)
print()

#Exercício 4(Cancelado)
with open("AtividadesEnvio/dados.txt", "r") as texto:
    try:
        escrito = texto.read()
    finally:
        print(escrito)
        print("encerrando programa")
print()

#Exercício 5
def divide(a, b):
    try:
        return a/b
    except:
        raise ValueError("ZeroDivisionError")

#Exercício 6
class IdadeInvalidaError(Exception):
    pass

def cadastrar_idade(idade):
    if idade < 0:
        raise IdadeInvalidaError("A idade não pode ser negativa!")
    
#Exercício 7
try:
    x7 = float(input("Digite o primeiro número a ser dividido: "))
    y7 = float(input("Digite o segundo número a ser dividido: "))
    print(x7/y7)
except ValueError:
        print("Valor inserido inválido")
except ZeroDivisionError:
        print("Não é possível dividir por zero")
except:
    print("Erro, contate o suporte.")
print()

#Exercício 8
try:
    x8 = float(input("Digite um número e verificarei se é impar ou par: "))
except:
    print("Digite um valor válido.")
else:
    if x8%2 == 0:
        print("É par")
    else:
        print("É impar")
finally:
    print("Fim do processo")
print()

#Exercício 9
class ErroDeSaque(Exception):
    pass

def sacar(saldo, valor):
    try:
        if valor > saldo:
            raise ErroDeSaque("SaldoInsuficienteError")
        else:
            saldo -= valor
            print(f"O novo saldo é de {saldo}")
    except:
        raise ValueError("Algum valor inserido é invalido")
