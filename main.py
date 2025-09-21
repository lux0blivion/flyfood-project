coordenadas = {}
def leituraMatriz(txt):
    with open(txt, 'r') as matrixTxt:
        linhas = matrixTxt.readlines()
        matriz  = [linha.strip().split() for linha in linhas]
        for y, subLista in enumerate(matriz):
            for x, valor in enumerate(subLista):
                 if valor not in ['0', '4', '5']:
                    if valor == 'R':
                        coordenadas['R'] = x, y
                    elif valor == 'A':
                        coordenadas['A'] = x, y
                    elif valor == 'B':
                        coordenadas['B'] = x, y
                    elif valor == 'C':
                        coordenadas['C'] = x, y
                    elif valor == 'D':
                        coordenadas['D'] = x, y


def calcDistanciaDoisPontos(dicionario):
    livroCoords = {}
    for key, value in dicionario.items():
        for chave, valor in dicionario.items():
            if key == chave:
                pass
            else:
                livroCoords[key + chave] = abs(value[0] - valor[0]) + abs(value[1] - valor[1])
    print(livroCoords)

leituraMatriz("matriz.txt")
calcDistanciaDoisPontos(coordenadas)
