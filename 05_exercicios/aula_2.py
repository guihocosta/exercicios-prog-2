def exp_rec_1(x, n):
    if x == 0:
        return 1
    return n * exp_rec_1(x-1, n)

def maior_elem_rec_2(l):
    if len(l) == 1:
        return l[0] 
    primeiro_elem = l[0]
    maior_do_resto = maior_elem_rec_2(l[1:])
    if primeiro_elem > maior_do_resto:
        return primeiro_elem
    else:
        return maior_do_resto

def mdc_rec_3(a, b):
    if b == 0:
        return a
    return mdc_rec_3(b, a % b)

def inverte_4(x):
    if x // 10 == 0:
        print(x)
    else:
        print(x%10, end='')
        inverte_4(x//10)
