def bonus_1(l):
    maiorMeses = 0
    for _, meses, _ in l:
        if meses > maiorMeses:
            maiorMeses = meses
    
    for nome, meses, salario in l:
        if meses == maiorMeses:
            print(f'{nome}: {salario * 1.1:.2f}')