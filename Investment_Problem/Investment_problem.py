import gurobipy as gp
from gurobipy import GRB

#first step setting up the first model
basic_model=gp.Model("basic_model")
print(basic_model)  

# second step creating of variables 
X1 = basic_model.addVar(vtype =GRB.CONTINUOUS,name = "X1")
X2= basic_model.addVar(vtype =GRB.CONTINUOUS,name = "X2")
X3 = basic_model.addVar(vtype =GRB.CONTINUOUS,name = "X3")
X4= basic_model.addVar(vtype =GRB.CONTINUOUS,name = "X4")
X5 = basic_model.addVar(vtype =GRB.CONTINUOUS,name = "X5")
X6= basic_model.addVar(vtype =GRB.CONTINUOUS,name = "X6")



# third step set objective function
basic_model.setObjective(0.0865*X1 + 0.0952*X2 + .10*X3 + 0.0875*X4 +0.0925*X5 +0.09*X6, GRB.MAXIMIZE)

# fourth step Add constraints 
"""first constraint"""
basic_model.addConstr(X1 + X2 + X3 +X4 +X5 +X6  == 750000,"total invest amount")

"""second constraint"""
basic_model.addConstr(X1 <= 187500,"25percent for decision variable 1")
basic_model.addConstr(X2 <= 187500,"25percent for decision variable 2")
basic_model.addConstr(X3 <= 187500,"25percent for decision variable 3")
basic_model.addConstr(X4 <= 187500,"25percent for decision variable 4")
basic_model.addConstr(X5 <= 187500,"25percent for decision variable 5")
basic_model.addConstr(X6 <= 187500,"25percent for decision variable 6")

"""third constraint"""
basic_model.addConstr(X1 + X2  +X4  +X6  >= 375000,"Long Investment")

"""fourth constraint"""
basic_model.addConstr(X2 +X3  +X5  <= 262500,"High Risk Investment")



# write the linear programming equation
basic_model.write('Investment_problem.lp')

# optimise the solution
basic_model.optimize()

# write the solution to .sol file
basic_model.write("Investment_problem.sol")


basic_model
for v in basic_model.getVars():
    print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % basic_model.ObjVal)

