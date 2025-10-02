from functools import reduce

#exercicio1
listaex1 = [1, 2, 3, 4, 5]
lista2ex1=list(map(lambda x: x*2, listaex1))
print(lista2ex1)

#exercicio2
listaex2 = [1, 2, 3, 4, 5]
print(reduce(lambda x,y: x+y, listaex2))

#exercicio3
listaex3 = ["uva", "banana", "maçã", "laranja"]
print(sorted(listaex3, key=lambda x: len(x)))

#Exercicio 4
listaex4 = ["ana", "pedro", "maria"]
print(list(map(lambda x: x.capitalize(), listaex4)))

#Exercicio 5
listaex5 = [2, 3, 4, 5]
print(reduce(lambda x,y: x*y, listaex5))

#Exercicio 6
listaex6 = ["banana", "uva", "maçã", "laranja"]
print(sorted(listaex6, key= lambda x: x[::-1]))