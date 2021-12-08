from mip import Model, xsum, maximize, BINARY

p = [10, 13, 18, 31, 7, 15]
w = [11, 15, 20, 35, 10, 33]
c, I = 47, range(len(Y))
J = [1,2,3,4,5]
J_len = range(len(J))

# Y = [0,1,2,3,4,5,6,7,8,9,10]
P = [J_len,J_len,J_len,J_len,J_len,J_len,J_len,J_len,J_len,J_len,J_len]

m = Model("Modelo Montagem de Elenco", solver_name=CBC)

#Definindo variavel dominio do Problema - 3.6
yij = [m.add_var(var_type=BINARY) for i,j in P]

#Definindo restrição - 3.5
m += xsum(yij[i] for i in P) <= 1

#Definindo restrição - 3.4

#Definindo as Funções Objetivo
m.objective = maximize(

blabla = [xsum(y[i][j])]

m.objective = maximize(xsum(p[i] * x[i] for i in I))

m += xsum(w[i] * x[i] for i in I) <= c

m.optimize()

selected = [i for i in I if x[i].x >= 0.99]
print("selected items: {}".format(selected))