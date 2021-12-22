from mip import Model, xsum, maximize, minimize, BINARY, CBC

def BuscarJogadores(nome_posicao):
    #TODO: Função que vai retornar os jogadores e os seus respectivos custos

    if nome_posicao is not None:
        # Aqui vai buscar todos os jogadores por posicao
        pass
    else:
        # Aqui vai buscar todos os jogadores da base de dados
        pass

    # VALORES MOCKADOS
    # vai virar o array "J"
    jogadores_resultado = [1,2,3]
    # vai virar PARTE DO ARRAY "c"
    custos_jogadores_resultado = [10,20,30]
    # vai virar o array "a"
    score_jogadores_resultado = [10,10,10]
    return jogadores_resultado, custos_jogadores_resultado, score_jogadores_resultado

def VariarEpsilon(epsilon, c, C):
    if epsilon != min(c) or epsilon is None:
        # Define o valor de Epsilon na primeira execução da recursão
        epsilon = min(c)
    else:
        if epsilon <= C:
            #TODO: Aqui vem a dinâmica de, a partir dos limites, ir incrementando o epsilon
            pass

    return epsilon

def AtualizarCusto(C):
    #TODO: Aqui vai vir a lógica para ir "tirando o dinheiro" a cada novo jogador na escalação
    pass

#Parametro de definicao da Esquema tático 
#q = [1,4,4,2]
def CalcularModelo(solucoes = [], q = [], C = 100):

    m = Model("Modelo Montagem de Elenco", solver_name=CBC)
    
    # Aqui vai carregar todos os jogadores disponíveis na base diretamente na memória.
    J, c, a = BuscarJogadores()

    #Array com ids dos jogadores
    #J=[1,2,3,4,5]

    #Array com ids das posições dos jogadores
    P = [1,2,3,4,5,6,7,8,9,10,11]

    #Array simulando os custos dos jogadores
    #c = [10.0,15.5,11.6,14.0,9.8,7.6,5.9,9.9,10.0,13.2,11.5]

    #Valor de cartoletas iniciais
    C = 100

    # Array simulando os scores dos jogadores
    #a = [9,9,9,9,9,9,9,9,9,9,9]

    goleiro = BuscarJogadores("goleiro")
    #goleiro = [1,2,3,4,5,6,7,8,9,0,1,2111,121,21,22,11,21,1,12,22,12,2,12,12,1]
    defesa = BuscarJogadores("defesa")
    #defesa = [65,4,45,456,65,4,43,4,43,45,454,4,5,445,34]
    meia = BuscarJogadores("meia")
    #meia = [56,54,45,3434,34,667,56,67,7634,4353,4]
    ataque = BuscarJogadores("ataque")
    #ataque = [676,67,65,78,5,65,5,45,45,45]

    #id de todos goleiros, id todos os jogadores de defesa
    #quais jogadores podem jogar em cada posição destas
    gama = [goleiro,defesa,meia,ataque]


    #Variavel de dominio y
    y = [m.add_var(var_type=BINARY) for i in P, for j in J]

    #Restricao 3.5
    for j in J:
        expr = 0
        for i in P: 
            expr += y[i][j]
        m.add_constr(expr <=1)


    #Restricao 3.4
    for i in P:
        expr = 0
        for j in gama[i]:
            expr += y[i][j]
        m.add_constr(expr == q[i])

    #Restricao 3.3
    for i in P:
        expr = 0
        for j in J:
            expr += c[j] * y[i][j]
        m.add_constr(expr <= C)

    #Função Objetivo 3.2 -> Vai virar a restrição
    for i in P:
        for j in J:
            expr += c[j]*y[i][j]
        # TODO: Aqui vai começar o Epsilon
        epsilon = VariarEpsilon(epsilon, c, C)
        m.add_constr(expr <= epsilon)
    #m.objective = minimize(expr)

    #Função Objetivo 3.1
    for i in P:
        for j in J:
            expr += a[j] * y[i][j]
        
    m.objective = maximize(expr)
    solucao = m.optimize()
    solucoes.append(solucao.objective_values)
    AtualizarCj(c, solucao)
    C = AtualizarCusto(C)

    if epsilon == C:
        # Criterio de parada da Recursão
        return solucoes
    
    CalcularModelo(solucoes, q, C)


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