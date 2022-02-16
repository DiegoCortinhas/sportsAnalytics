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
from plotaFronteira import PlotaFronteira
import pandas as pd


banco = DbConnector.DbConnector()

def FormatarJogadoresPorRodada(jogadores_por_rodada):
    jogadores_resultado = []
    custo_jogadores_resultado = []
    score_jogadores_resultado = []
    media_jogadores_resultado = []

    for jogador in jogadores_por_rodada:
        jogadores_resultado.append(jogador[1])
        custo_jogadores_resultado.append(jogador[2])
        score_jogadores_resultado.append(jogador[3])
        media_jogadores_resultado.append(jogador[4])

    return jogadores_resultado, custo_jogadores_resultado, score_jogadores_resultado, media_jogadores_resultado

def CalcularMediaScorePorRodadaEAno(ano_base_calculo, rodada, J):
    ano_anterior = ano_base_calculo - 1
    qtd_rodadas = len(range(0, rodada))
    medias = []
    for i in range(len(J)):
        # Lembrar que medias_rodadas_anteriores[i] e medias_ano_anterior[i] retornam uma tupla (id_jogador, valor_media)
        media_rodadas_anteriores = banco.CalcularMediaScorePorRodadaEAno(rodada, ano_base_calculo, J[i])
        media_ano_anterior = banco.CalcularMediaScorePorRodadaEAno(None, ano_anterior, J[i])[0][0]
        media_rodada = 0
        #media_rodadas_anteriores vem como lista de tuplas Exemplo: [('-1.6',)]
        for j in media_rodadas_anteriores:
            media_rodada += float(j[0])
        
        media = (media_rodada + float(media_ano_anterior)) / (qtd_rodadas + 1)
        medias.append(media)

    return medias

def CalcularTimeMaisBaratoDaRodada(rodada, q_i, q_nome_posicao):
    time_mais_barato = []
    time_mais_caro = []
    contador = 0
    
    # Calcula o time mais barato possível na rodada
    #q_i = [1,1,3,2,3,2]
    for i in range(len(q_i)):
        
        jogadores_posicao, valores_escolhas, _, medias_escolhas = FormatarJogadoresPorRodada(banco.BuscarJogadoresPorRodadaEPosicao(rodada, q_nome_posicao[i]))
        
        escolhas_mais_barato = heapq.nsmallest(q_i[i], valores_escolhas)
        escolhas_mais_caro = heapq.nlargest(q_i[i], valores_escolhas)
        
        jogadores_ja_escolhidos_mais_caros = []
        #Escolha dos jogadores mais caros
        for escolha in escolhas_mais_caro:
            #print("Novo jogador mais caro encontrado na posicao: " + q_nome_posicao[i])
            indice_escolha_mais_caro=indexOf(valores_escolhas, escolha)
            jogador_escolhido = jogadores_posicao[indice_escolha_mais_caro]
            if jogador_escolhido not in jogadores_ja_escolhidos_mais_caros:
                jogadores_ja_escolhidos_mais_caros.append(jogador_escolhido)
                time_mais_caro.append(jogador_escolhido)
        

        jogadores_ja_escolhidos = []
        contador+=1
        #limite_inferior_epsilon = 0
        for escolha in escolhas_mais_barato:
            indice_escolha_mais_barato=indexOf(valores_escolhas, escolha)
            jogador_escolhido = jogadores_posicao[indice_escolha_mais_barato]
            # Impede o jogador de ser escolhido duaas vezes em posições diferentes. (Exemplo do William Arão)
            if jogador_escolhido not in jogadores_ja_escolhidos:
                jogadores_ja_escolhidos.append(jogador_escolhido)
                time_mais_barato.append(jogador_escolhido)
        
    return time_mais_barato, valores_escolhas

def CalculaEpsilons(limite_inferior_epsilon, C, valores_escolhas):
    epsilon = float(limite_inferior_epsilon)
    print(epsilon, " epsilon")
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
    m.write('model.lp')
    m.write('model.mps')
    solucao = m.optimize()

    for i in range(len(P)):
        for j in range(len(J)): 
            if y[i][j].x >= 0.99:
                print("y[" + str(i) + "][" + str(j) + "].x = " + str(y[i][j].x) + " -> ESCOLHIDO PELO ALGORITMO")
            else:
                print("y[" + str(i) + "][" + str(j) + "].x = " + str(y[i][j].x))

    if solucao == OptimizationStatus.OPTIMAL:
        print('optimal solution cost {} found'.format(m.objective_value))
    
    elif solucao == OptimizationStatus.FEASIBLE:
        print('sol.cost {} found, best possible: {}'.format(m.objective_value, m.objective_bound))
    elif solucao == OptimizationStatus.NO_SOLUTION_FOUND:
        print('no feasible solution found, lower bound is: {}'.format(m.objective_bound))
        
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
    print(df)

    print(m.objective_value, " Scores dos times")
    print(custo_jogadores_escolhidos, "Custo jogadores escolhidos")
    return m.objective_value, jogadores_escolhidos, custo_jogadores_escolhidos
    
def run(perfis = [], q = [], rodadas = []):
    C = 100
    solucoes = []
    
    #Deixando somente 1 perfil para teste
    perfis = [1]
    limite_rodadas = 38
    q_nome_posicao = ["ata","gol","lat","mei","tec","zag"]
    q = [
        # 4-4-2
        #[2,1,2,4,1,2],
        # 3-5-2
    #P = ["ata", "gol", "lat", "mei", "tec", "zag"]
        #[2,1,2,4,1,2]
        [2,1,2,3,1,3]
    ]
    for perfil in perfis:
        # q_i é o esquema tático
        for q_i in q:
            print("COMEÇOU O ESQUEMA TÁTICO: \n" + str(q_i))
            # Incrementa o limite_rodadas porque o Python não considera o valor limite no laço de repetição
            for rodada in range(1, limite_rodadas+1):
            #for rodada in [34,35,36]:
                print("COMEÇOU A RODADA: \n" + str(rodada))
                print("Quantidade de Cartoletas disponiveis na rodada: " + str(C))

                time_mais_barato, valores_escolhas = CalcularTimeMaisBaratoDaRodada(rodada, q_i, q_nome_posicao)
                limite_inferior_epsilon = 0
                print("\n\nTIME MAIS BARATO CALCULADO PARA EPSILON")
                for jogador_id in time_mais_barato:
                    jogador = banco.BuscarJogadorPorRodadaEId(rodada,jogador_id)
                    
                    #  Soma os custos para o cálculo do Limite inferior de Epsilon
                    limite_inferior_epsilon += float(jogador[3])
                    nome_jogador = str(jogador[0])
                    posicao_jogador = str(jogador[2])
                    custo_jogador = str(jogador[3])
                    score_jogador = str(jogador[4])

                    print("Jogador: " + nome_jogador + "(" + posicao_jogador + ") -> Media: " + score_jogador + "; Custo: " + custo_jogador )

                print("LIMITE INFERIOR CALCULADO PARA O EPSILON: " + str(limite_inferior_epsilon))

                # Aqui vai carregar todos os jogadores disponíveis NAQUELA RODADA
                jogadores_por_rodada = banco.BuscarTodosJogadoresPorRodada(rodada)
                # Formata variáveis para entrada na função que calcula o modelo
                J, c, _, a = FormatarJogadoresPorRodada(jogadores_por_rodada)
                
                #Media na base é calculada somando os scores das rodadas jogadas e dividindo pelo numero de jogadas rodadas
                #a = CalcularMediaScorePorRodadaEAno(2019, rodada, J)
                
                epsilons = CalculaEpsilons(limite_inferior_epsilon, C, valores_escolhas)
                
                custo_jogadores_escolhidos_rodada_atual = 0.0
                
                if len(epsilons) == 0:
                    continue

                for epsilon in epsilons:
                    solucao_maior_score, jogadores_escolhidos, custo_solucao = CalcularModelo(rodada, J, c, a, q_i, epsilon)
                    solucoes.append((solucao_maior_score,custo_solucao,rodada))
                    
                    print(epsilon, "epsilon\n")
                
                print("Time escolhido com C igual a: " + str(C))
                solucao_eficiente = FronteiraEficiente(solucoes)
                print(solucoes, " Soluções")
                print(solucao_eficiente, " Soluções Eficientes")
                #PlotaFronteira(solucoes)
                
                # ATUALIZA A QUANTIDADE DE CARTOLETAS DISPONIVEL PARA A PRÓXIMA RODADA
                proxima_rodada = rodada + 1
                jogadores_escolhidos_na_proxima_rodada = []
                print(custo_solucao, " Custo do time na rodada")
                #sys.exit()
                custo_jogadores_escolhidos_rodada_atual += float(custo_solucao)
                
                for i in jogadores_escolhidos:
                    
                    #Busca o jogador que foi escolhido na rodada atual na rodada seguinte (para pegar o custo dele na prox rodada)
                    jogador_escolhido_na_prox_rodada = banco.BuscarJogadorPorRodadaEId(proxima_rodada,i[1])
                    
                    #Se o jogador jogar a prox rodada pega o custo dele prox na rodada
                    if jogador_escolhido_na_prox_rodada is not None:
                        jogadores_escolhidos_na_proxima_rodada.append(jogador_escolhido_na_prox_rodada)
                    
                    #Se o jogador não jogar a prox rodada pega o custo dele na rodada arual
                    if jogador_escolhido_na_prox_rodada is None:
                        jogadores_escolhidos_na_proxima_rodada.append(i)
                    
                #Diminui o custo de escalar o time na rodada atual
                C -= custo_jogadores_escolhidos_rodada_atual
                print("Quantidade de cartoletas que sobraram na rodada atual: " + str(C))
                #print(jogadores_escolhidos_na_proxima_rodada)
                print("Jogadores na lista de Escolhidos a somar no valor de C")
                C_proxima_rodada = C
                #Atualizar time com valores do time na segunda rodada
                for i in jogadores_escolhidos_na_proxima_rodada:
                    #print(i[3])
                    C_proxima_rodada += float(i[3])
                print("Quantidade de cartoletas para a proxima rodada: " + str(C_proxima_rodada) )

                # "Vende" o time e Atualiza o C para a próxima rodada
                C = C_proxima_rodada
                
            print("TERMINOU O CÁLCULO PARA A RODADA " + str(rodada) + " COM O ESQUEMA TÁTICO: " + str(q_i))
            print(len(epsilons), "len(epsilons)")
            print("############################################################################################\n\n")

run()

