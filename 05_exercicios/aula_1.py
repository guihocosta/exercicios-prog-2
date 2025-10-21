def fat(x):
    if x == 0:
        return 1
    return x * fat(x-1)

def SomaLista(l):
    tam = len(l)
    if tam == 0:
        return 0
    
    return l[0] + SomaLista(l[1:])

def Fib(x):
    if x == 1 or x == 2:
        return 1
    return Fib(x-1) + Fib(x-2)