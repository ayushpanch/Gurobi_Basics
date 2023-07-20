import gurobipy as gp
from gurobipy import GRB

#first step setting up the first model
basic_model=gp.Model("basic_model")
print(basic_model)  

# second step creating of variables 
X = basic_model.addVar(vtype =GRB.CONTINUOUS,name = "X")
Y = basic_model.addVar(vtype =GRB.CONTINUOUS,name = "Y")

# third step set objective function
basic_model.setObjective(350*X + 300*Y,GRB.MAXIMIZE)

# fourth step Add constraints 
basic_model.addConstr(6*X + 9*Y <= 1566,"first constraint")
basic_model.addConstr(16*X + 12*Y <= 2880,"second constraint")
basic_model.addConstr(X + Y <=200,'third constraint')
basic_model.addConstr(X>=0,'fourth constraint')
basic_model.addConstr(Y>=0,'fifth constraint')


basic_model.optimize()
basic_model
for v in basic_model.getVars():
    print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % basic_model.ObjVal)


