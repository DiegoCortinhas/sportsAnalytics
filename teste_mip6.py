import sys, heapq
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


def CalcularModelo(rodada, J, c, a, q_i, epsilon):

    m = Model("Modelo Montagem de Elenco", solver_name=CBC)
    
    #Array com ids das posições dos jogadores
    P = ["tecnico", "goleiro", "zagueiro", "lateral", "meia", "atacante"]

    tecnico = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "tec")
    #goleiro = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "gol")
    #zagueiro = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "zag")
    #lateral = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "lat")
    #meia = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "mei")
    #ataque = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "ata")

    #id de todos goleiros, id todos os jogadores de defesa
    #quais jogadores podem jogar em cada posição destas
    #gama = [tecnico, goleiro, zagueiro, lateral, meia, ataque]
    gama = [tecnico]

    #Variavel de dominio y
    y = [[m.add_var(name='y', var_type=BINARY) for i in P ] for j in J]
    #y = m.var_by_name('y')
    #print(len(J), "len j")

    #Restricao 3.6
    for j in J:
        m += xsum(y[i][j] for i in range(len(P)) <=1

    #m += xsum([y[i][j] for i in range(len(P))] for j in range(len (J)) <= 1
    #print("fim da restricao 3.6")

    #Restricao 3.5
    for i in range(len(P)):
        m+= xsum(y[i][j] for j in gama[i]) == q_i[i]
        #expr = 0
        #for j in gama[i]:
        #    expr += y[i][j]
        #m.add_constr(expr == q_i[i])

    #m += xsum([y[i][j] for i in range(len(P))] for j in range(len (J)) <= 1)

    
    #Restricao 3.3 (que "vira" a 3.2)
    for i in P:
        expr = 0
        for j in J:
            expr += c[j] * y[i][j]
        m.add_constr(expr <= epsilon)

    #m.objective = minimize(expr)

    #Função Objetivo 3.1
    expr = 0
    for i in P:
        for j in J:
            expr += a[j] * y[i][j]
        
    m.objective = maximize(expr)
    solucao = m.optimize()
    print(solucao, "solucao")
    return solucao
    
def run(perfis = [], q = [], rodadas = []):
    #resultado = banco.BuscarJogadoresPorRodadaEPosicao(1, "gol")
    resultado = banco.BuscarTodosJogadoresPorRodada(1)

    solucoes = []
    perfis = [1,2,3,4]
    q = [1,1,2,2,4,2]
    for perfil in perfis:
        # q_i é o esquema tático
        for q_i in q:
            for rodada in range(1,2):
                # Cartoletas iniciais
                C = 100
                # Aqui vai carregar todos os jogadores disponíveis NAQUELA RODADA
                jogadores_por_rodada = banco.BuscarTodosJogadoresPorRodada(rodada)
                J, c, a = FormatarJogadoresPorRodada(jogadores_por_rodada)

                # Pega os mínimos preços dos jogadores por seçao do campo na rodada para ter os limites de epsilons
                """
                sum(heapq.nsmallest(q_i,c_q0)) + sum(heapq.nsmallest(q[1],c_q1)) + sum(heapq.nsmallest(q[3],c_q3))
                """
                
                # Colocar epsilon variando em "min(c) vezes"
                soma_epsilons = sum(heapq.nsmallest(11,c))
                epsilon = soma_epsilons
                epsilons = []
                while epsilon < C:
                    # Chega perto dos casos em que estourem o valor de Cartoletas
                    if (epsilon + min(c)) > C:
                        epsilon = C
                    else:
                        epsilon += min(c)
                        
                    epsilons.append(epsilon) 
                
                #print(J)
                #print(c)
                #print(a)
                #print(epsilons, "epsilons")
                
                for epsilon in epsilons:
                    #print(epsilon, "epsilon")
                    solucao = CalcularModelo(rodada, J, c, a, q_i, epsilon)
                    solucao = []
                    solucoes.append(solucao)
                    #print(min(c), "min(c)")
                    #print(solucao)
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