def adultos_1():
    pessoas = {}
    for i in range(10):
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        telefone = input("Digite o telefone: ")
        pessoas[nome] = {'idade': idade, 'telefone': telefone}

    chaves_para_remover = []
    for nome in pessoas:
        if pessoas[nome]['idade'] < 18:
            chaves_para_remover.append(nome)

    for nome in chaves_para_remover:
        del pessoas[nome]

    print("\nAdultos na lista:")
    for nome in pessoas:
        print("Nome:", nome, "Telefone:", pessoas[nome]['telefone'])

import os

def limpaTela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def cadastrar_telefone(agenda):
    nome = input("Nome: ")
    telefone = input("Telefone: ")

    agenda[nome] = telefone

def visualizar_agenda(agenda):
    for contato in agenda:
        print(f'{contato}:\t{agenda[contato]}')

def agendas_2():
    menu = '''
[1] Cadastrar telefone
[2] Visualizar agenda
    '''

    agenda = {}

    op = int(input(menu))
    limpaTela()

    while op in [1, 2]:

        if op == 1:
            cadastrar_telefone(agenda)
        elif op == 2:
            visualizar_agenda(agenda)

        op = int(input(menu))
        limpaTela()    
    print("Obrigado por usar o meu programa!")

def existeCPF(cpf, jogadores):
    if cpf in jogadores:
        return True
    return False

def inserirJogador(jogadores):
    nome = input("Nome: ")
    cpf = input("CPF: ")
    
    if existeCPF(cpf, jogadores):
        print("Jogador repetido. Cadastro nao realizado.")
    else:
        jogadores[cpf] = nome
        print("Jogador cadastrado com sucesso.")
    
def visualizarJogadores(jogadores):
    if not jogadores:
        print("Nenhum jogador cadastrado ainda.")
    else:
        print("Jogadores:")
        for cpf in jogadores:
            nome = jogadores[cpf]
            print(nome, "- (CPF:", cpf, ")")

def inserirCPFs(jogadores):
    n = int(input("Quantos jogadores? "))
    cpfs = []
    
    while n < 1 or n > len(jogadores):
        n = int(input("Numero invalido. Tente novamente: "))
    
    while len(cpfs) != n:
        visualizarJogadores(jogadores)
        cpf = input("Digite um cpf: ")
        
        if existeCPF(cpf, jogadores) and cpf not in cpfs:
            cpfs.append(cpf)
        else:
            print("CPF invalido.")
    
    return cpfs
    
def inserirNumeros():
    numeros = []
    
    n = int(input("Quantos numeros nessa aposta? "))
    
    while n < 6 or n > 15:
        n = int(input("Numero invalido. Tente novamente: "))
        
    while len(numeros) < n:
        x = int(input("Digite um numero apostado neste cartao: "))
        
        if x >= 1 and x <= 60 and x not in numeros:
            numeros.append(x)
        else:
            print("Numero invalido.")
            
    return numeros

def inserirAposta(jogadores, apostas):
    cpfs = inserirCPFs(jogadores)
    numeros = inserirNumeros()
    
    apostas.append( (cpfs, numeros) )
 
def getName(cpf, jogadores):
    if cpf in jogadores:
        return jogadores[cpf]
    return None
    
def visualizarApostas(jogadores, apostas):
    if not apostas:
        print("Nenhuma aposta cadastrada.")
    else:
        i = 1
        for (cpfs, numeros) in apostas:
            print("Aposta", i)
            
            print("Numeros:", end=" ")
            
            for num in numeros: 
                print(num, end=" ")
            
            print("\n")
            
            print("Jogadores:")
            for cpf in cpfs:
                print(getName(cpf, jogadores), "- (cpf:", cpf, ")")
            
            i = i + 1

def lerSorteados():
    numeros = []
    
    while len(numeros) < 6:
        x = int(input("Digite um numero sorteado:"))
        
        if x >= 1 and x <= 60 and x not in numeros:
            numeros.append(x)
        else:
            print("Numero invalido.")
    
    return numeros

def sublista(l1, l2):
    for x in l1:
        if x not in l2: 
            return False
    return True

def vencedoras(apostas, sorteados):
    l = []
    
    for (cpfs, apostados) in apostas:
        if sublista(sorteados, apostados):
            l.append(cpfs)
            
    return l
    
def sorteio(jogadores, apostas):
    numeros = lerSorteados()
    premioTotal = float(input("Digite o valor total do premio: "))
    
    l = vencedoras(apostas, numeros)

    if len(l) > 0:
        premioPorBilhete = premioTotal / len(l)
        
        i = 1
        print("Vencedores:")
        for aposta in l:
            premioPorPessoa = premioPorBilhete / len(aposta)
            
            print("Aposta", i)
            for c in aposta:
                print(getName(c, jogadores), "- (CPF:", c, ") - R$", premioPorPessoa)
            
            i = i + 1
    else:
        print("Nenhuma aposta vencedora.")

def bolao_3():
    jogadores = {}
    apostas = []

    print("Bem vindo ao Bolao!")
    menu = '''
Escolha uma opcao:

1) Cadastrar usuario
2) Visualizar usuarios
3) Cadastrar aposta
4) Visualizar apostas
5) Inserir sorteio e ver vencedores
0) Sair 
'''
    
    op = input(menu)

    while op != "0":
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
            print("Opcao invalida. Tente novamente.")
        
        op = input(menu)

    print("Tchauzinho")

def fase_1(candidatos, areas, area):
    passaram = []
    inscritos = areas[area][1]
    for cod_candidato in inscritos:
        if candidatos[cod_candidato][2] >= 60:
            passaram.append(cod_candidato)
    return passaram

def concurso_4_a(candidatos, areas, area):
    aprovados = fase_1(candidatos, areas, area)

    for cod_candidato in aprovados:
        print(cod_candidato, candidatos[cod_candidato][1])

def selecionar_aprovado(candidatos, areas, area):
    maior_nota = 0
    aprovados = []
    aprovados_1_fase = fase_1(candidatos, areas, area)
    for aprovado in aprovados_1_fase:
        _,_,nota1, nota2 = candidatos[aprovado]
        soma = nota1 + nota2
        if soma > maior_nota:
            maior_nota = soma
    
    for aprovado in aprovados_1_fase:
        _,_,nota1, nota2 = candidatos[aprovado]
        soma = nota1 + nota2

        if soma == maior_nota:
            aprovados.append(aprovado)
    
    if len(aprovados) == 1:
        return aprovados[0]

    if len(aprovados) > 1:
        return aprovado_mais_velho(aprovados, candidatos)

def aprovado_mais_velho(aprovados, candidatos):
    id_mais_velho = aprovados[0]
    _, data_velho, _, _ = candidatos[id_mais_velho]

    i = 1
    while i < len(aprovados):
        id_atual = aprovados[i]
        _, data_atual, _, _ = candidatos[id_atual]

        ano_velho = data_velho[2]
        mes_velho = data_velho[1]
        dia_velho = data_velho[0]

        ano_atual = data_atual[2]
        mes_atual = data_atual[1]
        dia_atual = data_atual[0]

        if ano_atual < ano_velho:
            id_mais_velho = id_atual
            data_velho = data_atual
        elif ano_atual == ano_velho:
            if mes_atual < mes_velho:
                id_mais_velho = id_atual
                data_velho = data_atual
            elif mes_atual == mes_velho:
                if dia_atual < dia_velho:
                    id_mais_velho = id_atual
                    data_velho = data_atual
        i += 1
    return id_mais_velho
            

def concurso_4_b(candidatos, areas):
    for area in areas:
        cod_aprovado = selecionar_aprovado(candidatos, areas, area)
        nome_area = areas[area][0]
        if cod_aprovado:
            nome_aprovado = candidatos[cod_aprovado][0]
            print(nome_area, ":", nome_aprovado)
        else:
            print(nome_area, ": Sem aprovados.")
