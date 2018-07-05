from pulp import *
from scipy.optimize import linprog
import time

start = time.time()
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
x3 = pulp.LpVariable("x3", lowBound=0)
x4 = pulp.LpVariable("x4", lowBound=0)
x5 = pulp.LpVariable("x5", lowBound=0)
x6 = pulp.LpVariable("x6", lowBound=0)
problem = pulp.LpProblem('0', pulp.LpMaximize)
problem += 1.96 * (x1 + x2 + x3) + 2.08 * (x4 + x5 + x6) - \
           (1.08 * (x1 + x4) + 0.96 * (x2 + x5) + 0.5 * (x3 + x6)), "Функция цели"
problem += x1 >= 0.3 * (x1 + x2 + x3), "1"
problem += x3 <= 0.5 * (x1 + x2 + x3), "2"
problem += x5 >= 0.6 * (x4 + x5 + x6), "3"
problem += x6 <= 0.3 * (x4 + x5 + x6), "4"

problem += x1 + x2 + x3 <= 200, "5"
problem += x4 + x5 + x6 <= 180, "6"

problem += x1 + x4 == 100, "7"
problem += x2 + x5 == 130, "8"
problem += x3 + x6 == 150, "9"

problem.solve()
print("Результат:")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
print("прибыль:")
print(value(problem.objective))
stop = time.time()
print("Время :")
print(stop - start)
