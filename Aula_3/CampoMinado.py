import random
def CriaMatrizVazia(linhas, colunas, preenchimento=0):
    matriz=[]
    for i in range(linhas):
        matriz.append([])
        for j in range(colunas):
            matriz[i].append(preenchimento)
    return matriz
def SetaMinas(TamanhoMatriz, n_minas):
    matriz = CriaMatrizVazia(TamanhoMatriz, TamanhoMatriz)
    for i in range(n_minas):
        linha = random.randint(0, TamanhoMatriz - 1)
        coluna = random.randint(0, TamanhoMatriz - 1)
        if matriz[linha][coluna] == 0:
            matriz[linha][coluna] = "x"
        else:
            i -= 1
    return matriz
def MapeiaMinas(campo_oculto):
    for linha in range(len(campo_oculto)):
        for coluna in range(len(campo_oculto)):
            if campo_oculto[linha][coluna] != "x":
                contador = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= linha + i < len(campo_oculto) and 0 <= coluna + j < len(campo_oculto):
                            if campo_oculto[linha + i][coluna + j] == "x":
                                contador += 1
                campo_oculto[linha][coluna] = contador
    return campo_oculto
def Game(tamanho, minas):
    vida=1
    campo_oculto=MapeiaMinas(SetaMinas(tamanho, minas))
    campo_Player= CriaMatrizVazia(tamanho, tamanho, "O")
    checkcount=tamanho**2 - minas
    while vida>0:
        for l in range(len(campo_Player)):
            print()
            for col in range(len(campo_Player)):
                print(campo_Player[l][col], end=" ")
        print()
        linha= int(input("Digite a linha: "))
        coluna= int(input("Digite a coluna: "))
        try:
            if campo_oculto[linha][coluna]=="x":
                print("Você perdeu!")
                vida=0
            else:
                campo_Player[linha][coluna] = campo_oculto[linha][coluna]
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= linha + i < len(campo_oculto) and 0 <= coluna + j < len(campo_oculto):
                            if campo_oculto[linha + i][coluna + j] == 0:
                                campo_Player[linha + i][coluna + j] = campo_oculto[linha + i][coluna + j]
        except:
            print("Coordenada inválida!")
        c=0
        for x in range(len(campo_Player)):
            for y in range(len(campo_Player)):
                if campo_Player[x][y] == campo_oculto[x][y]:
                    c+=1
        if c==checkcount:
            print("Você ganhou!")
            vida=0
Game(4, 3)
