import sys, heapq
from pprint import pprint
from sys import stdout as out
from operator import indexOf
from unittest.mock import Mock
from mip import Model, xsum, maximize, minimize, BINARY, CBC
from mip.constants import OptimizationStatus
import DbConnector
from mockBase import MockBase

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
    q_nome_posicao = ["tec","gol","zag","lat","mei","ata"]
    m = Model("Modelo Montagem de Elenco", solver_name=CBC)
    gama = []
    mock_base = MockBase()
    #Array com ids das possíveis posições dos jogadores
    P = ["tec", "gol", "zag", "lat", "mei", "ata"]
    #P = []

    contador = 0
    
    #for q in q_i:
    #    for i in range(q):
    #        P.append(q_nome_posicao[contador])
    #        escolha = banco.BuscarJogadoresPorRodadaEPosicao(rodada, q_nome_posicao[contador])
    #        #gama.append(escolha)
    #    contador+=1

    tecnicos = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "tec")
    #tecnicos = mock_base[0]
    gama.append(tecnicos)

    goleiros = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "gol")
    #goleiros = mock_base[1]
    gama.append(goleiros)

    zagueiros = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "zag")
    #zagueiros = mock_base[2]
    gama.append(zagueiros)
    
    laterais = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "lat")
    #laterais = mock_base[3]
    gama.append(laterais)
    
    meias = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "mei")
    #meias = mock_base[4]
    gama.append(meias)
    
    ataques = banco.BuscarJogadoresPorRodadaEPosicao(rodada, "ata")
    #ataques = mock_base[5]
    gama.append(ataques)
    
    #q_i = [1,1,2,1,1,1]

    #Variavel de dominio y
    #y = [[m.add_var(name='y', var_type=BINARY) for j in range(len(J)) ] for i in range(len(P))]
    y = [[m.add_var(name='y', var_type=BINARY) for j in range(len(gama[i])) ] for i in range(len(P))]

    # Restrição 3.6
    for i in range(len(P)):
        m += xsum(y[i][j] for j in range(len(gama[i]))) <= q_i[i]
    #m += xsum(y[0][j] for j in range(len(gama[0]))) <= 1
    #m += xsum(y[1][j] for j in range(len(gama[1]))) <= 1
    #m += xsum(y[2][j] for j in range(len(gama[2]))) <= 1
    #m += xsum(y[3][j] for j in range(len(gama[3]))) <= 1
    #m += xsum(y[4][j] for j in range(len(gama[4]))) <= 1
    #m += xsum(y[5][j] for j in range(len(gama[5]))) <= 1
    #m += xsum(y[6][j] for j in range(len(gama[6]))) <= 1
    #m += xsum(y[7][j] for j in range(len(gama[7]))) <= 1
    #m += xsum(y[8][j] for j in range(len(gama[8]))) <= 1
    #m += xsum(y[9][j] for j in range(len(gama[9]))) <= 1
    #m += xsum(y[10][j] for j in range(len(gama[10]))) <= 1
    #m += xsum(y[11][j] for j in range(len(gama[11]))) <= 1

    #m += xsum([y[i][j] for i in range(len(P))] for j in range(len (J)) <= 1
    #print("fim da restricao 3.6")

    
    #Restricao 3.5
    for i in range(len(P)):
        m += xsum(y[i][j] for j in range(len(gama[i]))) == q_i[i]
    
    #m += xsum(y[0][j] for j in range(len(gama[0]))) == 1
    #m += xsum(y[1][j] for j in range(len(gama[1]))) == 1
    #m += xsum(y[2][j] for j in range(len(gama[2]))) == 1
    #m += xsum(y[3][j] for j in range(len(gama[3]))) == 1
    #m += xsum(y[4][j] for j in range(len(gama[4]))) == 1
    #m += xsum(y[5][j] for j in range(len(gama[5]))) == 1
    #m += xsum(y[6][j] for j in range(len(gama[6]))) == 1
    #m += xsum(y[7][j] for j in range(len(gama[7]))) == 1
    #m += xsum(y[8][j] for j in range(len(gama[8]))) == 1
    #m += xsum(y[9][j] for j in range(len(gama[9]))) == 1
    #m += xsum(y[10][j] for j in range(len(gama[10]))) == 1
    #m += xsum(y[11][j] for j in range(len(gama[11]))) == 1
    
    #m.add_constr(xsum(y[5][j] for j in range(len(gama[5]))) == 1)

    #print("fim da restricao 3.5")
    #m += xsum([y[i][j] for i in range(len(P))] for j in range(len (J)) <= 1)
    
    #Restricao 3.3 (que "vira" a 3.2)
    for i in range(len(P)):
        #m += xsum(c[j] * y[i][j] for j in range(len(gama[i]))) <= epsilon
        #m += xsum(c[j] * y[i][j] for j in range(len(gama[i]))) <= 1000
        
        m += xsum(float(gama[i][j][2]) * y[i][j] for j in range(len(gama[i]))) <= epsilon
        #m += xsum(float(gama[i][j][2]) * y[i][j] for j in range(len(gama[i]))) <= 1000

    #print("fim da restricao 3.3")

    #m.objective = minimize(expr)

    #Função Objetivo 3.1
    for i in range(len(P)):
        #somatorio_score = xsum(a[j] * y[i][j] for j in range(len(gama[i])))
        somatorio_score = xsum(float(gama[i][j][3]) * y[i][j] for j in range(len(gama[i])))
    
    m.objective = maximize(somatorio_score)
    m.verbose = 0
    solucao = m.optimize()

    for i in range(len(y)):
        for j in range(len(y[i])): 
            if y[i][j].x >= 0.99:
                print("y[" + str(i) + "][" + str(j) + "].x = " + str(y[i][j].x) + " -> ESCOLHIDO PELO ALGORITMO")
            else:
                print("y[" + str(i) + "][" + str(j) + "].x = " + str(y[i][j].x))

    #for j in range(len(J)):
    #    for i in range(len(P)):
    #        if y[i][j] == 1:
    #            sei_la.append(y[i][j])
    #sel = [i for i in range(len(y)) if y[i].x == 1]

    #if m.num_solutions:
    #    out.write('objective_value: %g \n' % (m.objective_value))
    #else:
    #    print("NÃO ACHOU SOLUÇÃO")
    #    sys.exit()

    if solucao == OptimizationStatus.OPTIMAL:
        print('optimal solution cost {} found'.format(m.objective_value))
    
    elif solucao == OptimizationStatus.FEASIBLE:
        print('sol.cost {} found, best possible: {}'.format(m.objective_value, m.objective_bound))
    elif solucao == OptimizationStatus.NO_SOLUTION_FOUND:
        print('no feasible solution found, lower bound is: {}'.format(m.objective_bound))
        
    #if status == OptimizationStatus.OPTIMAL or status == OptimizationStatus.FEASIBLE:print('solution:')

    jogadores_escolhidos = []
    print(P, "P")
    custo_jogadores_escolhidos = 0
    for i in range(len(P)):
        #print(gama[i])
        #print("gama[" + str(i) + "]")
        # q_i = [1,1,3,2,2]
        for j in range(len(gama[i])):
            #print(j, "j")
            #print(q_i[i])
            #print("q_i[" + str(i) + "]")
            if y[i][j].x >= 0.99:
                # REVER AQUI (LEMBRAR DO Q_I)
                #id_jogador = J[j]
                id_jogador = gama[i][j][1]
                custo_jogadores_escolhidos += gama[i][j][2]
                jogadores_escolhidos.append(banco.BuscarJogadorPorId(id_jogador))
    print(jogadores_escolhidos, "jogadores_escolhidos")
    #print(len(jogadores_escolhidos), "len(jogadores_escolhidos)")
    return m.objective_value, jogadores_escolhidos, custo_jogadores_escolhidos
    
def run(perfis = [], q = [], rodadas = []):
    C = 100
    solucoes = []
    conjunto_solucoes = []
    #Deixando somente 1 perfil para teste
    perfis = [1]
    limite_rodadas = 1
    #[tecnico, goleiro, zagueiro, lateral, meia, ataque]
    q_nome_posicao = ["tec","gol","zag","lat","mei","ata"]
    q = [
        [1,1,2,2,4,2],
        [1,1,3,2,3,2]
    ]
    for perfil in perfis:
        # q_i é o esquema tático
        for q_i in q:
            print("COMEÇOU O ESQUEMA TÁTICO: \n" + str(q_i))
            # Incrementa o limite_rodadas porque o Python não considera o valor limite no laço de repetição
            for rodada in range(1, limite_rodadas+1):
                jogadores_ja_escolhidos = []
                print("COMEÇOU A RODADA: \n" + str(rodada))

                # TODO: BUSCAR O NOVO CUSTO PARA A PRÓXIMA RODADA
                #if rodada != 1:
                #    C += custo_jogadores_escolhidos

                time_mais_barato = []
                contador = 0
                
                # Calcula o time mais barato possível na rodada
                #q_i = [1,1,3,2,3,2]
                for i in range(len(q_i)):
                    print("Comecando posicao: " + q_nome_posicao[i])
                    print(contador, "contador")

                    jogadores_posicao, valores_escolhas, scores_escolhas = FormatarJogadoresPorRodada(banco.BuscarJogadoresPorRodadaEPosicao(rodada, q_nome_posicao[i]))
                    
                    escolhas_mais_barato = heapq.nsmallest(q_i[i], valores_escolhas)
                    
                    print(valores_escolhas, "valores_escolhas")

                    contador+=1
                    #limite_inferior_epsilon = 0
                    for escolha in escolhas_mais_barato:
                        print("Novo jogador encontrado na posicao: " + q_nome_posicao[i])
                        #gama_estrutura.append(escolha)
                        indice_escolha_mais_barato=indexOf(valores_escolhas, escolha)
                        jogador_escolhido = jogadores_posicao[indice_escolha_mais_barato]
                        # Impede o jogador de ser escolhido duaas vezes em posições diferentes. (Exemplo do William Arão)
                        if jogador_escolhido not in jogadores_ja_escolhidos:
                            jogadores_ja_escolhidos.append(jogador_escolhido)
                            time_mais_barato.append(jogador_escolhido)
                    #        limite_inferior_epsilon += valores_escolhas[indice_escolha_mais_barato]
                            print(jogador_escolhido, "jogador_escolhido")

                limite_inferior_epsilon = 0
                print("\n\nTIME MAIS BARATO CALCULADO PARA EPSILON")
                for jogador_id in time_mais_barato:
                    jogador = banco.BuscarJogadorPorId(jogador_id)
                    #  Soma os custos para o cálculo do Limite inferior de Epsilon
                    limite_inferior_epsilon += jogador[3]
                    nome_jogador = str(jogador[0])
                    #id_jogador = str(jogador[1])
                    posicao_jogador = str(jogador[2])
                    custo_jogador = str(jogador[3])
                    score_jogador = str(jogador[4])

                    print("Jogador: " + nome_jogador + "(" + posicao_jogador + ") -> " + score_jogador + " pontos; Custo: " + custo_jogador )

                print("LIMITE INFERIOR CALCULADO PARA O EPSILON: " + str(limite_inferior_epsilon))

                # Aqui vai carregar todos os jogadores disponíveis NAQUELA RODADA
                jogadores_por_rodada = banco.BuscarTodosJogadoresPorRodada(rodada)
                # Formata variáveis para entrada na função que calcula o modelo
                J, c, a = FormatarJogadoresPorRodada(jogadores_por_rodada)
                
                epsilon = limite_inferior_epsilon
                epsilons = []
                while epsilon < C:
                    # Chega perto dos casos em que estourem o valor de Cartoletas
                    if (epsilon + min(valores_escolhas)) > C:
                        epsilon = C
                    else:
                        epsilon += min(valores_escolhas) 
                    epsilons.append(epsilon)

                custo_jogadores_escolhidos = 0
                for epsilon in epsilons:
                    solucao_maior_score, jogadores_escolhidos, custo_jogadores_escolhidos = CalcularModelo(rodada, J, c, a, q_i, epsilon)
                    #solucao_menor_custo = maximize()
                    solucoes.append(solucao_maior_score)
                    #print(solucao_maior_score, "solucao")
                    print(epsilon, "epsilon\n")
                    #epsilons.append(epsilon)
                
                # TODO: ATUALIZA A QUANTIDADE DE CARTOLETAS DISPONIVEL PARA A PRÓXIMA RODADA
                #diferenca_cartoletas_custo = C - custo_jogadores_escolhidos
                #print("Novo Valor de Cartoletas Calculado: " + str(C))

            print("TERMINOU O CÁLCULO PARA A RODADA " + str(rodada) + " COM O ESQUEMA TÁTICO: " + str(q_i))
            #conjunto_solucoes.append(solucoes)
            print(len(epsilons), "len(epsilons)")
            print("############################################################################################\n\n")
            #print("COMEÇA PRINT SOLUÇÕES")
            #pprint(solucoes)
            #print("TERMINA PRINT SOLUÇÕES")
            #print("COMEÇA PRINT EPSILONS")
            #pprint(epsilons)
            #print("TERMINA PRINT EPSILONS")

            
            #sys.exit()
run()

