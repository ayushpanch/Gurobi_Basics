import os,numpy,pandas
from pyexpat import model

######### to run the gurobi you should have liscene installed ##########
from gurobipy import *
######### creating the model first ###########


md = Model(name="model_ex_1")

######### Declaring the variables ##########

x = md.addVar(lb=0,ub=3,vtype=GRB.CONTINUOUS, name="X")
y = md.addVar(lb=0,vtype=GRB.CONTINUOUS, name="Y")

######## SET OBJECTIVE FUNCTION ##############
md.setObjective(-4*x-2*y, GRB.MINIMIZE )

####### setting up the constraints ############
constraint_1 = md.addConstr(lhs = x+y,rhs =8,sense =GRB.LESS_EQUAL)
constraint_2 = md.addConstr(lhs = 8*x+3*y,rhs =-24,sense =GRB.GREATER_EQUAL)
constraint_3 = md.addConstr(lhs = 3*x+5*y,rhs =15,sense =GRB.LESS_EQUAL)
constraint_4 = md.addConstr(lhs = -6*x+8*y,rhs =48,sense =GRB.LESS_EQUAL)

####### optimise the model ############
md.optimize()
if md.status == GRB.OPTIMAL:
    md.printAttr('X')
    print("the model is optimal")
else:
    print("model is not optimal")

print(md.display())

print(md.printAttr("X"))






