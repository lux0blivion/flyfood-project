coordenadas = {}
def leituraMatriz(txt):
    with open(txt, 'r') as matrixTxt:
        linhas = matrixTxt.readlines()
        matriz  = [linha.strip().split() for linha in linhas]
        for y, subLista in enumerate(matriz):
            for x, valor in enumerate(subLista):
                 if not valor.isdigit():
                        coordenadas[valor] = x + 1, y
                    

#Dicionario com os valores da distancia entre cada par de pontos
def calcDistanciaDoisPontos(dicionario):
    livroCoords = {}
    for key, value in dicionario.items():
        for chave, valor in dicionario.items():
            if key == chave:
                pass
            else:
                livroCoords[key + chave] = abs(value[0] - valor[0]) + abs(value[1] - valor[1])
    print(livroCoords)
    return livroCoords

leituraMatriz("matriz.txt")
calcDistanciaDoisPontos(coordenadas)
