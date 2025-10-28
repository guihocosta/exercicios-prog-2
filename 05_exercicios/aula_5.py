import random, matplotlib.pyplot as plt

'''
Funcoes para visualizar um caminho do TSP na tela
'''

def showTSP(caminho, titulo):
	xs = [coords[0] for (cidade, coords) in caminho]
	ys = [coords[1] for (cidade, coords) in caminho]
	nomes = [cidade for (cidade, coords) in caminho]
	
	for i in range(len(xs)):
		plt.annotate(nomes[i], # this is the text
						(xs[i],ys[i]), # this is the point to label
						textcoords="offset points", # how to position the text
						xytext=(5,5), # distance from text to points (x,y)
						ha='center') # horizontal alignment can be left, right or center

	plt.plot(xs+[xs[0]], ys+[ys[0]], 'pb-')
	plt.plot([xs[0]], [ys[0]], 'pb-', color='red')
	
	t = "{} (Custo: {:.2f})".format(titulo, custo(caminho))
	plt.suptitle(t)
	plt.gca().set_aspect('equal', adjustable='box')
	
	plt.show()


'''
Permutacoes
'''

def troca(l, x, y):
	aux = l[x]
	l[x] = l[y]
	l[y] = aux

def perms(l, pos=0, r=[]):
	if pos == len(l)-1:
		r.append(l.copy())
	else:
		for i in range(pos, len(l)):
			troca(l, pos, i)
			perms(l, pos+1, r)
			troca(l, pos, i)
		
		return r
		

def dist(p1, p2):
	x1 = p1[1][0]
	y1 = p1[1][1]
	x2 = p2[1][0]
	y2 = p2[1][1]
	
	return ( (x1-x2)**2 + (y1-y2)**2 ) ** 0.5

def custo(caminho):
	c = 0
	
	for i in range(len(caminho) - 1):
		c += dist(caminho[i], caminho[i+1])
		
	c += dist(caminho[-1], caminho[0])

	return c
	

def tsp(caminhos):
	melhor = caminhos[0]
	
	for caminho in caminhos:
		if custo(caminho) < custo(melhor):
			melhor = caminho
	
	return melhor
	
def nn(l):
	
	atual = 0
	while atual < len(l) - 2:
		maisPerto = atual+1
		for i in range(atual+2, len(l)):
			if dist(l[atual], l[i]) < dist(l[atual], l[maisPerto]):
				maisPerto = i
		
		l[atual+1], l[maisPerto] = l[maisPerto], l[atual+1]
		atual += 1
	
def gerarCidades():
	n = int(input("Digite o número de cidades: "))
	
	cidades = []
	
	for i in range(n):
		nome = chr(ord("A")+i)
		x = random.randint(0, 400)
		y = random.randint(0,300)
		cidade = ( nome, (x, y) )
		cidades.append(cidade)
	
	return cidades

import random
import matplotlib.pyplot as plt
import sys

'''
Funcoes para visualizar um caminho do TSP na tela
'''

def showTSP(caminho, titulo):
    # Extrai coordenadas e nomes para plotagem
    xs = [coords[0] for (cidade, coords) in caminho]
    ys = [coords[1] for (cidade, coords) in caminho]
    nomes = [cidade for (cidade, coords) in caminho]
    
    # Adiciona anotações com os nomes das cidades
    for i in range(len(xs)):
        plt.annotate(nomes[i], # this is the text
                     (xs[i],ys[i]), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(5,5), # distance from text to points (x,y)
                     ha='center') # horizontal alignment can be left, right or center

    # Plota o caminho (fechando o ciclo) e destaca a cidade inicial
    plt.plot(xs+[xs[0]], ys+[ys[0]], 'pb-')
    plt.plot([xs[0]], [ys[0]], 'pb-', color='red')
    
    # Configura o título com o custo total
    t = "{} (Custo: {:.2f})".format(titulo, custo(caminho))
    plt.suptitle(t)
    plt.gca().set_aspect('equal', adjustable='box')
    
    plt.show()


'''
Funcoes de apoio e algoritmos existentes
'''

def troca(l, x, y):
    aux = l[x]
    l[x] = l[y]
    l[y] = aux

def perms(l, pos=0, r=[]):
    if pos == len(l)-1:
        r.append(l.copy())
    else:
        for i in range(pos, len(l)):
            troca(l, pos, i)
            perms(l, pos+1, r)
            troca(l, pos, i)
        
        return r

def dist(p1, p2):
    x1 = p1[1][0]
    y1 = p1[1][1]
    x2 = p2[1][0]
    y2 = p2[1][1]
    
    return ( (x1-x2)**2 + (y1-y2)**2 ) ** 0.5

def custo(caminho):
    c = 0
    for i in range(len(caminho) - 1):
        c += dist(caminho[i], caminho[i+1])
    c += dist(caminho[-1], caminho[0]) # Volta para a origem
    return c

def tsp(caminhos):
    melhor = caminhos[0]
    for caminho in caminhos:
        if custo(caminho) < custo(melhor):
            melhor = caminho
    return melhor
    
def nn(l):
    atual = 0
    while atual < len(l) - 2:
        maisPerto = atual+1
        for i in range(atual+2, len(l)):
            if dist(l[atual], l[i]) < dist(l[atual], l[maisPerto]):
                maisPerto = i
        
        l[atual+1], l[maisPerto] = l[maisPerto], l[atual+1]
        atual += 1
    
def gerarCidades():
    try:
        n = int(input("Digite o número de cidades: "))
    except ValueError:
        print("Entrada inválida. Usando 15 cidades.")
        n = 15

    cidades = []
    for i in range(n):
        nome = chr(ord("A")+i)
        x = random.randint(0, 400)
        y = random.randint(0,300)
        cidade = ( nome, (x, y) )
        cidades.append(cidade)
    
    return cidades

def algoritmo_2opt_sem_break(caminho_inicial):
    melhor_caminho = caminho_inicial.copy()
    num_cidades = len(melhor_caminho)
    houve_melhora = True
    
    while houve_melhora:
        houve_melhora = False
        
        for i in range(1, num_cidades - 1):
            for j in range(i + 1, num_cidades):
                
                p_i_anterior = melhor_caminho[i-1]
                p_i = melhor_caminho[i]
                p_j = melhor_caminho[j]
                p_j_proximo = melhor_caminho[(j + 1) % num_cidades] 
                
                custo_antigo = dist(p_i_anterior, p_i) + dist(p_j, p_j_proximo)
                custo_novo = dist(p_i_anterior, p_j) + dist(p_i, p_j_proximo)
                
                if custo_novo < custo_antigo:
                    melhor_caminho[i : j+1] = melhor_caminho[i : j+1][::-1]
                    
                    houve_melhora = True
                    
    return melhor_caminho


def main(args):
    
    cidades = gerarCidades()
    
    showTSP(cidades, "Ordem Inicial")
    
    cidades1 = cidades.copy()
    nn(cidades1)
    showTSP(cidades1, "Vizinho Mais Proximo")

    cidades_2opt = algoritmo_2opt(cidades1)
    showTSP(cidades_2opt, "Otimizacao 2-opt")
    
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))

