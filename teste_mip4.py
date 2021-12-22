from mip import Model, xsum, maximize, minimize, BINARY, CBC

m = Model("Modelo Montagem de Elenco", solver_name=CBC)

#Array com ids dos jogadores
J=[1,2,3,4,5]
#Array com ids das Possiveis posições dos jogadores
P=[1,2,3,4,5,6,7,8,9,10,11]
#Parametro de definicao da Esquema tático 
q = [1,4,4,2]
#Array simulando os custos dos jogadores
c = [10.0,15.5,11.6,14.0,9.8,7.6,5.9,9.9,10.0,13.2,11.5]
#Valor de cartoletas iniciais
C = 100

goleiro = []
defesa = []
meia = []
ataque = []
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
    expr = xsum(y[i][j] for j in gama[i])
    m.add_constr(expr = q[i])

#Restricao 3.3
for i in P:
    expr = 0
    for j in J:
        expr += c[j] * y[i][j]
    m.add_constr(expr<=C)

#Função Objetivo 3.2
for i in P:
    for j in J:
        expr += c[j]*y[i][j]
m.objective = minimize(expr)

a = []
#Função Objetivo 3.1
for i in P:
    for j in J:
        expr += a[j]*y[i][j]
m.objective = maximize(expr)



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


m.objective = f1y
m.optimize()
'''