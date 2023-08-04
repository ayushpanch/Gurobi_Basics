import gurobipy as gp
from gurobipy import GRB
import pandas
import os 

# Reading the Excel file because now we will solve the same equation via data 
# df= pandas.read_csv(r"C:\Users\panch\Desktop\Gurobi\Week_3\Staffing_Problem\staffing_problem.csv")
# df.columns=[x.strip() for x in df.columns]
# df.shape[0]
Decision_variables_names = ["Feed_1",'Feed_2','Feed_3','Feed_4']


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
basic_model.setObjective(0.25*basic_model.getVars()[0] + 0.3*basic_model.getVars()[1] \
                         +0.32*basic_model.getVars()[2] + 0.15*basic_model.getVars()[3],GRB.MINIMIZE)   

# fourth step to add constraints 
"""first constraint """

basic_model.addConstr((basic_model.getVars()[0] +basic_model.getVars()[1] \
                      +basic_model.getVars()[2] + basic_model.getVars()[3]  )  == 8000, name = "total demand" )

basic_model.addConstr((.1*basic_model.getVars()[0] +.3*basic_model.getVars()[1] \
                      +.15*basic_model.getVars()[2] + .1*basic_model.getVars()[3]  )  >= 8000*.15      \
                            , name = "grains Constraint" )

basic_model.addConstr((.3*basic_model.getVars()[0] +0.05*basic_model.getVars()[1] \
                      +.2*basic_model.getVars()[2] + .1*basic_model.getVars()[3]  )  >= 8000*.2      \
                            , name = "corn Constraint" )

basic_model.addConstr((.2*basic_model.getVars()[0] +0.2*basic_model.getVars()[1] \
                      +.2*basic_model.getVars()[2] + .3*basic_model.getVars()[3]  )  >= 8000*.15      \
                            , name = "mineral Constraint" )

# basic_model.addConstrs(x >=0  for x in basic_model.getVars())



"""writting the linear programming to understand what we have written is right or wrong """
basic_model.write("blending.lp")


"""optmizing the problem"""
basic_model.optimize()

"""writting the solution file"""
basic_model.write("blending.sol")

for v in basic_model.getVars():
    print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % basic_model.ObjVal)

