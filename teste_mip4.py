from mip import Model, xsum, maximize, minimize, BINARY, CBC

m = Model("Modelo Montagem de Elenco", solver_name=CBC)
c_inicial = 100

J=[1,2,3,4,5]
P=[1,2,3,4,5,6,7,8,9,10,11]

f1y = maximize(xsum(a[i][j]*y[i][j] for i in P for j in J))
f2y = minimize(xsum(c[i][j]*y[i][j] for i in P for j in J))

#y = [[model.add_var(var_type=BINARY) for j in J] for i in P]



yij = [m.add_var(var_type=BINARY) for i in P, for j in J]
somatorio_yij = xsum(yij for i in P) 
C = 2
restricao_3_5 = somatorio_yij <= 1
m.add_constr(restricao_3_5)

m.add_constr(f2y <= C)

m.objective = f1y
