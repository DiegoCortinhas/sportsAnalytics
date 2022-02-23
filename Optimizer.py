from datetime import datetime
from re import L
import sys, heapq
from pprint import pprint
from sys import stdout as out
from operator import indexOf
from time import time
from unittest.mock import Mock
from mip import Model, xsum, maximize, minimize, BINARY, CBC, MAXIMIZE
from mip.constants import OptimizationStatus
import DbConnector
from mockBase import MockBase, MockJ
from fronteiraEficiente import FronteiraEficiente
from SeletorDeSolucoes import SeletorDeSolucoes
import pandas as pd


banco = DbConnector.DbConnector()

def FormatarJogadoresPorRodada(jogadores_por_rodada):
    jogadores_resultado = []
    custo_jogadores_resultado = []
    score_jogadores_resultado = []
    media_jogadores_resultado = []

    for jogador in jogadores_por_rodada:
        jogadores_resultado.append (jogador[1])
        custo_jogadores_resultado.append(float(jogador[2]))
        score_jogadores_resultado.append(float(jogador[3]))
        media_jogadores_resultado.append(float(jogador[4]))

    return jogadores_resultado, custo_jogadores_resultado, score_jogadores_resultado, media_jogadores_resultado

def CalcularTimeMaisBaratoDaRodada(rodada, q_i, q_nome_posicao):
    time_mais_barato = []
    custo_time_mais_barato = 0
    valores_escolhas = []
    
    # Calcula o time mais barato possível na rodada
    #q_i = [1,1,3,2,3,2]
    for i in range(len(q_i)):
        jogadores_posicao = banco.BuscarJogadoresMaisBaratosPorRodadaEPosicao(rodada, q_nome_posicao[i], q_i[i])
        for jogador in jogadores_posicao:
            time_mais_barato.append(jogador)
    
    #print(time_mais_barato, "time_mais_barato")
    for jogador in time_mais_barato:
        custo_time_mais_barato += float(jogador[3])
        valores_escolhas.append(float(jogador[3]))
    
    return time_mais_barato, valores_escolhas, custo_time_mais_barato

def CalculaEpsilons(limite_inferior_epsilon, C, valores_escolhas):
    epsilon = float(limite_inferior_epsilon)
    epsilons = []
    while epsilon < C:
        
        # Chega perto dos casos em que estourem o valor de Cartoletas
        if (epsilon + float(min(valores_escolhas))) > C:
            epsilon = C
        else:
            epsilon += float(min(valores_escolhas))
        epsilons.append(epsilon)
    return epsilons

def CalcularModelo(rodada, J, c, a, q_i, epsilon):
    #q_i = [1,1,1,1,1,1]
    m = Model("Modelo Montagem de Elenco", solver_name=CBC)
    gama = []
    #mock_base = MockBase()
    #Array com ids das possíveis posições dos jogadores
    P = ["ata", "gol", "lat", "mei", "tec", "zag"]

    ataques = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "ata")
    goleiros = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "gol")
    laterais = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "lat")
    meias = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "mei")
    tecnicos = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "tec")
    zagueiros = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "zag")
        
    # IMPORTANTE: NÃO MUDAR ORDEM DOS APPEND NO GAMA
    gama.append(ataques)
    gama.append(goleiros)
    gama.append(laterais)
    gama.append(meias)
    gama.append(tecnicos)
    gama.append(zagueiros)

    #Variavel de dominio y
    y = [[m.add_var(var_type=BINARY, name='y({},{})'.format(i,j)) for j in range(len(J))] for i in range(len(P))]
    
    # Restrição 3.6
    #Nova maneira de escrever restricao 3.6
    for j in range(len(J)):
        nome_restricao = "restricao3.6_" + str(j)
        m.add_constr(xsum(y[i][j] for i in range(len(P))) <= 1.0, name=nome_restricao)
        
    #Nova condição no modelo para não precisarmos usar o inverso de gama e garantirmos a escolha de 1 jogador apenas uma vez
    m.add_constr(xsum(y[i][j] for i in range(len (P)) for j in range(len(J))) == 12, name="restricao_12jogadores")
    
    #Restricao 3.5
    for i in range(len(P)):
        id_jogador_primeira_posicao = gama[i][0][1]
        id_jogador_ultima_posicao = gama[i][-1][1]

        indice_primeiro_jogador_na_posicao_gama_i = indexOf(J, id_jogador_primeira_posicao)
        indice_ultimo_jogador_na_posicao_gama_i = indexOf(J, id_jogador_ultima_posicao)
        
        primeiro_id_jogador = J[indice_primeiro_jogador_na_posicao_gama_i]
        primeiro_jogador = banco.BuscarJogadorPorRodadaEId(rodada, primeiro_id_jogador)
        
        ultimo_id_jogador = J[indice_ultimo_jogador_na_posicao_gama_i]
        ultimo_jogador = banco.BuscarJogadorPorRodadaEId(rodada,ultimo_id_jogador)
        
        
        #print("q_i[" + str(i) + "]: " + str(q_i[i]))
        gama_i = range(indice_primeiro_jogador_na_posicao_gama_i, indice_ultimo_jogador_na_posicao_gama_i + 1)
        nome_restricao = "restricao3.5_" + str(i)
        m.add_constr(xsum(y[i][j] for j in gama_i) == q_i[i], name=nome_restricao)
    
    #Restricao 3.3 (que "vira" a 3.2)
    m.add_constr(xsum(float(c[j]) * y[i][j] for j in range(len(J)) for i in range(len(P))) <= epsilon, name= "restricao3.3_" + str(i))
        
    
    #Função Objetivo 3.1
    somatorio_score = xsum(float(a[j]) * y[i][j] for j in range(len(J)) for i in range(len(P)))
    
    m.objective = maximize(somatorio_score)
    m.verbose = 0
    #m.write('model.lp')
    #m.write('model.mps')
    solucao = m.optimize()

    #for i in range(len(P)):
    #    for j in range(len(J)): 
    #        if y[i][j].x >= 0.99:
    #            print("y[" + str(i) + "][" + str(j) + "].x = " + str(y[i][j].x) + " -> ESCOLHIDO PELO ALGORITMO")
    #        else:
    #            print("y[" + str(i) + "][" + str(j) + "].x = " + str(y[i][j].x))

    """if solucao == OptimizationStatus.OPTIMAL:
        print('optimal solution cost {} found'.format(m.objective_value))
    
    elif solucao == OptimizationStatus.FEASIBLE:
        print('sol.cost {} found, best possible: {}'.format(m.objective_value, m.objective_bound))
    elif solucao == OptimizationStatus.NO_SOLUTION_FOUND:
        print('no feasible solution found, lower bound is: {}'.format(m.objective_bound))"""
        
    jogadores_escolhidos = []
    custo_jogadores_escolhidos = 0

    for i in range(len(P)):
        for j in range(len(J)):
            if y[i][j].x >= 0.99:
                # REVER AQUI (LEMBRAR DO Q_I)
                id_jogador = J[j]
                custo_jogadores_escolhidos += float(c[j])
                jogador_escolhido = banco.BuscarJogadorPorRodadaEId(rodada,id_jogador)
                jogadores_escolhidos.append(jogador_escolhido)
    
    df = pd.DataFrame(jogadores_escolhidos,columns=["Nome","Id","Posicao","Custo","Score","Media"])
    #print(df)

    #print(m.objective_value, " Scores dos times")
    #print(custo_jogadores_escolhidos, "Custo jogadores escolhidos")
    return m.objective_value, jogadores_escolhidos, custo_jogadores_escolhidos
    
def run(perfis = [], q = [], rodadas = []):
    solucoes = []
    #Deixando somente 1 perfil para teste
    perfis = ["prefere_mais_score"]
    # ["ata", "gol", "lat", "mei", "tec", "zag"]
    q_legivel = ["4-4-2"]
    q = [
        # 4-4-2
        [2,1,2,4,1,2]
        # 3-5-2
        #[2,1,0,5,1,3]
        # 4-3-3
        #[3,1,2,3,1,2]
        # 5-3-2
        #[2,1,2,3,1,3]
    ]
    for perfil in perfis:
        C = 100
        #C = 51.36999999999997
        limite_rodadas = 38
        q_nome_posicao = ["ata","gol","lat","mei","tec","zag"]
        i_esquema_tatico = 0
        # q_i é o esquema tático
        for q_i in q:
            # Incrementa o limite_rodadas porque o Python não considera o valor limite no laço de repetição
            for rodada in range(1, limite_rodadas+1):
            #for rodada in [34,35,36,37,38]:
                solucoes_por_rodada = []
                
                print("\n\nCOMEÇOU A RODADA: " + str(rodada))
                print(datetime.now().strftime('%d/%m/%Y %H:%M'), " Hora que começou a rodada")
                print("Perfil: " + perfil + "; Esquema Tático: " + q_legivel[i_esquema_tatico])
                print("Quantidade de Cartoletas disponiveis na rodada: " + str(C))

                time_mais_barato, valores_escolhas, limite_inferior_epsilon = CalcularTimeMaisBaratoDaRodada(rodada, q_i, q_nome_posicao)

                dataframe_time_mais_barato = pd.DataFrame(time_mais_barato, columns=["nome","id","posicao","custo","score","media"])

                print(dataframe_time_mais_barato, " Dataframe time Mais Barato")

                print("LIMITE INFERIOR PARA EPSILON: " + str(limite_inferior_epsilon) + "\n")
                # Aqui vai carregar todos os jogadores disponíveis NAQUELA RODADA
                jogadores_por_rodada = banco.BuscarTodosJogadoresPorRodada(rodada)
                # Formata variáveis para entrada na função que calcula o modelo
                J, c, _, a = FormatarJogadoresPorRodada(jogadores_por_rodada)
                
                #Media na base é calculada somando os scores das rodadas jogadas e dividindo pelo numero de jogadas rodadas
                #a = CalcularMediaScorePorRodadaEAno(2019, rodada, J)
                
                epsilons = CalculaEpsilons(limite_inferior_epsilon, C, valores_escolhas)
                
                custo_jogadores_escolhidos_rodada_atual = 0.0
                jogadores_escolhidos = []
                indice_jogadores_escolhidos = 0
                
                for epsilon in epsilons:
                    solucao_maior_score, jogadores_escolhidos_modelo, custo_solucao = CalcularModelo(rodada, J, c, a, q_i, epsilon)
                    jogadores_escolhidos.append(jogadores_escolhidos_modelo)
                    solucoes.append((solucao_maior_score,custo_solucao,rodada,indice_jogadores_escolhidos))
                    solucoes_por_rodada.append((solucao_maior_score,custo_solucao,rodada,indice_jogadores_escolhidos))
                    indice_jogadores_escolhidos += 1                    #print(epsilon, "epsilon\n")
                
                
                fronteira_eficiente = FronteiraEficiente(solucoes_por_rodada, jogadores_escolhidos)
                solucoes_eficiente, jogadores_escolhidos_solucoes_eficiente = fronteira_eficiente.CalcularFronteiraEficiente()
                print("\n", solucoes_eficiente, "\nsolucoes_eficiente\n")
                #jogadores_escolhidos_solucoes_eficiente = fronteira_eficiente.RetornaJogadoresSolucoesEficiente()
                # Escolhe a solução para cada Perfil de Jogador Virtual
                seletor_solucoes = SeletorDeSolucoes(perfil, jogadores_escolhidos_solucoes_eficiente, solucoes_eficiente, C)
                solucao_escolhida_pelo_perfil, jogadores_solucao_escolhida_pelo_perfil = seletor_solucoes.EscolherSolucao()
                
                print(solucao_escolhida_pelo_perfil, "solucao_escolhida_pelo_perfil")
                print(type(solucao_escolhida_pelo_perfil), "type(solucao_escolhida_pelo_perfil)")
                print(len(solucao_escolhida_pelo_perfil), "len(solucao_escolhida_pelo_perfil)")
                custo_solucao_escolhida_pelo_perfil = float(solucao_escolhida_pelo_perfil.iloc[1])
                score_solucao_escolhida_pelo_perfil = float(solucao_escolhida_pelo_perfil.iloc[0])

                print(seletor_solucoes.FormatarDataframeParaRetorno(jogadores_solucao_escolhida_pelo_perfil), " Solução escolhida")
                print("\nCusto da Solução Escolhida pelo Perfil: " + str(custo_solucao_escolhida_pelo_perfil))
                print("Score da Solução Escolhida pelo Perfil: " + str(score_solucao_escolhida_pelo_perfil))
                print("Time escolhido com C igual a: " + str(C) + "\n")
                
                # ATUALIZA A QUANTIDADE DE CARTOLETAS DISPONIVEL PARA A PRÓXIMA RODADA
                proxima_rodada = rodada + 1
                
                jogadores_escolhidos_na_proxima_rodada = []
                
                custo_jogadores_escolhidos_rodada_atual += float(custo_solucao_escolhida_pelo_perfil)
                
                for i in jogadores_solucao_escolhida_pelo_perfil:
                    
                    #Busca o jogador que foi escolhido na rodada atual na rodada seguinte (para pegar o custo dele na prox rodada)
                    jogador_escolhido_na_prox_rodada = banco.BuscarJogadorPorRodadaEId(proxima_rodada,i[1])
                    
                    #Se o jogador jogar a prox rodada pega o custo dele prox na rodada
                    if jogador_escolhido_na_prox_rodada is not None:
                        jogadores_escolhidos_na_proxima_rodada.append(jogador_escolhido_na_prox_rodada)
                    
                    #Se o jogador não jogar a prox rodada pega o custo dele na rodada arual
                    if jogador_escolhido_na_prox_rodada is None:
                        custo_jogador_rodada_atual = float(i[3])
                        posicao_jogador_rodada_atual = i[2]

                        if rodada < 38:
                            jogador_menor_custo_da_posicao_na_proxima_rodada = banco.BuscarJogadorComMenorCustoProximaRodada(rodada, posicao_jogador_rodada_atual)
                            custo_jogador_menor_custo_da_posicao_na_proxima_rodada = float(jogador_menor_custo_da_posicao_na_proxima_rodada[3])

                            if max(custo_jogador_rodada_atual, custo_jogador_menor_custo_da_posicao_na_proxima_rodada ) == custo_jogador_rodada_atual:
                                jogadores_escolhidos_na_proxima_rodada.append(i)
                            else:
                                jogadores_escolhidos_na_proxima_rodada.append(jogador_menor_custo_da_posicao_na_proxima_rodada)
                        else:
                            jogadores_escolhidos_na_proxima_rodada.append(i)

                
                #print(jogadores_escolhidos_na_proxima_rodada, "jogadores_escolhidos_na_proxima_rodada")

                #Diminui o custo de escalar o time na rodada atual
                C -= custo_jogadores_escolhidos_rodada_atual
                print("Quantidade de cartoletas que sobraram na rodada atual: " + str(C))
                #print(jogadores_escolhidos_na_proxima_rodada)
                print("Jogadores na lista de Escolhidos a somar no valor de C")
                C_proxima_rodada = C
                valor = 0
                #Atualizar time com valores do time na segunda rodada
                for i in jogadores_escolhidos_na_proxima_rodada:
                    #print(i[3])
                    valor += float(i[3])
                    C_proxima_rodada += float(i[3])
                print(valor, " Custo do time escolhido pelo Perfil na PRÓXIMA RODADA")
                print("Quantidade de cartoletas para a proxima rodada: " + str(C_proxima_rodada) )

                # "Vende" o time e Atualiza o C para a próxima rodada
                C = C_proxima_rodada
                print(datetime.now().strftime('%d/%m/%Y %H:%M'), " Hora que terminou a rodada")    
                print("############################################################################################\n\n")

            i_esquema_tatico += 1
            print("############################################################################################\n\n")
            

run()

