import gurobipy as gp
from gurobipy import GRB
import pandas
import os 
from helper_functions import *
# Reading the Excel file because now we will solve the same equation via data 
# df= pandas.read_csv(r"C:\Users\panch\Desktop\Gurobi\Week_3\Staffing_Problem\staffing_problem.csv")
# df.columns=[x.strip() for x in df.columns]
# df.shape[0]
Decision_variables_names = ['A','B','C','D1','E1','D2','E2','M1','M2','M3']


#first step setting up the first model
basic_model=gp.Model("basic_model")
print(basic_model)  

# Create decision variables with meaningful names using list comprehension
decision_vars = [basic_model.addVar(vtype=GRB.CONTINUOUS, name=individual_decision_variable) for individual_decision_variable in Decision_variables_names]
# for name in Decision_variables_names:
#     locals()[name] = basic_model.addVar(vtype=GRB.CONTINUOUS, name=name)
# second step creating of variables 
basic_model.update()

# third step setting up the objective functions 

# lets see if our helper functions gives us what we need 

 #writting here 
basic_model.setObjective(3*basic_model.getVars()[0] + 3*basic_model.getVars()[1] \
                         +3*basic_model.getVars()[2]+3*basic_model.getVars()[3] \
                            + 3*basic_model.getVars()[4]  + 2*basic_model.getVars()[5] \
                            + 2*basic_model.getVars()[6] - 4*basic_model.getVars()[7] 
                             +4*basic_model.getVars()[8] + 4*basic_model.getVars()[9] 
                           ,GRB.MAXIMIZE)   

# fourth step to add constraints 
"""first constraint """
 

basic_model.addConstr(basic_model.getVars()[3] <=20 , name = "D1 <=20" )
basic_model.addConstr(basic_model.getVars()[4] <=20 , name = "E1 <=20" )
basic_model.addConstr(basic_model.getVars()[7] <=120 , name = "M1 <=120" )
basic_model.addConstr(basic_model.getVars()[8] <=120 , name = "M2 <=120" )
basic_model.addConstr(basic_model.getVars()[9] <=120 , name = "M3 <=120" )

basic_model.addConstr((12*basic_model.getVars()[0] +7*basic_model.getVars()[1] \
                      +8*basic_model.getVars()[2] + 10*(basic_model.getVars()[3] + basic_model.getVars()[5]) \
                      +7*(basic_model.getVars()[4] + basic_model.getVars()[6]) )  == 60*basic_model.getVars()[7]      \
                            , name = "M1 Constraint" )

basic_model.addConstr((8*basic_model.getVars()[0] +9*basic_model.getVars()[1] \
                      +4*basic_model.getVars()[2] + 0*(basic_model.getVars()[3] + basic_model.getVars()[5]) \
                      +11*(basic_model.getVars()[4] + basic_model.getVars()[6]) )  == 60*basic_model.getVars()[8]      \
                            , name = "M2 Constraint" )

basic_model.addConstr((5*basic_model.getVars()[0] +10*basic_model.getVars()[1] \
                      +7*basic_model.getVars()[2] + 3*(basic_model.getVars()[3] + basic_model.getVars()[5]) \
                      +2*(basic_model.getVars()[4] + basic_model.getVars()[6]) )  == 60*basic_model.getVars()[9]      \
                            , name = "M3 Constraint" )




"""writting the linear programming to understand what we have written is right or wrong """
basic_model.write("Product_Mix_problem.lp")


"""optmizing the problem"""
basic_model.optimize()

"""writting the solution file"""
basic_model.write("Product_Mix_problem.sol")

for v in basic_model.getVars():
    print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % basic_model.ObjVal)

