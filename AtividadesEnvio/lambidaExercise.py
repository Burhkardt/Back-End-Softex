from functools import reduce

#exercicio1
listaex1 = [1, 2, 3, 4, 5]
lista2ex1=list(map(lambda x: x*2, listaex1))
print(lista2ex1)

#Exercicio 2
listaex2 = [10, 15, 20, 25, 30]
print(list(filter(lambda x: x%2 == 0, listaex2)))

#exercicio3
listaex3 = [1, 2, 3, 4, 5]
print(reduce(lambda x,y: x+y, listaex3))

#exercicio4
listaex4 = ["uva", "banana", "maçã", "laranja"]
print(sorted(listaex4, key=lambda x: len(x)))

#Exercicio 5
listaex5 = ["ana", "pedro", "maria"]
print(list(map(lambda x: x.capitalize(), listaex5)))

#Exercicio 6
listaex6 = [2, 3, 4, 5]
print(reduce(lambda x,y: x*y, listaex6))

#Exercicio 7
listaex7 = ["banana", "uva", "maçã", "laranja"]
print(sorted(listaex7, key= lambda x: x[::-1]))