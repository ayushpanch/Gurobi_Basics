from gurobipy import GRB
try:
    GRB.GRBEnv()
    print("Gurobi license is active.")
except GurobiError:
    print("Gurobi license is not active.")