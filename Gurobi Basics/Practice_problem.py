import gurobipy as gp
from gurobipy import GRB

#first step setting up the first model
basic_model=gp.Model("basic_model")
print(basic_model)  

# second step creating of variables 
X1 = basic_model.addVar(vtype =GRB.CONTINUOUS,name = "X1")
X2= basic_model.addVar(vtype =GRB.CONTINUOUS,name = "X2")
Y1 = basic_model.addVar(vtype =GRB.CONTINUOUS,name = "Y1")
Y2= basic_model.addVar(vtype =GRB.CONTINUOUS,name = "Y2")
# Z1 = basic_model.addVar(vtype =GRB.CONTINUOUS,name = "Z1")
# Z2= basic_model.addVar(vtype =GRB.CONTINUOUS,name = "Z2")


# third step set objective function
basic_model.setObjective(6*X1 + 4*X2 + 6*Y1 + 8*Y2 ,GRB.MAXIMIZE)

# fourth step Add constraints 
basic_model.addConstr(3*X1+ 2*X2 +2*Y1 +4*Y2 <=480,"first constraint")
basic_model.addConstr(1*X1+ 1*X2 +2*Y1 +3*Y2 <=400,"second constraint")
basic_model.addConstr(2*X1+ 1*X2 +2*Y1 +1*Y2 <=400,'third constraint')
# basic_model.addConstr(X1 >=50,'fourth constraint')
# basic_model.addConstr(X2+Y1  1000,'fifth constraint')
basic_model.addConstr(X1 >=50,'fifth constraint')
basic_model.addConstr(X2 +Y1 >=100,'sixth constraint')
basic_model.addConstr(Y2<=25,'seventh constraint')
basic_model.addConstr(Y2>=0,'eight constraint')
basic_model.addConstr(X1>=0,'Ninth constraint')
basic_model.addConstr(X2>=0,'tenth constraint')
basic_model.addConstr(Y1>=0,'Ninth constraint')
basic_model.addConstr(Y2>=0,'tenth constraint')



# write the linear programming equation
basic_model.write('practice_problem.lp')

# optimise the solution
basic_model.optimize()

# write the solution to .sol file
basic_model.write("Pracrice_problem_another.sol")


basic_model
for v in basic_model.getVars():
    print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % basic_model.ObjVal)

