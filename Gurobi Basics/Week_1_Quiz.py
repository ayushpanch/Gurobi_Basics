import gurobipy as gp
from gurobipy import GRB

#first step setting up the first model
basic_model=gp.Model("basic_model")
print(basic_model)  

# second step creating of variables 
X = basic_model.addVar(vtype =GRB.CONTINUOUS,name = "X")
Y= basic_model.addVar(vtype =GRB.CONTINUOUS,name = "Y")
Z = basic_model.addVar(vtype =GRB.CONTINUOUS,name = "Z")


# third step set objective function
basic_model.setObjective(X + Y +Z -1,GRB.MINIMIZE)

# fourth step Add constraints 
basic_model.addConstr(X-Y<=4,"first constraint")
basic_model.addConstr(Y+Z<=9,"second constraint")
basic_model.addConstr(Z-X>=2,'third constraint')

# write the linear programming equation
basic_model.write('week_1_practice_questions.lp')

# optimise the solution
basic_model.optimize()

# write the solution to .sol file
basic_model.write("week_1_practice_questions.sol")


basic_model
for v in basic_model.getVars():
    print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % basic_model.ObjVal)

