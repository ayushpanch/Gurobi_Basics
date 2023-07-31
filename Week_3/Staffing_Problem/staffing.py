import gurobipy as gp
from gurobipy import GRB
import pandas
import os 

# Reading the Excel file because now we will solve the same equation via data 
df= pandas.read_csv(r"C:\Users\panch\Desktop\Gurobi\Week_3\Staffing_Problem\staffing_problem.csv")
df.columns=[x.strip() for x in df.columns]
df.shape[0]

Decision_variables_names = df['Day'].tolist()


#first step setting up the first model
basic_model=gp.Model("basic_model")
print(basic_model)  

# Create decision variables with meaningful names using list comprehension
decision_vars = [basic_model.addVar(vtype=GRB.INTEGER, name=individual_decision_variable) for individual_decision_variable in Decision_variables_names]

# second step creating of variables 
basic_model.update()

# third step setting up the objective functions 


 #writting here 
basic_model.setObjective(gp.quicksum(basic_model.getVars()),GRB.MINIMIZE)   

# fourth step to add constraints 
"""first constraint """
basic_model.addConstr((basic_model.getVars()[0] +
                       basic_model.getVars()[3] + 
                       basic_model.getVars()[4] + 
                       basic_model.getVars()[5] +
                       basic_model.getVars()[6]) >= 17 , name = "employees coming on monday" )

"second constraint"
"""Second constraint """
basic_model.addConstr(
                       (basic_model.getVars()[1] + 
                       basic_model.getVars()[4] + 
                       basic_model.getVars()[5] +
                       basic_model.getVars()[6] +basic_model.getVars()[0] ) >= 13 , name = "employees coming on tuesday" )

"""Third constraint """
basic_model.addConstr((basic_model.getVars()[2] +
                       basic_model.getVars()[5] +
                       basic_model.getVars()[6] +
                       basic_model.getVars()[0] + 
                       basic_model.getVars()[1] )  >= 15 , name = "employees coming on wensday" )

"""fourth constraint """
basic_model.addConstr((basic_model.getVars()[3] +
                       basic_model.getVars()[6] + 
                       basic_model.getVars()[0] + 
                       basic_model.getVars()[1] +
                       basic_model.getVars()[2]) >= 19 , name = "employees coming on Thursday" )


"""fifth constraint """
basic_model.addConstr((basic_model.getVars()[4] +
                       basic_model.getVars()[0] + 
                       basic_model.getVars()[1] + 
                       basic_model.getVars()[2] +
                       basic_model.getVars()[3]) >= 14 , name = "employees coming on Friday" )

"""Sixth constraint """
basic_model.addConstr((basic_model.getVars()[5] +
                       basic_model.getVars()[1] + 
                       basic_model.getVars()[2] + 
                       basic_model.getVars()[3] +
                       basic_model.getVars()[4]) >= 16 , name = "employees coming on Saturday" )

"""Seventh constraint """
basic_model.addConstr((basic_model.getVars()[6] +
                       basic_model.getVars()[2] + 
                       basic_model.getVars()[3] + 
                       basic_model.getVars()[4] +
                       basic_model.getVars()[5]) >= 11 , name = "employees coming on Saturday" )






"""Second constraint equality constraints"""
basic_model.addConstrs(x >=0  for x in basic_model.getVars())

"""writting the linear programming to understand what we have written is right or wrong """
basic_model.write("Staffing.lp")


"""optmizing the problem"""
basic_model.optimize()

"""writting the solution file"""
basic_model.write("Staffing.sol")

for v in basic_model.getVars():
    print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % basic_model.ObjVal)

