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
basic_model.setObjective(X + Y,GRB.MAXIMIZE)

# fourth step Add constraints 
basic_model.addConstr(X + Y <= 100,"first constraint")
basic_model.addConstr(-X + Y >= 200,"second constraint")
basic_model.addConstr(X>=0,'fourth constraint')
basic_model.addConstr(Y>=0,'fifth constraint')

# problems with unbounded solution is that where the solution can go upto infinity either positive infinity or negative infinity
basic_model.write("infeasible_solution.lp")
basic_model.optimize()
# basic_model.write("infeasible_solution.sol")

##### when you get Unable to retrieve attribute 'X' ### that means the solution is \
# infeasible where there is no value of X and Y which can satisfy both the lines
# basic_model.write("unbounded_solution.sol")


# the basic model status will tell me whether the solution is infeasible or unbounded or optimal 
# 4 - unbounded or infeasible 
# 2 - optimal
basic_model
print(f"the status of the model is -----------{basic_model.Status}")
for v in basic_model.getVars():
    print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % basic_model.ObjVal)
