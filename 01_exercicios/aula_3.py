def entrada_lista(n):

    lista = []

    for i in range(n):
        valor = float(input())
        lista.append(valor)

    return lista 

def media_alunos():
    n = int(input())
    lista = entrada_lista(n)
    cont = int()

    soma = float()

    for nota in lista:
        if nota >= 60:
            cont += 1 
        soma += nota
    
    print("Média da nota dos alunos: %s", soma / len(lista))
    print("Quantidade de alunos com nota igual ou maior que 60: %s", cont)

def media(l):
    soma = 0
    for valor in l:
        soma += valor
    return soma / len(l)

def temperaturas():

    n = int(input())
    cont = int()
    lista = entrada_lista(n)

    media_anual = media(lista)
    for temp in lista:
        if temp < media_anual:
            cont += 1
    
    print("Quantidade de dias em que a temperatura ficou abaixo da média: %s", cont)

def iguais(l1, l2):

    cont = 0
    for i in range(len(l1)):
        if l1[i] == l2[i]:
            cont += 1
    
    print(cont)

def salarios(n):
    l1 = []
    l2 = []

    for i in range(n):
        nome = input()
        salario = float(input())
        l1.append(nome)
        l2.append(salario)
    
    media = media(l2)
    for i in range(len(l1)):
        if l2[i] > media:
            print(l1[i])

def sublista(l, x, y):
    l2 = []
    for item in l:
        if item >= x and item <= y:
            l2.append(item)
    return l2

def sem_repeticoes(l):
    l2 = [l[0]]
    for item in l:
        if item != l2[-1]:
            l2.append(item)
    return l2
            

def troca_cartas(l1, l2):
    cont_1 = 0
    cont_2 = 0
    l1 = sem_repeticoes(l1)
    l2 = sem_repeticoes(l2)
    print(l1, l2)
    for carta in l1:
        if carta not in l2:
            cont_1 += 1
    
    for carta in l2:
        if carta not in l1:
            cont_2 += 1
    
    print(min(cont_1, cont_2))
    







    
