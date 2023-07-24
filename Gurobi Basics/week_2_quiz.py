import gurobipy as gp
from gurobipy import GRB

#first step setting up the first model
basic_model=gp.Model("basic_model")
print(basic_model)  

# second step creating of variables 
X = basic_model.addVar(vtype =GRB.CONTINUOUS,name = "X")
Y= basic_model.addVar(vtype =GRB.CONTINUOUS,name = "Y")


# third step set objective function
basic_model.setObjective(3*X + 2*Y,GRB.MAXIMIZE)

# fourth step Add constraints 
basic_model.addConstr(2*X + 1*Y<=100,"first constraint")
basic_model.addConstr(1*X + 1*Y <=80,"second constraint")
basic_model.addConstr(X<=40,"third constraint")
basic_model.addConstr(X>=0,"fourth constraint")
basic_model.addConstr(X>=0,"fifth constraint")


# write the linear programming equation
basic_model.write('Week_2_quiz.lp')

# optimise the solution
basic_model.optimize()

# write the solution to .sol file
basic_model.write("Week_2_quiz.sol")


basic_model
for v in basic_model.getVars():
    print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % basic_model.ObjVal)

