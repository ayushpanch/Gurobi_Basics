import gurobipy as gp
from gurobipy import GRB

#first step setting up the first model
basic_model=gp.Model("basic_model")
print(basic_model)  

# second step creating of variables
# X is product 1 and Y is product 2 
X = basic_model.addVar(vtype =GRB.CONTINUOUS,name = "X")
Y = basic_model.addVar(vtype =GRB.CONTINUOUS,name = "Y")

# third step set objective function
basic_model.setObjective(400*X + 200*Y,GRB.MAXIMIZE)

# fourth step Add constraints 
basic_model.addConstr(2*X + 1*Y <= 8,"first constraint")
basic_model.addConstr(1*X + 2*Y <= 8,"second constraint")
basic_model.addConstr(X>=0,'fourth constraint')
basic_model.addConstr(Y>=0,'fifth constraint')


basic_model.optimize()
basic_model.write("exercise_2.sol")
basic_model
for v in basic_model.getVars():
    print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % basic_model.ObjVal)


