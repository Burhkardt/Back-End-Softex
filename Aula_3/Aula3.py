print("Exercício 1:")
print("Olá, Mundo!\n\n")
print("Exercício 2:")
print("O rato roeu a roupa do rei de Roma.")
print("Três pratos de trigo para três tigres tristes.")
print("Bottom text.\n\n")
print("Exercício 3:")
print("Nome:    João\n"\
      "Idade:   20 Anos\n"\
      "Curso:   Python Básico\n\n")
print("Exercício 4:")
nome = "Juliandre"
idade = 23
curso = "Python"
print(f"Nome:   {nome}\n"\
      f"Idade:  {idade}\n"\
      f"Curso:  {curso}\n\n")
print("Exercício 5:")
def FazQuadrado(x,y):
    for i in range(x):
        print()
        for j in range(y):
            if i==0 or j==0 or i == x-1 or j == y-1:
                print("#", end="")
            else:
                print(" ", end="")
    print()
FazQuadrado(10,20)