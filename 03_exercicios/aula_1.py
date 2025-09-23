def entrada_dados(x):
    l = []
    for i in range(x):
        dict = {}
        dict["Nome"] = input()
        dict["Idade"] = int(input())
        dict["Telefone"] = input()
        l.append(dict)
    return l


def adultos_1():
    lista = entrada_dados(10)
    
    i = 0
    while i < len(lista):
        if lista[i]["Idade"] < 18:
            lista.remove(lista[i])
            i -= 1
        i += 1

    for dados in lista:
        print(f'{dados["Nome"]} : {dados["Telefone"]}')

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

def bolao_3():
    


