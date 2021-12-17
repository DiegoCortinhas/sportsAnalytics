from mip import Model, xsum, maximize, minimize, BINARY, CBC

m = Model("Modelo Montagem de Elenco", solver_name=CBC)
cartoleta_inicial = 100

J=[1,2,3,4,5]
P=[1,2,3,4,5,6,7,8,9,10,11]

goleiro = []
defesa = []
meia = []
ataque = []
#id de todos goleiros, id todos os jogadores de defesa
#quais jogadores podem jogar em cada posição destas
gama = [goleiro,defesa,meia,ataque]


f1y = maximize(xsum(a[i][j]*y[i][j] for i in P for j in J))
f2y = minimize(xsum(c[i][j]*y[i][j] for i in P for j in J))

#y = [[model.add_var(var_type=BINARY) for j in J] for i in P]
C = 2

y = [m.add_var(var_type=BINARY) for i in P, for j in J]

#Restricao 3.5
for j in J:
    expr = 0
    for i in P: 
        expr += y[i][j]
    m.add_constr(expr <=1)

#Restricao 3.5
for j in J:
    expr = xsum(y[i][j] for i in P)
    m.add_constr(expr <=1)

q = [1,4,4,2]

#Restricao 3.4
for i in P:
    expr = xsum(y[i][j] for j in gama[i])
    m.add_constr(expr = q[i])

y = xsum(variavel_dominio[i] for i in P) 
restricao_3_5 = somatorio_yij <= 1
m.add_constr(restricao_3_5)

qi = xsum(q[i] for i in P)

y_2 = xsum(variavel_dominio[j] for j in L) 
restricao_3_4 = somatorio_yij_2 == qi
m.add_constr(restricao_3_4)

restricao_3_3 = f2y <= C
m.add_constr(restricao_3_3)

m.objective = f1y
m.optimize()