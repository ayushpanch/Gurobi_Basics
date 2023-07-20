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
Z1 = basic_model.addVar(vtype =GRB.CONTINUOUS,name = "Z1")
Z2= basic_model.addVar(vtype =GRB.CONTINUOUS,name = "Z2")


# third step set objective function
basic_model.setObjective(50*X1 + 61*X2 + 83*Y1 + 97*Y2 + 130*Z1 + 145*Z2,GRB.MINIMIZE)

# fourth step Add constraints 
basic_model.addConstr(2*X1+ 1.5*Y1 +3*Z1 <=10000,"first constraint")
basic_model.addConstr(1*X1 +2*Y1 +1*Z1 <=5000,"second constraint")
basic_model.addConstr(X1+X2 ==3000,'third constraint')
basic_model.addConstr(Y1+Y2 ==2000,'fourth constraint')
basic_model.addConstr(Z1+Z2 == 1000,'fifth constraint')
basic_model.addConstr(X1>=0,'fifth constraint')
basic_model.addConstr(X2>=0,'sixth constraint')
basic_model.addConstr(Y1>=0,'seventh constraint')
basic_model.addConstr(Y2>=0,'eight constraint')
basic_model.addConstr(Z1>=0,'Ninth constraint')
basic_model.addConstr(Z2>=0,'tenth constraint')

# write the linear programming equation
basic_model.write('case_study_problem.lp')

# optimise the solution
basic_model.optimize()

# write the solution to .sol file
basic_model.write("case_study_problem.sol")


basic_model
for v in basic_model.getVars():
    print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % basic_model.ObjVal)

