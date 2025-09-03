#Exercício 1
print("Exercício 1:")
ExercicioUm = "123"
print(ExercicioUm)
ExercicioUm = float(ExercicioUm)
print(ExercicioUm)
print("\n")



#Exercício 2
print("Exercício 2:")
ExercicioDois = "Python é incrível!"
print(len(ExercicioDois))
print(ExercicioDois.upper())
print(ExercicioDois.replace("incrível", "poderoso"))
print("\n")



#Exercício 3
print("Exercício 3:")
ExercicioTres = [10,20,30,40,50]
print(ExercicioTres[2])
ExercicioTres.append(60)
ExercicioTres.pop(1)
print(ExercicioTres)
print("\n")



#Exercício 4
print("Exercício 4:")
aluno = {"nome": "Maria", "Idade": 22, "curso": "Engenharia"}
aluno["notas"] = [8.5, 7.0, 9.2]
print(aluno["curso"])
print("\n")



#Exercício 5
print("Exercício 5:")
cores = ("vermelho", "verde", "azul", "verde")
cores = list(set(cores))
cores.append("amarelo")
print(cores)
print("\n")




#Exercício 6
print("Exercício 6:")
a=15
b=4
print(int(a/b))
print(a%b)
print("\n")



#Exercício 7
print("Exercício 7:")
ExercicioSete = [42, 3.14, "Python", True, [1,2]]
for i in ExercicioSete:
    print(type(i))
print("\n")



#Exercício 8
print("Exercício 8:")
ExercicioOito = "programação"
ExercicioOitoInverso = ExercicioOito[::-1]
print(ExercicioOitoInverso)
print(ExercicioOito == ExercicioOitoInverso)
print("\n")



#Exercício 9
print("Exercício 9:")
ExercicioNove = [[1,2,3],[4,5,6],[7,8,9]]
print(ExercicioNove[1][1])
ExercicioNove[2][1] = 10
print(ExercicioNove)
print("\n")



#Exercício 10
print("Exercício Final:")
ExercicioDez = {"maçã": 10, "banana": 5, "laranja": 8}
ExercicioDez["pera"] = 12
print(ExercicioDez)
ExercicioDez.pop("banana")
print(ExercicioDez.keys())