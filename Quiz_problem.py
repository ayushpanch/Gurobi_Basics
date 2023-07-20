import gurobipy as gp
from gurobipy import GRB

#first step setting up the first model
basic_model=gp.Model("basic_model")
print(basic_model)  

# second step creating of variables 
X = basic_model.addVar(vtype =GRB.CONTINUOUS,name = "X")
Y= basic_model.addVar(vtype =GRB.CONTINUOUS,name = "Y")
Z = basic_model.addVar(vtype =GRB.CONTINUOUS,name = "Z")

# X Y AND Z are three suppliers


# third step set objective function
basic_model.setObjective(5*X+ 4*Y + 3*Z  ,GRB.MINIMIZE)

# fourth step Add constraints 
basic_model.addConstr(.4*X+ .3*Y +.2*Z  >=500,"first constraint")
basic_model.addConstr(.4*X+ .35*Y +.2*Z >=300,"second constraint")
basic_model.addConstr(.2*X+ 0.35*Y +.6*Z  >=300,'third constraint')
# basic_model.addConstr(X1 >=50,'fourth constraint')
# basic_model.addConstr(X2+Y1  1000,'fifth constraint')
basic_model.addConstr(X <=700,'fifth constraint')
basic_model.addConstr(Y <=700,'sixth constraint')
basic_model.addConstr(Z <=700,'seventh constraint')
basic_model.addConstr(Z>=0,'eight constraint')
basic_model.addConstr(X>=0,'Ninth constraint')
basic_model.addConstr(Y>=0,'tenth constraint')



# write the linear programming equation
basic_model.write('Quiz_problem.lp')

# optimise the solution
basic_model.optimize()

# write the solution to .sol file
basic_model.write("Quiz_problem.sol")


basic_model
for v in basic_model.getVars():
    print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % basic_model.ObjVal)

