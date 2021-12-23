import sys
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


def CalcularModelo(rodada, J, c, a, q_i = [], epsilon = 100):

    m = Model("Modelo Montagem de Elenco", solver_name=CBC)
    
    #Array com ids das posições dos jogadores
    P = [1,2,3,4,5,6,7,8,9,10,11]

    tecnico = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "tec")
    goleiro = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "gol")
    zagueiro = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "zag")
    lateral = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "lat")
    meia = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "mei")
    ataque = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "ata")

    #id de todos goleiros, id todos os jogadores de defesa
    #quais jogadores podem jogar em cada posição destas
    gama = [tecnico, goleiro, zagueiro, lateral, meia, ataque]


    #Variavel de dominio y
    y = [m.add_var(var_type=BINARY) for i in P for j in J]

    #Restricao 3.5
    for j in J:
        expr = 0
        for i in P: 
            expr += y[i][j]
        m.add_constr(expr <= 1)


    #Restricao 3.4
    for i in P:
        expr = 0
        for j in gama[i]:
            expr += y[i][j]
        m.add_constr(expr == q_i[i])

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
            for rodada in range(1,38):
                # Cartoletas iniciais
                C = 100
                # Aqui vai carregar todos os jogadores disponíveis NAQUELA RODADA
                jogadores_por_rodada = banco.BuscarTodosJogadoresPorRodada(rodada)
                J, c, a = FormatarJogadoresPorRodada(jogadores_por_rodada)
                
                epsilons = range(1, C, min(c)) 
                
                #print(J)
                #print(c)
                #print(a)
                #print(epsilons, "epsilons")
                for epsilon in epsilons:
                    print(epsilon)
                    #solucao = CalcularModelo(rodada, J, c, a, q_i, epsilon)
                    #solucoes.append(solucao)
                print(min(c), "min(c)")
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