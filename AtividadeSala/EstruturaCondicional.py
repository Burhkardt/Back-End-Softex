print("Exercício 1:\n")
dadoum = int(input("Digite um número inteiro, e direi par ou impar: "))
if dadoum%2 == 0:
    print("O número é par.")
else:
    print("O número é impar")
print("\n")

#Exercício 2
print("Exercício 2:\n")
dadodois = float(input("Digite a nota do aluno: "))
if dadodois >= 7:
    print("Aprovado")
elif 5 < dadodois < 6.9:
    print("Recuperação")
else:
    print("Reprovado")
print("\n")

#Exercício 3
print("Exercício 3:\n")
print("Digite dois números e eu direi qual deles é maior")
dadotresA = float(input("Primeiro número: "))
dadotresB = float(input("Segundo número: "))

if dadotresA > dadotresB:
    print("O primeiro número é maior.")
elif dadotresB > dadotresA:
    print("O segundo número é maior.")
else:
    print("Os números são iguais")
print("\n")

#Exercício 4
print("Exercício 4:\n")
dadoquatro = int(input("Digite a idade em anos: "))
if dadoquatro < 0:
    print("Nem nasceu ainda")
if dadoquatro <= 12:
    print("Criança")
elif 13 <= dadoquatro <= 17:
    print("Adolescente")
elif 18 <= dadoquatro <= 64:
    print("Adulto")
else:
    print("Idoso")
print("\n")

#Exercício 5
print("Exercício 5:\n")
for i in range(1,11):
    print(i)
print("\n")

#Exercício 6
print("Exercício 6")
dadoseis = int(input("Qual tabuada você quer? "))
for i in range(11):
    print(f"{dadoseis} x {i} = {dadoseis*i}")
print("\n")

#Exercício 7
print("Exercício 7")
check = 1
dadosete = 0
while check != 0:
    soma = float(input("Digite o número a ser somado (Digite 0 para finalizar):"))
    if soma != 0:
        dadosete = dadosete+soma
    else:
        check = 0

print(dadosete)