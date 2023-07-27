import gurobipy as gp
from gurobipy import GRB
import pandas
import os 

# Reading the Excel file because now we will solve the same equation via data 
df= pandas.read_csv(r"C:\Users\panch\Desktop\Gurobi\Practice_Problem_week_1_Excel\prob.csv")
df.shape[0]


#first step setting up the first model
basic_model=gp.Model("basic_model")
print(basic_model)  


Decision_variable_names = df['Bond_Name'].tolist()

# Create decision variables with meaningful names using list comprehension
decision_vars = [basic_model.addVar(vtype=GRB.CONTINUOUS, name=individual_bond_name) for individual_bond_name in Decision_variable_names]

# second step creating of variables 
basic_model.update()

# third step setting up the objective functions 
tax_yield_return =df['Tax_Yield'].tolist()
basic_model.setObjective(gp.quicksum((a*b) for a,b in zip(tax_yield_return,basic_model.getVars())),GRB.MAXIMIZE)   

# fourth step to add constraints 
"""first constraint manager can invest upto this 10 million in any bond"""
basic_model.addConstr(gp.quicksum(basic_model.getVars()) <=10 ,"initial investment")


"""second constraint criteria Government and Agency bond must be invested atleast 4 millions"""
indexes_of_dec_var=df[df['Bond_Type'].isin(["Agency","Government"])].index.tolist()
basic_model.addConstr(gp.quicksum([basic_model.getVars()[x] for x in indexes_of_dec_var]) >= 4, \
                      "Government and Agency Bond"  )


"""third constraint Avg quality of Portfolio """
Quality_scale_bank = df['Quality_Scale_Bank'].tolist()
basic_model.addConstr(gp.quicksum((a*b) for a,b in zip(Quality_scale_bank,basic_model.getVars()))\
                      <=1.4*(gp.quicksum(basic_model.getVars())),"Avg Quality of Portfolio")

"""fourth constraint years of maturity"""
Years_maturity=df['Years_Maturity'].tolist()
basic_model.addConstr(gp.quicksum((a*b) for a,b in zip(Years_maturity,basic_model.getVars()))\
                      <=5*(gp.quicksum(basic_model.getVars())),"Years of maturity")

"""fifth constraint equality constraints"""
basic_model.addConstrs(x >=0  for x in basic_model.getVars())

"""writting the linear programming to understand what we have written is right or wrong """
basic_model.write("Solving_Excel.lp")


"""optmizing the problem"""
basic_model.optimize()

"""writting the solution file"""
basic_model.write("Solving_Excel.sol")

for v in basic_model.getVars():
    print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % basic_model.ObjVal)

