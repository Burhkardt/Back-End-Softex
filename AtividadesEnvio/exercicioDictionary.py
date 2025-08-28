#Exercício 1
aluno = {"Nome": "José", "Idade": 9, "Nota": 6.5 }
print(aluno)

#Exercício 2
produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}
print(f"Há {produto["estoque"]} unidade(s) do produto: {produto["nome"]}")

#Exercício 3
pessoa = {"nome": "Carlos", "idade": 30}
pessoa["cidade"] = "São Paulo"
print(pessoa)

#Exercício 4
carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
carro.pop("ano")
print(carro)

#Exercício 5
contato = {"nome": "Ana", "email": "ana@email.com"}
print(contato.__contains__("telefone"))

#Exercício 6
def ContaItens(lista):
    contagemDeItens = dict()
    listaOrg = list(lista)
    for item in listaOrg:
        contagemDeItens[item] = lista.count(item)
    return contagemDeItens
palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
print(ContaItens(palavras))

#Exercício 7
d = {"a": 1, "b": 2, "c": 3}
dInvertido = dict()
for i in d:
    dInvertido.update({d[i]: i})
print(dInvertido)


#Exercício 8
alunosMedia = {"José": [10,9,8], "Carlos": [6,4,8], "Marcelo": [9,3,7]}
for aluno in alunosMedia:
    media = sum(alunosMedia[aluno])/len(alunosMedia[aluno])
    print(f"O aluno(a) {aluno} tem a média: {media:.2}")

#Exercício 9
pessoa9 = {"nome": "Carlos", "idade": 30}
contato9 = {"nome": "Ana", "email": "ana@email.com"}
dictionary9 = pessoa9|contato9
print(dictionary9)

#Exercício 10
pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}

print(sorted(pontuacoes.items(), key=lambda item: item[1]))