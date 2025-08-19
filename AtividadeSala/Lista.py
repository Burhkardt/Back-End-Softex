"""
Teste
"""

#Exercício 1
listaum = ["String", 2, ["Uma lista de listas", "Hihi", 3]]

#Exercício 2
listaum.append("TesteA")
listaum[2].append("testeB")
listaum[2].remove("Hihi")
print(listaum)

#Exercício 3
listadois = listaum[:]
print(id(listaum) == id(listadois))

#Exercício 4
listatres = [1,1,1,1,1,1,1]
listaquatro = []
w=2
for i in range(len(listatres)):
    listaquatro.append(listatres[i]*5)
print(listatres)
print(listaquatro)

#Exercício 5
listacinco = [1,2,3,4,5,6]
listaseis = listacinco[3:5]
print(listaseis)