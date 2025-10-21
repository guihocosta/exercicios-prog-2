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

def eh_data_anterior(data1, data2):
    dia1, mes1, ano1 = data1
    dia2, mes2, ano2 = data2
    if ano1 < ano2:
        return True
    if ano1 == ano2 and mes1 < mes2:
        return True
    if ano1 == ano2 and mes1 == mes2 and dia1 < dia2:
        return True
    return False

def filtrar_infracoes_recentes_5a(infracoes, data_atual):
    infracoes_recentes = []
    dia_atual, mes_atual, ano_atual = data_atual
    data_limite = (dia_atual, mes_atual, ano_atual - 1)
    
    for infracao in infracoes:
        data_infracao = infracao[1]
        
        if not eh_data_anterior(data_infracao, data_limite):
            infracoes_recentes.append(infracao)
            
    return infracoes_recentes

def calcular_pontos_cnh_5b(cnh, infracoes_recentes, veiculos, naturezas):
    pontos = 0
    placas_do_motorista = []
    for placa in veiculos:
        cnh_proprietario, _, _ = veiculos[placa]
        if cnh_proprietario == cnh:
            placas_do_motorista.append(placa)
            
    for infracao in infracoes_recentes:
        _, _, placa_multada, tipo_natureza = infracao
        if placa_multada in placas_do_motorista:
            if tipo_natureza in naturezas:
                pontos = pontos + naturezas[tipo_natureza]
                
    return pontos

def checar_blitz_5c(cnh_motorista, placa_veiculo, data_atual, motoristas, veiculos, infracoes, naturezas):
    print("\n--- Verificacao Blitz ---")
    print("Motorista:", cnh_motorista, "| Placa:", placa_veiculo)

    if placa_veiculo not in veiculos:
        print("ALERTA: Placa nao cadastrada.")
        return

    vencimento_motorista = motoristas[cnh_motorista][1]
    if eh_data_anterior(vencimento_motorista, data_atual):
        print("ALERTA: CNH do motorista vencida.")
        return
        
    infracoes_recentes = filtrar_infracoes_recentes_5a(infracoes, data_atual)
    pontos_motorista = calcular_pontos_cnh_5b(cnh_motorista, infracoes_recentes, veiculos, naturezas)
    
    if pontos_motorista >= 20:
        print("ALERTA: CNH do motorista com 20 pontos ou mais.")
        return

    print("Situacao: Regular")
    cnh_proprietario, modelo, cor = veiculos[placa_veiculo]
    nome_proprietario, _ = motoristas[cnh_proprietario]
    pontos_proprietario = calcular_pontos_cnh_5b(cnh_proprietario, infracoes_recentes, veiculos, naturezas)
    nome_motorista, _ = motoristas[cnh_motorista]

    print("Modelo:", modelo, "| Cor:", cor)
    print("Proprietario:", nome_proprietario, "| Pontos:", pontos_proprietario)
    print("Motorista:", nome_motorista, "| Pontos:", pontos_motorista)

def exibir_treino_grupo(exercicios, alunos, treinos, login, grupo):
    nome_aluno = alunos[login][0]
    print("\n------------------------------")
    print("Aluno:", nome_aluno)
    print("Grupo:", grupo)
    print("------------------------------")
    
    atividades_aluno = treinos[login]
    for atividade in atividades_aluno:
        cod_exercicio, series, repeticoes, grupo_treino = atividade
        if grupo_treino == grupo:
            nome_exercicio = exercicios[cod_exercicio]
            print(nome_exercicio)
            print(series, "de", repeticoes)

def listar_exercicios_nao_feitos(exercicios, treinos, login):
    print("\n------------------------------")
    print("Verificando exercicios nao feitos por", login)
    print("------------------------------")

    exercicios_feitos_cod = []
    if login in treinos:
        atividades_aluno = treinos[login]
        for atividade in atividades_aluno:
            cod_exercicio, _, _, _ = atividade
            if cod_exercicio not in exercicios_feitos_cod:
                exercicios_feitos_cod.append(cod_exercicio)

    for cod_exercicio in exercicios:
        if cod_exercicio not in exercicios_feitos_cod:
            print(exercicios[cod_exercicio])

def autenticar_aluno_6(exercicios, alunos, treinos):
    print("\n--- Sistema de Autenticacao 'Hoje Ta Pago' ---")
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if login not in alunos:
        print("Erro: login nao existente.")
        return

    senha_correta = alunos[login][1]
    if senha != senha_correta:
        print("Erro: senha incorreta.")
        return

    grupo_desejado = input("Login efetuado. Digite o grupo que deseja treinar hoje: ")
    
    grupo_existe = False
    if login in treinos:
        atividades_aluno = treinos[login]
        for atividade in atividades_aluno:
            _, _, _, grupo_treino = atividade
            if grupo_treino == grupo_desejado:
                grupo_existe = True

    if not grupo_existe:
        print("Erro: grupo inexistente para o aluno.")
        return
        
    exibir_treino_grupo(exercicios, alunos, treinos, login, grupo_desejado)

def verificar_estoque_7a(cod_produto, produtos, pedidos):
    if cod_produto not in produtos:
        print("Produto nao encontrado.")
        return

    _, _, estoque_atual = produtos[cod_produto]
    demanda_pedidos_abertos = 0

    for cod_pedido in pedidos:
        _, status, lista_itens = pedidos[cod_pedido]
        if not status:
            for item in lista_itens:
                cod_item, quantidade = item
                if cod_item == cod_produto:
                    demanda_pedidos_abertos = demanda_pedidos_abertos + quantidade

    print("\n--- Verificacao de Estoque para o produto:", cod_produto, "---")
    print("Estoque atual:", estoque_atual)
    print("Demanda em pedidos abertos:", demanda_pedidos_abertos)

    if estoque_atual >= demanda_pedidos_abertos:
        print("Resultado: Estoque SUFICIENTE.")
    else:
        print("Resultado: Estoque INSUFICIENTE.")

def imprimir_pedido_7b(cod_pedido, produtos, pedidos):
    if cod_pedido not in pedidos:
        print("Pedido nao encontrado.")
        return

    _, status, lista_itens = pedidos[cod_pedido]
    
    print("\n--- Detalhes do Pedido #", cod_pedido, "---")
    for item in lista_itens:
        cod_produto, quantidade = item
        valor_unit, nome_produto, _ = produtos[cod_produto]
        valor_total_item = valor_unit * quantidade
        
        print(nome_produto)
        print("Qtd:", quantidade)
        print("Valor unitario: R$", valor_unit)
        print("Valor total: R$", valor_total_item)
        print("---")
    
    if status:
        print("Status: Entregue")
    else:
        print("Status: Em aberto")

def calcular_total_pedido_7c(cod_pedido, produtos, pedidos):
    if cod_pedido not in pedidos:
        return 0

    valor_total = 0
    _, _, lista_itens = pedidos[cod_pedido]
    for item in lista_itens:
        cod_produto, quantidade = item
        valor_unit, _, _ = produtos[cod_produto]
        valor_total = valor_total + (valor_unit * quantidade)
    return valor_total

def imprimir_totais_clientes_7d(clientes, produtos, pedidos):
    gastos_por_cliente = {}
    for cpf in clientes:
        gastos_por_cliente[cpf] = 0

    for cod_pedido in pedidos:
        cpf_cliente, status, _ = pedidos[cod_pedido]
        if status:
            total_pedido = calcular_total_pedido_7c(cod_pedido, produtos, pedidos)
            if cpf_cliente in gastos_por_cliente:
                gastos_por_cliente[cpf_cliente] = gastos_por_cliente[cpf_cliente] + total_pedido
    
    print("\n--- Total Pago por Cliente ---")
    for cpf in gastos_por_cliente:
        nome_cliente, _ = clientes[cpf]
        total_gasto = gastos_por_cliente[cpf]
        print(nome_cliente, "- R$", total_gasto)

def tempo_voo_8a(num_voo, voos):
    _, _, escalas = voos[num_voo]
    
    _, hora_partida = escalas[0]
    _, hora_chegada = escalas[len(escalas) - 1]
    
    h_partida, m_partida = hora_partida
    h_chegada, m_chegada = hora_chegada
    
    minutos_partida = h_partida * 60 + m_partida
    minutos_chegada = h_chegada * 60 + m_chegada
    
    duracao = 0
    if minutos_chegada < minutos_partida:
        duracao = (minutos_chegada + 24 * 60) - minutos_partida
    else:
        duracao = minutos_chegada - minutos_partida
        
    return duracao

def listar_origem_destino_8b(voos):
    print("\n--- Origem e Destino dos Voos ---")
    for num_voo in voos:
        _, _, escalas = voos[num_voo]
        cidade_origem, _ = escalas[0]
        cidade_destino, _ = escalas[len(escalas) - 1]
        print("Voo:", num_voo, "- Origem:", cidade_origem, "- Destino:", cidade_destino)

def voos_por_cidade_8c(origem, intermediaria, voos):
    print("\n--- Voos de", origem, "passando por", intermediaria, "---")
    voo_encontrado = False
    for num_voo in voos:
        _, _, escalas = voos[num_voo]
        cidade_origem, _ = escalas[0]
        
        if cidade_origem == origem:
            passa_pela_cidade = False
            i = 1
            while i < len(escalas):
                cidade_escala, _ = escalas[i]
                if cidade_escala == intermediaria:
                    passa_pela_cidade = True
                i = i + 1
            
            if passa_pela_cidade:
                print("Voo:", num_voo)
                voo_encontrado = True
    
    if not voo_encontrado:
        print("Nenhum voo encontrado para esta rota.")

def voo_mais_rapido_8d(origem, destino, voos):
    print("\n--- Voo mais rapido de", origem, "para", destino, "---")
    melhor_voo_id = -1
    menor_tempo = -1

    for num_voo in voos:
        _, _, escalas = voos[num_voo]
        cidade_origem, _ = escalas[0]
        cidade_destino, _ = escalas[len(escalas) - 1]
        
        if cidade_origem == origem and cidade_destino == destino:
            tempo_atual = tempo_voo_8a(num_voo, voos)
            if menor_tempo == -1 or tempo_atual < menor_tempo:
                menor_tempo = tempo_atual
                melhor_voo_id = num_voo

    if melhor_voo_id != -1:
        companhia, _, _ = voos[melhor_voo_id]
        print("Companhia:", companhia, "- Voo:", melhor_voo_id)
        print("Tempo total:", menor_tempo, "minutos")
    else:
        print("Nenhum voo direto encontrado.")

def exibir_series(series):
    print("\n--- STATUS DAS SERIES ---")
    if not series:
        print("Nenhuma serie cadastrada.")
        return
    
    for nome in series:
        print("*", nome, "*")
        temporadas = series[nome]
        if not temporadas:
            print("Nenhuma temporada cadastrada")
        else:
            num_temporada = 1
            for temporada in temporadas:
                linha = "Temporada " + str(num_temporada) + ": "
                num_episodio = 1
                for episodio_visto in temporada:
                    id_ep = "T" + str(num_temporada) + "E" + str(num_episodio)
                    if episodio_visto:
                        linha = linha + "+" + id_ep + " "
                    else:
                        linha = linha + "-" + id_ep + " "
                    num_episodio = num_episodio + 1
                print(linha)
                num_temporada = num_temporada + 1
    print("-------------------------")

def selecionar_serie_valida(series, mensagem):
    print("\nSeries disponiveis:")
    if not series:
        print("Nenhuma.")
        return None
    for nome in series:
        print("-", nome)
    nome_escolhido = input(mensagem)
    if nome_escolhido in series:
        return nome_escolhido
    else:
        print("Erro: Serie nao encontrada.")
        return None

def cadastrar_serie_a(series):
    nome = input("Digite o nome da serie a ser cadastrada: ")
    if nome in series:
        print("Erro: Serie ja cadastrada.")
    else:
        series[nome] = []
        print("Serie", nome, "cadastrada com sucesso.")

def excluir_serie_b(series):
    nome = selecionar_serie_valida(series, "Digite o nome da serie a ser excluida: ")
    if nome:
        del series[nome]
        print("Serie", nome, "excluida com sucesso.")

def cadastrar_temporada_c(series):
    nome = selecionar_serie_valida(series, "Digite o nome da serie para adicionar temporada: ")
    if nome:
        num_existentes = len(series[nome])
        print("Cadastrando a temporada", num_existentes + 1, "para", nome)
        num_eps = int(input("Digite o numero de episodios: "))
        nova_temporada = []
        i = 0
        while i < num_eps:
            nova_temporada.append(False)
            i = i + 1
        series[nome].append(nova_temporada)
        print("Temporada cadastrada.")

def marcar_episodio_visto_e(series):
    nome = selecionar_serie_valida(series, "Digite o nome da serie: ")
    if nome:
        temp = int(input("Digite o numero da temporada: "))
        ep = int(input("Digite o numero do episodio: "))
        if temp > 0 and temp <= len(series[nome]):
            if ep > 0 and ep <= len(series[nome][temp-1]):
                series[nome][temp-1][ep-1] = True
                print("Episodio marcado como visto.")
            else:
                print("Erro: Episodio invalido.")
        else:
            print("Erro: Temporada invalida.")

def marcar_temporada_vista_f(series):
    nome = selecionar_serie_valida(series, "Digite o nome da serie: ")
    if nome:
        temp = int(input("Digite o numero da temporada: "))
        if temp > 0 and temp <= len(series[nome]):
            temporada = series[nome][temp-1]
            i = 0
            while i < len(temporada):
                temporada[i] = True
                i = i + 1
            print("Temporada marcada como vista.")
        else:
            print("Erro: Temporada invalida.")

def marcar_serie_vista_g(series):
    nome = selecionar_serie_valida(series, "Digite o nome da serie: ")
    if nome:
        for temporada in series[nome]:
            i = 0
            while i < len(temporada):
                temporada[i] = True
                i = i + 1
        print("Serie marcada como vista.")

def calcular_e_exibir_estatisticas_h(series):
    total_eps_cadastrados = 0
    total_eps_assistidos = 0
    series_em_dia = []
    series_atrasadas = {}

    for nome in series:
        atrasada = False
        eps_atrasados_lista = []
        num_temp = 1
        for temporada in series[nome]:
            num_ep = 1
            for visto in temporada:
                total_eps_cadastrados = total_eps_cadastrados + 1
                if visto:
                    total_eps_assistidos = total_eps_assistidos + 1
                else:
                    atrasada = True
                    eps_atrasados_lista.append("T" + str(num_temp) + "E" + str(num_ep))
                num_ep = num_ep + 1
            num_temp = num_temp + 1
        if atrasada:
            series_atrasadas[nome] = eps_atrasados_lista
        else:
            if series[nome]:
                series_em_dia.append(nome)
    
    print("\n--- ESTATISTICAS ---")
    print("Quantidade de series cadastradas:", len(series))
    print("\nSeries em dia:", series_em_dia)
    print("\nEpisodios atrasados:")
    for nome in series_atrasadas:
        linha = "* " + nome + ": "
        for ep_id in series_atrasadas[nome]:
            linha = linha + ep_id + " "
        print(linha)
    print("\nTotal de episodios cadastrados:", total_eps_cadastrados)
    print("Total de episodios assistidos:", total_eps_assistidos)
    print("--------------------")