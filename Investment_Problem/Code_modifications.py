import gurobipy as gp
from gurobipy import GRB

""" in this we will read the excel and we will try to formulate according to Excel not manually writting it """

#first step setting up the first model
basic_model=gp.Model("basic_model")
print(basic_model)  

# second step creating of variables 


decision_variables= basic_model.addVars([x for x in range(1,7)],vtype =GRB.CONTINUOUS,name ="Decsion Variables")
# decision_variables = [basic_model.addVar(x,vtype =GRB.CONTINUOUS,name ="Decsion Variables") for x in range(1,7)]
#update the model to include the variable
basic_model.update()

#objective functions
basic_model.setObjective(0.0865*basic_model.getVars()[0]\
                        + 0.0952*basic_model.getVars()[1] \
                        + .10*basic_model.getVars()[2] +\
                        0.0875*basic_model.getVars()[3] \
                        +0.0925*basic_model.getVars()[4]\
                        +0.09*basic_model.getVars()[5],\
                        GRB.MAXIMIZE)

basic_model.write("testing.lp")


# fourth step Add constraints 
"""first constraint"""
# basic_model.addConstr(X1 + X2 + X3 +X4 +X5 +X6  == 750000,"total invest amount")
basic_model.addConstr(gp.quicksum(basic_model.getVars()) == 750000,"total invest amount")


"""second constraint"""
# basic_model.addConstr(X1 <= 187500,"25percent for decision variable 1")
# basic_model.addConstr(X2 <= 187500,"25percent for decision variable 2")
# basic_model.addConstr(X3 <= 187500,"25percent for decision variable 3")
# basic_model.addConstr(X4 <= 187500,"25percent for decision variable 4")
# basic_model.addConstr(X5 <= 187500,"25percent for decision variable 5")
# basic_model.addConstr(X6 <= 187500,"25percent for decision variable 6")

# basic_model.addConstrs([x for x in basic_model.getVars()]<= 187500,"25percent for decision variable 6")
basic_model.addConstrs(decision_variables[x] <= 187500 for x in range(0,6))

# basic_model.write("testing.lp")


"""third constraint"""
# basic_model.addConstr(X1 + X2  +X4  +X6  >= 375000,"Long Investment")

basic_model.addConstr(basic_model.getVars()[0] +\
                        basic_model.getVars()[1] +\
                        basic_model.getVars()[2] + basic_model.getVars()[5] \
                         >= 375000,"Long Investment")

# basic_model.write("testing.lp")
"""fourth constraint"""
# basic_model.addConstr(X2 +X3  +X5  <= 262500,"High Risk Investment")
basic_model.addConstr(basic_model.getVars()[1] +basic_model.getVars()[2]  +basic_model.getVars()[4]  <= 262500,"High Risk Investment")


# write the linear programming equation
basic_model.write('Investment_problem_Advanced.lp')

# optimise the solution
basic_model.optimize()

# write the solution to .sol file
basic_model.write("Investment_problem_Advanced.sol")


basic_model
for v in basic_model.getVars():
    print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % basic_model.ObjVal)

