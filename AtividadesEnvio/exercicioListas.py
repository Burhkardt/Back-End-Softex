# Exercício 1
livros = ["Dom Quixote de La Mancha","O Pequeno Príncipe","A Casa dos Espíritos"]
print(livros)
print("\n")

#Exercício 2
print(livros[0]+" e "+livros[2]+ "\n\n")

#Exercício 3
livros.append("Um Conto de Duas Cidades")
livros.append("O Senhor dos Anéis")
print(livros)
print("\n")

#Exercício 4
livros.insert(1, "Duna")
print(livros)
print("\n")

#Exercício 5
try:
    livros.remove("Silêncio dos inocentes")
except:
    print("Livro não encontrado.\n\n")

#Exercício 6
numeros = [1, 2, 3, 2, 4, 2, 5]
print(numeros.count(2))
print("\n")

#Exercício 7
for i in livros:
    print(f"O livro {i} é interessante \n\n")

#Exercício 8
idades = [12, 18, 25, 14, 30]
maioridade = []
for i in idades:
    if i >= 18:
        maioridade.append(i)
print(maioridade)
del(maioridade)
print("\n")

#Exercício 9
valores = [10, 20, 30, 40]
somaVal = 0
for i in valores:
    somaVal+=i
print (somaVal)

#Exercício 10
notaAluno1 = [int(input("Digite a primeira nota do primeiro aluno: "))]
for i in range(2,4):
    notaAluno1.append(int(input(f"Digite a {i}ª nota do primeiro aluno: ")))
notaAluno2 = [int(input("Digite a primeira nota do segundo aluno: "))]
for i in range(2,4):
    notaAluno2.append(int(input(f"Digite a {i}ª nota do segundo aluno: ")))
notas = [notaAluno1, notaAluno2]
media1 = 0
for i in notaAluno1:
    media1 += i
media1 = media1/len(notaAluno1)
print(media1)
media2 = 0
for i in notaAluno2:
    media2 += i
media2 = media2/len(notaAluno1)
print(media2)

#exercício 11

tabuleiro = []
for c in range(8):
    tabuleiro.append([])
    for l in range(8):
        if (c == 0 or c == 7):
            if l == 0 or l == 7:
                tabuleiro[c].append("Tor")
            elif l == 1 or l == 6:
                tabuleiro[c].append("cav")
            elif l == 2 or l == 5:
                tabuleiro[c].append("bis")
            elif (c == 0 and l == 4) or (c == 7 and l == 3):
                tabuleiro[c].append("rei")
            else:
                tabuleiro[c].append("rai")
        elif c == 1 or c == 6:
            tabuleiro[c].append("pea")
        else:
            tabuleiro[c].append("[]")
for i in range(len(tabuleiro)):
    for l in tabuleiro[i]:
        print(l , end="  ")
    print("\n")