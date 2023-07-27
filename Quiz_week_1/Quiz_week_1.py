import gurobipy as gp
from gurobipy import GRB
import pandas
import os 

# Reading the Excel file because now we will solve the same equation via data 
df= pandas.read_csv(r"C:\Users\panch\Desktop\Gurobi\Quiz_week_1\quiz_week_1.csv")
df.shape[0]
df['diff'] = 1 - df['Probability_of_Bad_Debt ']

#first step setting up the first model
basic_model=gp.Model("basic_model")
print(basic_model)  


Decision_variable_names = df['Type_of_Loan'].tolist()

# Create decision variables with meaningful names using list comprehension
decision_vars = [basic_model.addVar(vtype=GRB.CONTINUOUS, name=individual_bond_name) for individual_bond_name in Decision_variable_names]

# second step creating of variables 
basic_model.update()

# third step setting up the objective functions 
bad_debts=df['Probability_of_Bad_Debt '].tolist()
Interest_Rate=df['Interrest_Rate'].tolist()

#writting here 
# basic_model.setObjective([(a*b) for a,b in zip(Interest_Rate,basic_model.getVars())]  - \
#                         [(a*b) for a,b in zip(bad_debts,basic_model.getVars())]    ,GRB.MAXIMIZE)   

basic_model.setObjective([(a*b) for a,b in zip(
                                                df['diff'].tolist(),
                                                [(a*b) for a,b in zip(Interest_Rate,basic_model.getVars())])]  - \
                        [(a*b) for a,b in zip(bad_debts,basic_model.getVars())]    ,GRB.MAXIMIZE)   

#part 1 
# part 2  - [(a*b) for a,b in zip(df['diff'].tolist(),[(a*b) for a,b in zip(Interest_Rate,basic_model.getVars())])]


# fourth step to add constraints 
"""first constraint manager can invest upto this 10 million in any bond"""
basic_model.addConstr(gp.quicksum(basic_model.getVars()) <=10 ,"Bank Investment")


"""second constraint criteria Government and Agency bond must be invested atleast 4 millions"""
indexes_of_dec_var=df[df['Type_of_Loan'].isin(["Farm","Commercial"])].index.tolist()
basic_model.addConstr(gp.quicksum([basic_model.getVars()[x] for x in indexes_of_dec_var]) >= 
                      gp.quicksum(basic_model.getVars()) , \
                      "Government and Agency Bond"  )


"""third constraint Home Loan"""
indexes_of_dec_var=df[df['Type_of_Loan'].isin(["Perosnal","Car","Home"])].index.tolist()
basic_model.addConstr(basic_model.getVars()[2]
                      >=.4*gp.quicksum([basic_model.getVars()[x] for x in indexes_of_dec_var]),"Home Loans")

"""fourth constraint Bad Debts"""
bad_debts=df['Probability_of_Bad_Debt '].tolist()
basic_model.addConstr(gp.quicksum((a*b) for a,b in zip(bad_debts,basic_model.getVars()))\
                      <=.04*(gp.quicksum(basic_model.getVars())),"Years of maturity")

"""fifth constraint equality constraints"""
basic_model.addConstrs(x >=0  for x in basic_model.getVars())

"""writting the linear programming to understand what we have written is right or wrong """
basic_model.write("Quiz_prob.lp")


"""optmizing the problem"""
basic_model.optimize()

"""writting the solution file"""
basic_model.write("Quiz_prob.sol")

for v in basic_model.getVars():
    print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % basic_model.ObjVal)

