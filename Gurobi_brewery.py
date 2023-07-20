import gurobipy as gp
from gurobipy import GRB

#first step setting up the first model
basic_model=gp.Model("basic_model")
print(basic_model)  

# second step creating of variables 
X = basic_model.addVar(vtype =GRB.CONTINUOUS,name = "X")
Y = basic_model.addVar(vtype =GRB.CONTINUOUS,name = "Y")

# third step set objective function
basic_model.setObjective(13*X + 23*Y,GRB.MAXIMIZE)

# fourth step Add constraints 
basic_model.addConstr(5*X + 15*Y <= 480,"first constraint")
basic_model.addConstr(4*X + 4*Y <= 160,"second constraint")
basic_model.addConstr(35*X + 20*Y <=1190,'third constraint')
basic_model.addConstr(X>=0,'fourth constraint')
basic_model.addConstr(Y>=0,'fifth constraint')


basic_model.optimize()
print(f"the outcomes of optimisations are ---- {basic_model.printAttr('X')}")
basic_model
for v in basic_model.getVars():
    print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % basic_model.ObjVal)


