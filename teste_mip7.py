import sys, heapq
from pprint import pprint
from sys import stdout as out
from operator import indexOf
from mip import Model, xsum, maximize, minimize, BINARY, CBC
import DbConnector

banco = DbConnector.DbConnector()

def FormatarJogadoresPorRodada(jogadores_por_rodada):
    jogadores_resultado = []
    custo_jogadores_resultado = []
    score_jogadores_resultado = []

    for jogador in jogadores_por_rodada:
        jogadores_resultado.append(jogador[1])
        custo_jogadores_resultado.append(jogador[2])
        score_jogadores_resultado.append(jogador[3])

    return jogadores_resultado, custo_jogadores_resultado, score_jogadores_resultado


def CalcularModelo(rodada, J, c, a, q_i, epsilon, gama_estrutura):

    m = Model("Modelo Montagem de Elenco", solver_name=CBC)
    
    #Array com ids das posições dos jogadores
    P = ["tecnico", "goleiro", "zagueiro", "lateral", "meia", "atacante"]

    #tecnico = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "tec")
    ##valores_tecnico = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "tec")
    #tecnico_mais_barato = heapq.nsmallest(1, tecnico(2))
#
    #goleiro = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "gol")
    #goleiro_mais_barato = heapq.nsmallest(1, goleiro(2))
#
    #zagueiro = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "zag")
    #zagueiro_mais_barato = heapq.nsmallest(1, zagueiro(2))
    #
    #lateral = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "lat")
    #lateral_mais_barato = heapq.nsmallest(1, lateral(2))
    #
    #meia = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "mei")
    #meia_mais_barato = heapq.nsmallest(1, meia(2))
    #
    #ataque = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "ata")
    #ataque_mais_barato = heapq.nsmallest(1, ataque(2))

    #id de todos goleiros, id todos os jogadores de defesa
    #quais jogadores podem jogar em cada posição destas
    gama = [gama_estrutura[0], gama_estrutura[1], gama_estrutura[2], gama_estrutura[3], gama_estrutura[4], gama_estrutura[5]]
    

    #Variavel de dominio y
    y = [[m.add_var(name='y', var_type=BINARY) for j in range(len(J)) ] for i in range(len(P))]

    #y = m.var_by_name('y')
    # #Restricao 3.6
    # for j in range(len(J)):
    #     expr=0
    #     for i in range(len(P)):
    #         print(i,"i")
    #         print(j,"j")
    #         y_aux = y[i][j]
    #         expr += y_aux
    #     m.add_constr(expr<=1)

    for j in range(len(J)):
        m += xsum(y[i][j] for i in range(len(P))) <= 1

    #m += xsum([y[i][j] for i in range(len(P))] for j in range(len (J)) <= 1
    print("fim da restricao 3.6")

    #Restricao 3.5
    expr = 0
    for i in range(len(P)):
        m += xsum(y[i][j] for j in range(len(gama[i]))) == q_i[i]

    print("fim da restricao 3.5")
    #m += xsum([y[i][j] for i in range(len(P))] for j in range(len (J)) <= 1)

    #Restricao 3.3 (que "vira" a 3.2)
    for j in range(len(J)):
        m += xsum(c[j] * y[i][j] for i in range(len(P))) <= epsilon

    print("fim da restricao 3.3")

    #m.objective = minimize(expr)

    #Função Objetivo 3.1
    for j in range(len(J)):
        somatorio_score = xsum(a[j] * y[i][j] for i in range(len(P)))

    m.objective = maximize(somatorio_score)
    solucao = m.optimize()
    sei_la = []
    #for j in range(len(J)):
    #    for i in range(len(P)):
    #        if y[i][j] == 1:
    #            sei_la.append(y[i][j])
    #sel = [i for i in range(len(y)) if y[i].x == 1]

    if m.num_solutions:
        out.write('objective_value: %g \n' % (m.objective_value))
    #else:
    #    print("NÃO ACHOU SOLUÇÃO")
    #    sys.exit()
    return m.objective_value
    #return sei_la
    
def run(perfis = [], q = [], rodadas = []):
    C = 100
    solucoes = []
    #Deixando somente 1 perfil para teste
    perfis = [1]
    limite_rodadas = 5
    #[tecnico, goleiro, zagueiro, lateral, meia, ataque]
    q_nome_posicao = ["tec","gol","zag","lat","mei","ata"]
    q = [
        #[1,1,2,2,4,2],
        [1,1,3,2,3,2]
    ]
    for perfil in perfis:
        # q_i é o esquema tático
        for q_i in q:
            print("COMEÇOU O ESQUEMA TÁTICO: \n" + str(q_i))
            # Incrementa o limite_rodadas porque o Python não considera o valor limite no laço de repetição
            for rodada in range(1, limite_rodadas+1):

                print("COMEÇOU A RODADA: \n" + str(rodada))

                # Cartoletas iniciais
                
                # Aqui vai carregar todos os jogadores disponíveis NAQUELA RODADA
                jogadores_por_rodada = banco.BuscarTodosJogadoresPorRodada(rodada)
                J, c, a = FormatarJogadoresPorRodada(jogadores_por_rodada)

                # Pega os mínimos preços dos jogadores por seçao do campo na rodada para ter os limites de epsilons
                """
                sum(heapq.nsmallest(q_i,c_q0)) + sum(heapq.nsmallest(q[1],c_q1)) + sum(heapq.nsmallest(q[3],c_q3))
                """
                gama_estrutura = []
                time_mais_barato = []
                
                tecnico, valores_tecnicos, _ = FormatarJogadoresPorRodada(banco.BuscarJogadoresPorRodadaEPosicao(rodada, "tec"))
                tecnico_mais_barato = heapq.nsmallest(1, valores_tecnicos)[0]
                #tecnico_mais_barato_sql = banco.BuscarJogadoresPorRodadaPrecoEScore(rodada=rodada,preco=tecnico_mais_barato,score=0,posicao="tec")
                gama_estrutura.append(tecnico)
                indice_tecnico_mais_barato=indexOf(valores_tecnicos,tecnico_mais_barato)
                time_mais_barato.append(tecnico[indice_tecnico_mais_barato])
                print(tecnico[indice_tecnico_mais_barato],"tecnico")
            

                goleiro, valores_goleiros, _ = FormatarJogadoresPorRodada(banco.BuscarJogadoresPorRodadaEPosicao(rodada, "gol"))
                goleiro_mais_barato = heapq.nsmallest(1, valores_goleiros)[0]
                #goleiro_mais_barato_sql = banco.BuscarJogadoresPorRodadaPrecoEScore(rodada=rodada,preco=goleiro_mais_barato,posicao='gol')
                gama_estrutura.append(goleiro)
                indice_goleiro_mais_barato=indexOf(valores_goleiros,goleiro_mais_barato)
                print(goleiro[indice_goleiro_mais_barato],"goleiro")
                time_mais_barato.append(goleiro[indice_goleiro_mais_barato])

                #rever como fazer lista com mais de 1 zagueiro mais barato
                zagueiros_selecionados = []
                zagueiro, valores_zagueiros, _ = FormatarJogadoresPorRodada(banco.BuscarJogadoresPorRodadaEPosicao(rodada, "zag"))
                zagueiro_mais_barato = heapq.nsmallest(1, valores_zagueiros)[0]

                #zagueiro_mais_barato_sql = banco.BuscarJogadoresPorRodadaPrecoEScore(rodada=rodada,preco=zagueiro_mais_barato,posicao='zag')
                gama_estrutura.append(zagueiro)
                indice_zagueiro_mais_barato=indexOf(valores_zagueiros,zagueiro_mais_barato)
                print(zagueiro[indice_zagueiro_mais_barato],"zagueiro")
                time_mais_barato.append(zagueiro[indice_zagueiro_mais_barato])
                
                lateral, valores_laterais, _ = FormatarJogadoresPorRodada(banco.BuscarJogadoresPorRodadaEPosicao(rodada, "lat"))
                lateral_mais_barato = heapq.nsmallest(1, valores_laterais)[0]
                #lateral_mais_barato_sql = banco.BuscarJogadoresPorRodadaPrecoEScore(rodada=rodada,preco=lateral_mais_barato,posicao='lat')
                gama_estrutura.append(lateral)
                indice_lateral_mais_barato=indexOf(valores_laterais,lateral_mais_barato)
                print(lateral[indice_lateral_mais_barato],"lateral")
                time_mais_barato.append(lateral[indice_lateral_mais_barato])
                #print(lateral_mais_barato,"Lateral Mais Barato")

                meia, valores_meias, _ = FormatarJogadoresPorRodada(banco.BuscarJogadoresPorRodadaEPosicao(rodada, "mei"))
                meia_mais_barato = heapq.nsmallest(1, valores_meias)[0]
                #meia_mais_barato_sql = banco.BuscarJogadoresPorRodadaPrecoEScore(rodada=rodada,preco=meia_mais_barato,posicao='mei')
                gama_estrutura.append(meia)
                indice_meia_mais_barato=indexOf(valores_meias,meia_mais_barato)
                print(meia[indice_meia_mais_barato],"meia")
                time_mais_barato.append(meia[indice_meia_mais_barato])
                #print(meia_mais_barato,"Meia Mais Barato")
                
                ataque, valores_ataque, _ = FormatarJogadoresPorRodada(banco.BuscarJogadoresPorRodadaEPosicao(rodada, "ata"))
                ataque_mais_barato = heapq.nsmallest(1, valores_ataque)[0]
                #ataque_mais_barato_sql = banco.BuscarJogadoresPorRodadaPrecoEScore(rodada=rodada,preco=ataque_mais_barato,posicao='ata')
                gama_estrutura.append(ataque)
                indice_ataque_mais_barato=indexOf(valores_ataque,ataque_mais_barato)
                print(ataque[indice_ataque_mais_barato],"ataque")
                time_mais_barato.append(ataque[indice_ataque_mais_barato])
                

                print(time_mais_barato,"time mais baratos por posicao")
                #print(goleiro_mais_barato_sql, "Goleiro mais barato")
                # Colocar epsilon variando em "min(c) vezes"
                # OBS: colocamos 12 porque agora tem o técnico tbm
                soma_epsilons = tecnico_mais_barato + goleiro_mais_barato + zagueiro_mais_barato + lateral_mais_barato + meia_mais_barato + ataque_mais_barato
                print(soma_epsilons)
                sys.exit()

                epsilon = soma_epsilons
                epsilons = []
                while epsilon < C:
                    # Chega perto dos casos em que estourem o valor de Cartoletas
                    if (epsilon + min(c)) > C:
                        epsilon = C
                    else:
                        epsilon += min(c)
                        
                    epsilons.append(epsilon) 
                
                for epsilon in epsilons:
                    solucao = CalcularModelo(rodada, J, c, a, q_i, epsilon, gama_estrutura)
                    solucoes.append(solucao)

            print("COMEÇA PRINT SOLUÇÕES")
            pprint(solucoes)
            print("TERMINA PRINT SOLUÇÕES")
            #print("COMEÇA PRINT EPSILONS")
            #pprint(epsilons)
            #print("TERMINA PRINT EPSILONS")

            
            #sys.exit()
run()


