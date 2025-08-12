# Fundamentos da Programação

def fat(x):
    if x == 0:
        return 1
    else:
        return x * fat(x - 1)

def combinacao(n, p):
    return fat(n) / (fat(p) * fat(n - p))

def multiplos(n, k):
    i = 1
    while i <= n:
        print(k * i)
        i += 1

def divisor(x, y):
    return y % x == 0

def divisores(k):
    i = 1
    while i <= k:
        if divisor(i, k):
            print(i)
        i += 1

def mdc(m, n):
    i = m
    while i > 0:
        if divisor(i, m) and divisor(i, n):
            print(i)
            return 
        i -= 1
    return

def primo(x):

    if x == 1:
        return False
    
    i = 2
    while i < x:
        if x % i == 0:
            return False
        i += 1
    return True 

def primos(k):
    i = 2
    while i <= k:
        if primo(i):
            print(i)
        i += 1

def mesma_posicao(x, y, m, n):
    return x == m and y == n

def alinhados(x, y, m, n):
    return x == m or y == n or abs((x-m)) == abs((y-n))
    
def dama(x, y, m, n):

    if mesma_posicao(x, y, m, n):
        return 0
    elif alinhados(x, y, m, n):
        return 1
    else:
        return 2

def acerola(n, f):
    producao_suco_unid_ml = 50

    qtd_suco_litro = (producao_suco_unid_ml * f) / 1000
    qtd_por_amigo = qtd_suco_litro / n

    print(f'{qtd_por_amigo:.2f}')

def alarme_despertador(hora_atual, minuto_atual, hora_alarme, minuto_alarme):
    t1 = hora_atual * 60 +  minuto_atual
    t2 = hora_alarme * 60 + minuto_alarme

    if t1 < t2:
        return(t2-t1)
    else:
        return(24 * 60 + t2-t1)