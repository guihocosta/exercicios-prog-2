def bonus_1(l):
    maiorMeses = 0
    for _, meses, _ in l:
        if meses > maiorMeses:
            maiorMeses = meses
    
    for nome, meses, salario in l:
        if meses == maiorMeses:
            print(f'{nome}: {salario * 1.1:.2f}')

def lucro_2(prod):
    menos_20_lucro = 0
    mais_25_lucro = 0

    for custo, venda in prod:
        if venda < (custo * 1.2):
            menos_20_lucro += 1
        elif venda > (custo * 1.25):
            mais_25_lucro += 1
    
    print("A quantidade de produtos com menos de 20% de lucro é", menos_20_lucro)
    print("A quantidade de produtos com lucro superior a 25% é", mais_25_lucro)

def alinhados_3(p1, p2, p3):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3

    resultado_determinante = (y2 - y1) * (x3 - x2) - (y3 - y2) * (x2 - x1)
    return resultado_determinante == 0

def turismo_a_4(a, b, voos):
    for numero, companhia, escalas in voos:
        if escalas[0] == a and escalas[-1] == b:
            print(numero, companhia)

def turismo_b_4(a, b, voos):
    for numero, companhia, escalas in voos:
        if escalas[0] == a and b in escalas:
            print(numero, companhia)

def turismo_c_4(a, b, voos):
    for numero, companhia, escalas in voos:
        for i in range(len(escalas) - 1):
            if escalas[i] == a and escalas[i+1] == b:
                print(numero, companhia)

def copa_do_mundo_5(qtd_jogos, classificacao):
    pontos_totais = 0
    for _, pontos in classificacao:
        pontos_totais += pontos
    return (3 * qtd_jogos - pontos_totais)






