import gurobipy as gp
from gurobipy import GRB

#first step setting up the first model
basic_model=gp.Model("basic_model")
print(basic_model)  

# second step creating of variables 
X = basic_model.addVar(vtype =GRB.CONTINUOUS,name = "X")
Y= basic_model.addVar(vtype =GRB.CONTINUOUS,name = "Y")


# third step set objective function
basic_model.setObjective(50*X + 100*Y,GRB.MINIMIZE)

# fourth step Add constraints 
basic_model.addConstr(7*X + 2*Y>=28,"first constraint")
basic_model.addConstr(2*X + 12*Y>=24,"second constraint")
basic_model.addConstr(X>=0,"fourth constraint")
basic_model.addConstr(X>=0,"fifth constraint")


# write the linear programming equation
basic_model.write('Week_3_quiz.lp')

# optimise the solution
basic_model.optimize()

# write the solution to .sol file
basic_model.write("Week_3_quiz.sol")


basic_model
for v in basic_model.getVars():
    print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % basic_model.ObjVal)

