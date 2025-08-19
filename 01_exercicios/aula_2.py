def fibonacci(n):
    lista = [0, 1]
    for i in range(n):
        lista.append(lista[-1] + lista[-2])
    
    return lista[1:n+1]

def isPar(x):
    return x % 2 == 0

def cont(l, par):
    cont = 0
    for num in l:
        if isPar(num) == par:
            cont += 1
    return cont

def soma(l):
    soma = 0
    for num in l:
        soma += num
    return soma

def produto(l):
    mult = 0
    for num in l:
        mult *= num
    return mult

def ordenadas_abscissas(l1, l2):
    cont_a = cont(l1, True)
    cont_b = cont(l2, False)

    if cont_a > cont_b:
        print(soma(l1))
    else:
        print(produto(l2))

def multiplos(k, n):
    lista = [n]
    for i in range(k - 1):
        lista.append(lista[-1] + n)
    return lista
    
