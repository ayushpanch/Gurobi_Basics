import gurobipy as gp
from gurobipy import GRB
import pandas
import os 

# Reading the Excel file because now we will solve the same equation via data 
# df= pandas.read_csv(r"C:\Users\panch\Desktop\Gurobi\Week_3\Staffing_Problem\staffing_problem.csv")
# df.columns=[x.strip() for x in df.columns]
# df.shape[0]

Decision_variables_names = ['A','B','C','D','E','F','G']


#first step setting up the first model
basic_model=gp.Model("basic_model")
print(basic_model)  

# Create decision variables with meaningful names using list comprehension
decision_vars = [basic_model.addVar(vtype=GRB.INTEGER, name=individual_decision_variable) for individual_decision_variable in Decision_variables_names]

# second step creating of variables 
basic_model.update()

# third step setting up the objective functions 


 #writting here 
basic_model.setObjective((2200*(basic_model.getVars()[0] +
                       basic_model.getVars()[1] + 
                       basic_model.getVars()[2] + 
                       basic_model.getVars()[3] +
                       basic_model.getVars()[4]+
                       basic_model.getVars()[5])+
                       2000*basic_model.getVars()[6] )  ,GRB.MINIMIZE)   
# Thursday is wrong
# fourth step to add constraints 
"""first constraint """
basic_model.addConstr((basic_model.getVars()[1] +
                       basic_model.getVars()[2] + 
                       basic_model.getVars()[3] + 
                       basic_model.getVars()[4] +
                       basic_model.getVars()[5]) >= 22 , name = "employees coming on sunday" )

"second constraint"
"""Second constraint """
basic_model.addConstr((basic_model.getVars()[2] +
                       basic_model.getVars()[3] + 
                       basic_model.getVars()[4] + 
                       basic_model.getVars()[5] +
                       basic_model.getVars()[6]) >= 17 , name = "employees coming on monday" )



"""Third constraint """
basic_model.addConstr((basic_model.getVars()[3] +
                       basic_model.getVars()[4] +
                       basic_model.getVars()[5] +
                       basic_model.getVars()[6] + 
                       basic_model.getVars()[0] )  >= 13 , name = "employees coming on Tuesday" )

"""fourth constraint """
basic_model.addConstr((basic_model.getVars()[4] +
                       basic_model.getVars()[5] + 
                       basic_model.getVars()[6] + 
                       basic_model.getVars()[0] +
                       basic_model.getVars()[1]) >= 14 , name = "employees coming on Wensday" )


"""fifth constraint """
basic_model.addConstr((basic_model.getVars()[0] +
                       basic_model.getVars()[1] + 
                       basic_model.getVars()[2] + 
                       basic_model.getVars()[5] +
                       basic_model.getVars()[6]) >= 15 , name = "employees coming on Thursday" )

"""Sixth constraint """
basic_model.addConstr((basic_model.getVars()[6] +
                       basic_model.getVars()[0] + 
                       basic_model.getVars()[1] + 
                       basic_model.getVars()[2] +
                       basic_model.getVars()[3]) >= 18 , name = "employees coming on Friday" )

"""Seventh constraint """
basic_model.addConstr((basic_model.getVars()[0] +
                       basic_model.getVars()[1] + 
                       basic_model.getVars()[2] + 
                       basic_model.getVars()[3] +
                       basic_model.getVars()[4]) >= 24 , name = "employees coming on Saturday" )






"""Second constraint equality constraints"""
basic_model.addConstrs(x >=0  for x in basic_model.getVars())

"""writting the linear programming to understand what we have written is right or wrong """
basic_model.write("Week_3_Prac.lp")


"""optmizing the problem"""
basic_model.optimize()

"""writting the solution file"""
basic_model.write("Week_3_Prac.sol")

for v in basic_model.getVars():
    print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % basic_model.ObjVal)

