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

def cavalo_24(matriz_m):
    posicao_cavalo = None
    for i in range(8):
        for j in range(8):
            if matriz_m[i][j] == 1:
                posicao_cavalo = (i, j)

    if posicao_cavalo is None:
        return

    linha_cavalo, coluna_cavalo = posicao_cavalo

    movimentos_possiveis = [
        (-2, -1), (-2, 1),
        (2, -1), (2, 1),
        (-1, -2), (1, -2),
        (-1, 2), (1, 2)
    ]

    contador_movimentos_validos = 0

    for dl, dc in movimentos_possiveis:
        nova_linha = linha_cavalo + dl
        nova_coluna = coluna_cavalo + dc

        if 0 <= nova_linha < 8 and 0 <= nova_coluna < 8:
            contador_movimentos_validos += 1

    print(contador_movimentos_validos)

def robo_24(arena, instrucoes):
    num_linhas = len(arena)
    num_colunas = len(arena[0])

    movimentos = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    pos_linha = -1
    pos_coluna = -1
    orientacao_atual = -1
    
    robo_encontrado = False
    
    i = 0
    while i < num_linhas and not robo_encontrado:
        j = 0
        while j < num_colunas and not robo_encontrado:
            celula = arena[i][j]          
            if celula == 'N' or celula == 'L' or celula == 'S' or celula == 'O':
                pos_linha = i
                pos_coluna = j

                if celula == 'N':
                    orientacao_atual = 0
                elif celula == 'L':
                    orientacao_atual = 1
                elif celula == 'S':
                    orientacao_atual = 2
                elif celula == 'O':
                    orientacao_atual = 3            
                arena[i][j] = '.'
                robo_encontrado = True
            j += 1
        i += 1

    figurinhas_coletadas = 0

    for instrucao in instrucoes:
        if instrucao == 'D':
            orientacao_atual = (orientacao_atual + 1) % 4
        elif instrucao == 'E':
            orientacao_atual = (orientacao_atual - 1 + 4) % 4
        elif instrucao == 'F':
            delta_linha, delta_coluna = movimentos[orientacao_atual]
            proxima_linha = pos_linha + delta_linha
            proxima_coluna = pos_coluna + delta_coluna

            if 0 <= proxima_linha < num_linhas and 0 <= proxima_coluna < num_colunas:
                if arena[proxima_linha][proxima_coluna] != '#':
                    pos_linha = proxima_linha
                    pos_coluna = proxima_coluna

                    if arena[pos_linha][pos_coluna] == '*':
                        figurinhas_coletadas += 1
                        arena[pos_linha][pos_coluna] = '.'
    return figurinhas_coletadas
