import os

def limpaTela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

import random

def SalvarArquivo(qtdJogadas):
    f = open("resultados_genius.txt", "a")
    f.write(str(qtdJogadas) + "\n")
    f.close()

def MaiorPontuacao():
    f = open("resultados_genius.txt", "r")
    maior = 0
    for linha in f:
        linha_limpa = int(linha.strip())
        if linha_limpa > maior:
            maior = linha_limpa
    f.close()
    return maior

def Genius1():
    qtdJogadas = 0
    sequencia = ""
    fraseUsuario = ""
    while sequencia == fraseUsuario:
        num = random.randint(0, 9)
        sequencia += str(num)
        print(num)
        fraseUsuario = input()
        qtdJogadas += 1
        limpaTela()

    SalvarArquivo(qtdJogadas - 1)
    print('A quantidade de jogadas foi', qtdJogadas - 1)
    print("A maior quantidade de jogadas até o momento foi", MaiorPontuacao())

def cadastrar_telefone(agenda):
    nome = input("Nome: ")
    telefone = input("Telefone: ")

    agenda[nome] = telefone

def visualizar_agenda(agenda):
    for contato in agenda:
        print(f'{contato}:\t{agenda[contato]}')

import pickle

def SalvarArquivoAgenda(agenda):
    

    with open("agenda_bin", "wb") as f:
        pickle.dump(agenda, f)

def LerArquivoAgenda():
    with open("agenda_bin", "rb") as f:
        agenda = pickle.load(f)
    return agenda

def Agendas2():
    menu = '''
[1] Cadastrar telefone
[2] Visualizar agenda
    '''

    try:
        agenda = LerArquivoAgenda()
    except Exception:
        agenda = {}

    op = int(input(menu))
    limpaTela()

    while op in [1, 2]:

        if op == 1:
            cadastrar_telefone(agenda)
            SalvarArquivoAgenda(agenda)
        elif op == 2:
            visualizar_agenda(agenda)

        op = int(input(menu))
        limpaTela()
    print("Obrigado por usar o meu programa!")

import pickle
import os

def salvar_dados(jogadores, apostas):
    with open('jogadores.dat', 'wb') as f_jogadores:
        pickle.dump(jogadores, f_jogadores)
    
    with open('apostas.dat', 'wb') as f_apostas:
        pickle.dump(apostas, f_apostas)
            
def carregar_dados():
    with open('jogadores.dat', 'rb') as f_jogadores:
        jogadores = pickle.load(f_jogadores)
        
    with open('apostas.dat', 'rb') as f_apostas:
        apostas = pickle.load(f_apostas)
        
    print("Dados carregados com sucesso!")
    return jogadores, apostas

def existeCPF(cpf, jogadores):
    for (c, _) in jogadores:
        if c == cpf: return True
    
    return False
    
def inserirJogador(jogadores):
    nome = input("Nome: ")
    cpf = input("CPF: ")
    
    if existeCPF(cpf, jogadores):
        print("Jogador repetido. Cadastro não realizado.")
    else:
        jogadores.append( (cpf, nome) )
        print("Jogador cadastrado com sucesso.")
    
def visualizarJogadores(jogadores):
    if len(jogadores) == 0:
        print("Nenhum jogador cadastrado ainda.")
    else:
        print("Jogadores:")
        
        for (cpf, nome) in jogadores:
            print(f"{nome} - (CPF: {cpf})")

def inserirCPFs(jogadores):
    n = int(input("Quantos jogadores? "))
    cpfs = []
    
    while n < 1 or n > len(jogadores):
        n = int(input("Número inválido. Tente novamente: "))
    
    while len(cpfs) != n:
        visualizarJogadores(jogadores)
        cpf = input("Digite um cpf: ")
        
        if existeCPF(cpf, jogadores) and cpf not in cpfs:
            cpfs.append(cpf)
        else:
            print("CPF inválido.")
    
    return cpfs
   
def inserirNumeros():
    numeros = []
    
    n = int(input("Quantos números nessa aposta? "))
    
    while n < 6 or n > 15:
        n = int(input("Número inválido. Tente novamente: "))
        
    while len(numeros) < n:
        x = int(input("Digite um número apostado neste cartão: "))
        
        if x >= 1 and x <= 60 and x not in numeros:
            numeros.append(x)
        else:
            print("Número inválido, seu burro.")
            
    return numeros

def inserirAposta(jogadores, apostas):
    cpfs = inserirCPFs(jogadores)
    numeros = inserirNumeros()
    
    apostas.append( (cpfs, numeros) )
  
def getName(cpf, jogadores):
    for (c, n) in jogadores:
        if c == cpf: return n
    return None
    
def visualizarApostas(jogadores, apostas):
    if len(apostas) == 0:
        print("Nenhuma aposta cadastrada.")
    else:
        i = 1
        for (cpfs, numeros) in apostas:
            print(f"Aposta {i}\n")
            
            print("Números:", end=" ")
            
            for num in numeros: 
                print(num, end=" ")
            
            print("\n")
            
            print("Jogadores:")
            for cpf in cpfs:
                print(f"{getName(cpf, jogadores)} - (cpf: {cpf})")
            
            i += 1
            
            print("\n*************************\n")

def lerSorteados():
    numeros = []
    
    while len(numeros) < 6:
        x = int(input("Digite um número sorteado:"))
        
        if x >= 1 and x <= 60 and x not in numeros:
            numeros.append(x)
        else:
            print("Número inválido.")
    
    return numeros

def sublista(l1, l2):
    for x in l1:
        if x not in l2: return False
    
    return True
def vencedoras(apostas, sorteados):
    l = []
    
    for (cpfs, apostados) in apostas:
        if sublista(sorteados, apostados):
            l.append( cpfs )
            
    return l
    
    
def sorteio(jogadores, apostas):
    numeros = lerSorteados()
    premioTotal = float(input("Digite o valor total do prêmio: "))
    
    l = vencedoras(apostas, numeros)
    
    premioPorBilhete = premioTotal / len(l)
    
    i = 1
    print("Vencedores:")
    for aposta in l:
        premioPorPessoa = premioPorBilhete / len(aposta)
        
        print("Aposta", i)
        for c in aposta:
            print(f"{getName(c, jogadores)} - (CPF: {c}) - R${premioPorPessoa:.2f}")
        
        i += 1

jogadores = []
apostas = []

print("Bem vindo ao Bolão!")
menu = '''
Escolha uma opção:

1) Cadastrar usuário
2) Visualizar usuários
3) Cadastrar aposta
4) Visualizar apostas
5) Inserir sorteio e ver vencedores
0) Sair 
'''

op = input(menu)

while op != "0":
    limpaTela()
    if op == "1":
        inserirJogador(jogadores)
    elif op == "2":
        visualizarJogadores(jogadores)
    elif op == "3":
        inserirAposta(jogadores, apostas)
    elif op == "4":
        visualizarApostas(jogadores, apostas)
    elif op == "5":
        sorteio(jogadores, apostas)
    else:
        print("Opção inválida. Tente novamente.")
    
    
    op = input(menu)

print("Tchauzinho <3")