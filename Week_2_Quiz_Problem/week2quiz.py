import gurobipy as gp
from gurobipy import GRB
import pandas
import os 

#first step setting up the first model
basic_model=gp.Model("basic_model")
print(basic_model)  


months = ['C1','C2','T1','T2','S1','S2','IC1','IT1','IC2','IT2']
# Create decision variables with meaningful names using list comprehension
decision_vars = [basic_model.addVar(vtype=GRB.CONTINUOUS, name=every_month) for every_month in months]

# second step creating of variables 
basic_model.update()

basic_model.setObjective(400*basic_model.getVars()[4] + 600*basic_model.getVars()[5] + 150*basic_model.getVars()[6]\
                          + 150*basic_model.getVars()[7] + 150*basic_model.getVars()[8]  +150*basic_model.getVars()[9] ,GRB.MINIMIZE)   


# fourth step to add constraints 
"""first constraint """

basic_model.addConstr( basic_model.getVars()[0] + basic_model.getVars()[2] <=1000 , name="Production capcacity constraints part 1")
basic_model.addConstr( basic_model.getVars()[1] + basic_model.getVars()[3] <=1000 , name="Production capcacity constraints part 2")

basic_model.addConstr( basic_model.getVars()[0] + 2*basic_model.getVars()[2]  == basic_model.getVars()[4] ,\
                       name="Steel usage constraints part 1")

basic_model.addConstr( basic_model.getVars()[1] + 2*basic_model.getVars()[3]  == basic_model.getVars()[5] ,\
                       name="Steel usage constraints part 2")

basic_model.addConstr( basic_model.getVars()[0] - basic_model.getVars()[6]  == 600,\
                       name="Material balence  car month 1")

basic_model.addConstr( basic_model.getVars()[2] - basic_model.getVars()[7]  == 300,\
                       name="Material balence truck month 1")
# IC1 +C2 -IC2
basic_model.addConstr( basic_model.getVars()[6]  +  basic_model.getVars()[1]  - basic_model.getVars()[8]   == 300,\
                       name="Material balence car month 2")

# IT1 +T2 -IT2 =300
basic_model.addConstr( basic_model.getVars()[3]  +  basic_model.getVars()[7]  - basic_model.getVars()[9]   == 300,\
                       name="Material balence Truck month 2")
#4C1 -6T1 >=0
basic_model.addConstr( 4*basic_model.getVars()[0]  +  6*basic_model.getVars()[2]   >= 0,\
                       name="fuel eff part 1")
#4C2 -6T2
basic_model.addConstr( 4*basic_model.getVars()[1]  +  6*basic_model.getVars()[3]   >= 0,\
                       name="fuel eff part 2")
#S1 
basic_model.addConstr( basic_model.getVars()[4] >= 0,\
                       name="fuel eff part 2")
#S2
basic_model.addConstr( basic_model.getVars()[5] >= 0,\
                       name="fuel eff part 2")


"""writting the linear programming to understand what we have written is right or wrong """
basic_model.write("week2quiz.lp")


"""optmizing the problem"""
basic_model.optimize()

"""writting the solution file"""
basic_model.write("week2quiz.sol")

for v in basic_model.getVars():
    print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % basic_model.ObjVal)

