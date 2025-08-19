def regressiva():
    return [n for n in range(100, 0, -2)]

def metade():
    lista = list()
    for i in range(10):
        lista.append(float(input()) / 2)
    
def leitura(n):
    lista = list()
    for i in range(n):
        lista.append(float(input()))
    return lista

def ocorrencias(elem, lista):
    # cont = 0
    # for item in lista:
    #     if elem == item:
    #         cont += 1
    # return cont 
    return lista.count(elem)

      # outra forma de fazer

def maximo(lista):
    # maior = lista[0]
    # for num in lista:
    #     if num > maior:
    #         maior = num
    # return maior
    return max(lista)

def posicao_maximo(lista):
    maior_indice = 0
    for i in range(len(lista)):
        if lista[i] > lista[maior_indice]:
            maior_indice = i
    return maior_indice

def inverter(lista):
    # lista_2 = list()
    # for i in range(len(lista)-1, -1, -1):
    #     lista_2.append(lista[i])
    # return lista_2
    lista.reverse()

