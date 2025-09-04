#Exercício 1
def saudacao():
    print("Olá, bem-vindo ao Python!")
saudacao()
print()

#Exercício 2
def dobro(num):
    return num*2
print(dobro(4))
print(dobro(5))
print()

#Exercício 3
def soma(*x):
    result = 0
    for i in x:
        result += i
    return result
print(soma(10,20))
print()

#Exercício 4
def mensagem(a = "visitante"):
    return f"Olá, {a}!"
print(mensagem())
print()

#Exercício 5
def operacoes(a, b):
    return f"Soma = {a+b}\nSubtração = {a-b}\nMultiplicação = {a*b}"
print(operacoes(1,2))
print()

#Exercício 6
def media(*x):
    try:
        return sum(x)/len(x)
    except:
        return "Proibido divisão por zero"

print(media(10, 20, 30))
print(media(5, 10, 15, 20, 25))
print(media(1, 2, 3, 4, 5, 6, 7))
print(media())
print()

#Exercício 7
def dados_pessoais(**dados):
    for i,j in dados.items():
        print(f"{i}: {j}")
dados_pessoais(nome="Ana", idade=25, cidade="Recife")
print()

#Exercício 8
def subtrai(x,y):
    return x-y

def multiplica(x,y):
    return x*y

def divide(x,y):
    if y != 0:
        return x/y
    else:
        return "Proibido dividir por zero"

def calculadora():
    while True:
        a = input("O que desejas fazer:\n" \
              "Somar: digite 1\n" \
              "subtrair: digite 2\n" \
              "multiplicar: digite 3\n" \
              "dividir: digite 4\n" \
              "Cancelar: digite 0\n")
        match a:
            case "1":
                x = float(input("Digite o 1º número: "))
                y = float(input("Digite o 2º número: "))
                return soma(x,y)
            case "2":
                x = float(input("Digite o 1º número: "))
                y = float(input("Digite o 2º número: "))
                return subtrai(x,y)
            case "3":
                x = float(input("Digite o 1º número: "))
                y = float(input("Digite o 2º número: "))
                return multiplica(x,y)
            case "4":
                x = float(input("Digite o 1º número: "))
                y = float(input("Digite o 2º número: "))
                return divide(x,y)
            case "0":
                break
            case __:
                print("Escolha uma opção válida\n")
print(calculadora())

#Exercício 9
def aplicar_operacao(x, y, op):
    return op(x,y)


print(aplicar_operacao(3, 4, soma))