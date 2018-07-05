from scipy.optimize import linprog
import time
from pulp import *

start = time.time()
# c = [1, 1, 0, 0, 0, 0]  # Функция цели
# A_eq = [[3, 2, 1, 0, 0, 0],
#         [1, 0, 0, 1, 0, 0],
#         [1, 0, 0, 0, -1, 0],
#         [0, 1, 0, 0, 0, 1]]  # выражения вида ==
# b_eq = [10, 5, 2, 3]  # '2'
# print(linprog(c, A_eq=A_eq, b_eq=b_eq))
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
problem = pulp.LpProblem('0', pulp.LpMaximize)
problem += x1 - x2, "Функция цели"
problem += (3 * x1 + 2 * x2) <= 10, "1"
problem += x1 <= 5, "2"
problem += x1 >= 2, "3"
problem += x2 <=3
problem.solve()
print("Результат:")
for variable in problem.variables():
    print(variable.name, "=", variable.varValue)
print("q = {0}".format(value(problem.objective)))
stop = time.time()
print("Время :")
print(stop - start)
