def criar_matriz_17(m, n):
    l = []
    for i in range(m):
        l.append([0] * n)
    return l

def imprimir_matriz_18(m):
    for linha in m:
        for coluna in linha:
            print(coluna, end=" \t")
        print()

def somar_matrizes_19(a, b):
    n_linhas = len(a)
    n_colunas = len(a[0])

    c = criar_matriz_17(n_linhas, n_colunas)

    for i in range(n_linhas):
        for j in range(n_colunas):
            c[i][j] = a[i][j] + b[i][j]
    
    return c

def calcular_media_20(l):
    soma = 0
    for x in l:
        soma += x
    return soma/len(l)


def notas_20():

    qtd_alunos = int(input())
    qtd_notas = int(input())
    soma_geral = 0.0

    matriz = criar_matriz_17(qtd_alunos, qtd_notas)
    for i in range(qtd_alunos):
        for j in range(qtd_notas):
            nota = float(input())
            matriz[i][j] = nota
    
    for i in range(len(matriz)):
        media_aluno = calcular_media_20(matriz[i])
        soma_geral += media_aluno
        print(f'Aluno {i+1}: {media_aluno}')
    
    if qtd_alunos != 0:
        print(f'Média da turma: {soma_geral/qtd_alunos}')

def matriz_identidade_21(m):

    nLinhas = len(m)
    
    for i in range(nLinhas):
        if len(m[i]) != nLinhas:
            return False
        for j in range(nLinhas):
            elemento = m[i][j]
            if i == j:
                if elemento != 1:
                    return False
            elif elemento != 0:
                    return False
    return True

def determinante_22(matriz):
    positivos = (matriz[0][0] * matriz[1][1] * matriz[2][2] +
                 matriz[0][1] * matriz[1][2] * matriz[2][0] +
                 matriz[0][2] * matriz[1][0] * matriz[2][1])

    negativos = (matriz[0][2] * matriz[1][1] * matriz[2][0] +
                 matriz[0][0] * matriz[1][2] * matriz[2][1] +
                 matriz[0][1] * matriz[1][0] * matriz[2][2])

    determinante = positivos - negativos
    return determinante

def transposta_23(m):
    n = len(m)
    for i in range(n):
        for j in range(i + 1, n):
            m[i][j], m[j][i] = m[j][i], m[i][j]

def triangular_inferior_23(M):
    n = len(M)

    transposta_23(M)

    for i in range(n):
        for j in range(n):
            if j > i:
                M[i][j] = 0

def cavalo_24(m):
    posicao_cavalo = ()
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 1:
                posicao_cavalo = i, j
    print(posicao_cavalo)

xadrez = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
]

cavalo_24(xadrez)



