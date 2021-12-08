from mip import Model, xsum, maximize, minimize, BINARY, CBC

qtd_goleiros = 1
qtd_defensores = 4
qtd_meiocampos = 4
qtd_atacantes = 2
dinheiro_total_disponivel = 300

def BuscarJogadoresPorSecao(nome_posicao, qtd_maxima_jogadores_na_secao):
    #TODO: Função que vai retornar os jogadores e os seus respectivos custos
    jogadores_resultado = [1,2,3]
    custos_jogadores_resultado = [10,20,30]
    score_jogadores_resultado = [10,10,10]
    return jogadores_resultado, custos_jogadores_resultado, score_jogadores_resultado

def CalcularModelo(dinheiro_total_disponivel,qtd_goleiros, qtd_defensores, qtd_meiocampos, qtd_atacantes):
    # dinheiro_total_disponivel = Custo Total "C"

    escalacao_jogadores_rodada = []
    # Esquema Tatico 4-4-2
    qtd_por_secoes_campo = [qtd_goleiros, qtd_defensores, qtd_meiocampos, qtd_atacantes]
    #Dados na base estão como gol, zag, mei, ata
    nome_posicoes = ["gol","zag", "mei", "ata"]
    lista_rodadas = [1 .... 38]

    for rodada in lista_rodadas:
        indice_nome_posicoes = 0
        for qtd_por_secao_campo in qtd_por_secoes_campo:
            # posicoes_jogadores_por_secao = qi do problema
            posicoes_jogadores_por_secao = []
            # custo_jogadores_por_secao = cj do problema
            custo_jogadores_por_secao = []
            # score_jogadores_por_secao = aj do problema
            score_jogadores_por_secao = []

            # Como resultado da busca terei os jogadores com seus respectivos IDS, custos e scores
            jogadores_por_secao, custo_jogadores_por_secao, score_jogadores_por_secao = \
                BuscarJogadoresPorSecao(nome_posicoes[indice_nome_posicoes], qtd_por_secao_campo)

            # Preenche os jogadores nas posições
            for jogador in jogadores_por_secao:
                posicoes_jogadores_por_secao.append(jogador)

            m = Model("Modelo Montagem de Elenco", solver_name=CBC)

            # Definindo variavel dominio do Problema - 3.6
            yij = [m.add_var(var_type=BINARY) for i,j in posicoes_jogadores_por_secao]

            # Definindo restrição - 3.5
            m += xsum(yij[i] for i in posicoes_jogadores_por_secao) <= 1

            # Definindo restrição - 3.4
            m += xsum(yij[i] for i in posicoes_jogadores_por_secao) == qtd_por_secao_campo
            
            # Definindo restrição - 3.3
            somatorio_custos = (jogadores_por_secao[j] for j in custo_jogadores_por_secao)
            somatorio_custos_por_jogadores_na_posicao = xsum(somatorio_custos[i] * yij[i] for i in posicoes_jogadores_por_secao)
            # m += xsum(jogadores_por_secao[j] for j in custo_jogadores_por_secao) <= dinheiro_total_disponivel
            m += somatorio_custos_por_jogadores_na_posicao <= dinheiro_total_disponivel


            #Definindo a Função Objetivo 3.2
            m += minimize(somatorio_custos_por_jogadores_na_posicao)
            
            #Definindo a Função Objetivo 3.1
            somatorio_scores = (score_jogadores_por_secao[j] for j in score_jogadores_por_secao)
            somatorio_scores_por_jogadores_na_posicao = xsum(somatorio_scores * yij[i] for i in posicoes_jogadores_por_secao)
            m += maximize(somatorio_scores_por_jogadores_na_posicao)

            m.optimize()

            #selected = [i for i in I if x[i].x >= 0.99]
            #print("selected items: {}".format(selected))
            
            indice_nome_posicoes += 1
        escalacao_jogadores_rodada.append(posicoes_jogadores_por_secao)
    
    return escalacao_jogadores_rodada

CalcularModelo(dinheiro_total_disponivel, qtd_defensores, qtd_meiocampos, qtd_atacantes)