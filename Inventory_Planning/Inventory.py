import gurobipy as gp
from gurobipy import GRB
import pandas
import os 




#first step setting up the first model
basic_model=gp.Model("basic_model")
print(basic_model)  


months = ['month_1','month_2','month_3','month_4']
# Create decision variables with meaningful names using list comprehension
decision_vars = [basic_model.addVar(vtype=GRB.CONTINUOUS, name=every_month) for every_month in months]

# second step creating of variables 
basic_model.update()

# third step setting up the objective functions 


 #writting here
# 49*basic_model.getVars()[0] +45*basic_model.getVars()[1] + 46*basic_model.getVars()[2] + 47*basic_model.getVars()[3] +\
# 1.5*(120  + basic_model.getVars()[0] -300)/2 +\
#       1.5*((basic_model.getVars()[0]-300) + (basic_model.getVars()[0] +basic_model.getVars()[1] -880 ))/2 +\
#       1.5*((basic_model.getVars()[0] +basic_model.getVars()[1] -880) + \
#            (basic_model.getVars()[0] +basic_model.getVars()[1] +basic_model.getVars()[2] -1190))/2 +\
#             1.5 * ((basic_model.getVars()[0] +basic_model.getVars()[1] +basic_model.getVars()[2] -1190 ) +\
#              (basic_model.getVars()[0] + basic_model.getVars()[1] +basic_model.getVars()[2] +basic_model.getVars()[3] -1730))/2




basic_model.setObjective(49*basic_model.getVars()[0] +45*basic_model.getVars()[1] +\
                          46*basic_model.getVars()[2] + 47*basic_model.getVars()[3] +\
1.5*(120  + basic_model.getVars()[0] -300)/2 +\
      1.5*((basic_model.getVars()[0]-300) + (basic_model.getVars()[0] +basic_model.getVars()[1] -880 ))/2 +\
      1.5*((basic_model.getVars()[0] +basic_model.getVars()[1] -880) + \
           (basic_model.getVars()[0] +basic_model.getVars()[1] +basic_model.getVars()[2] -1190))/2 +\
            1.5 * ((basic_model.getVars()[0] +basic_model.getVars()[1] +basic_model.getVars()[2] -1190 ) +\
             (basic_model.getVars()[0] + basic_model.getVars()[1] +basic_model.getVars()[2] +basic_model.getVars()[3] -1730))/2
,GRB.MINIMIZE)   

# fourth step to add constraints 
"""first constraint """
# basic_model.addConstr(gp.quicksum([basic_model.getVars()[x] for x in positions]) <=200000 ,"Storage capacity in Houston")
basic_model.addConstr( basic_model.getVars()[0] == [400, 500], name="Month_1_units_constraints")
basic_model.addConstr( basic_model.getVars()[1] == [400, 520], name="Month_1_units_constraints")
basic_model.addConstr( basic_model.getVars()[2] == [400, 450], name="Month_1_units_constraints")
basic_model.addConstr( basic_model.getVars()[3] == [400, 550], name="Month_1_units_constraints")

"""second constraint """
basic_model.addConstr( basic_model.getVars()[0] -300 == [50, 130], name="Month_1_Inventory_constraints")
basic_model.addConstr( basic_model.getVars()[0] + basic_model.getVars()[1] -880  == [50, 130], name="Month_2_Inventory_constraints")
basic_model.addConstr( basic_model.getVars()[0] + basic_model.getVars()[1] + basic_model.getVars()[2] -1190   == [50, 130], name="Month_3_Inventory_constraints")
basic_model.addConstr( basic_model.getVars()[0] + basic_model.getVars()[1] + basic_model.getVars()[2] +\
                      basic_model.getVars()[3] -1730 == [50, 130], name="Month_4_Inventory_constraints")


"""writting the linear programming to understand what we have written is right or wrong """
basic_model.write("Inventory.lp")


"""optmizing the problem"""
basic_model.optimize()

"""writting the solution file"""
basic_model.write("Inventory.sol")

for v in basic_model.getVars():
    print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % basic_model.ObjVal)

