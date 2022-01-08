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
    
    solucoes = []
    perfis = [1,2,3,4]
    limite_rodadas = 2
    #[tecnico, goleiro, zagueiro, lateral, meia, ataque]
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
                C = 100
                # Aqui vai carregar todos os jogadores disponíveis NAQUELA RODADA
                jogadores_por_rodada = banco.BuscarTodosJogadoresPorRodada(rodada)
                J, c, a = FormatarJogadoresPorRodada(jogadores_por_rodada)

                # Pega os mínimos preços dos jogadores por seçao do campo na rodada para ter os limites de epsilons
                """
                sum(heapq.nsmallest(q_i,c_q0)) + sum(heapq.nsmallest(q[1],c_q1)) + sum(heapq.nsmallest(q[3],c_q3))
                """
                gama_estrutura = []
                
                tecnico, valores_tecnicos, _ = FormatarJogadoresPorRodada(banco.BuscarJogadoresPorRodadaEPosicao(rodada, "tec"))
                tecnico_mais_barato = heapq.nsmallest(1, valores_tecnicos)[0]
                gama_estrutura.append(tecnico)

                goleiro, valores_goleiros, _ = FormatarJogadoresPorRodada(banco.BuscarJogadoresPorRodadaEPosicao(rodada, "gol"))
                goleiro_mais_barato = heapq.nsmallest(1, valores_goleiros)[0]
                gama_estrutura.append(goleiro)

                zagueiro, valores_zagueiros, _ = FormatarJogadoresPorRodada(banco.BuscarJogadoresPorRodadaEPosicao(rodada, "zag"))
                zagueiro_mais_barato = heapq.nsmallest(1, valores_zagueiros)[0]
                gama_estrutura.append(zagueiro)
                
                lateral, valores_laterais, _ = FormatarJogadoresPorRodada(banco.BuscarJogadoresPorRodadaEPosicao(rodada, "lat"))
                lateral_mais_barato = heapq.nsmallest(1, valores_laterais)[0]
                gama_estrutura.append(lateral)
                
                meia, valores_meias, _ = FormatarJogadoresPorRodada(banco.BuscarJogadoresPorRodadaEPosicao(rodada, "mei"))
                meia_mais_barato = heapq.nsmallest(1, valores_meias)[0]
                gama_estrutura.append(meia)
                
                ataque, valores_ataque, _ = FormatarJogadoresPorRodada(banco.BuscarJogadoresPorRodadaEPosicao(rodada, "ata"))
                ataque_mais_barato = heapq.nsmallest(1, valores_ataque)[0]
                gama_estrutura.append(ataque)
                
                # Colocar epsilon variando em "min(c) vezes"
                # OBS: colocamos 12 porque agora tem o técnico tbm
                soma_epsilons = tecnico_mais_barato + goleiro_mais_barato + zagueiro_mais_barato + lateral_mais_barato + meia_mais_barato + ataque_mais_barato

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

            
            sys.exit()
run()


'''
#Restricao 3.5
for j in J:
expr = xsum(y[i][j] for i in P)
m.add_constr(expr <=1)

y = xsum(variavel_dominio[i] for i in P) 
restricao_3_5 = somatorio_yij <= 1
m.add_constr(restricao_3_5)

qi = xsum(q[i] for i in P)

y_2 = xsum(variavel_dominio[j] for j in L) 
restricao_3_4 = somatorio_yij_2 == qi
m.add_constr(restricao_3_4)

restricao_3_3 = f2y <= C
m.add_constr(restricao_3_3)


f1y = maximize(xsum(a[i][j]*y[i][j] for i in P for j in J))
f2y = minimize(xsum(c[i][j]*y[i][j] for i in P for j in J))

#y = [[model.add_var(var_type=BINARY) for j in J] for i in P]

#for i in P:
#    expr = xsum(y[i][j] for j in gama[i])
#    m.add_constr(expr = q[i])

m.objective = f1y
m.optimize()
'''