import gurobipy as gp
from gurobipy import GRB
import pandas
import os 

# Reading the Excel file because now we will solve the same equation via data 
df= pandas.read_csv(r"C:\Users\panch\Desktop\Gurobi\Week_4\Week_4_quiz\Electronics_problems.csv")
df.columns=[x.strip() for x in df.columns]
df.shape[0]

Decision_variables_names = ['A','B','C1','C2','X1A','X2A','X1B','X2B']


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
basic_model.setObjective(6*basic_model.getVars()[0] +5*basic_model.getVars()[1] \
                         -6*basic_model.getVars()[2]-4*basic_model.getVars()[3],GRB.MAXIMIZE)   

# fourth step to add constraints 
"""first constraint """

basic_model.addConstr( basic_model.getVars()[0]== basic_model.getVars()[4] +basic_model.getVars()[5], name = "Drug 1 Creation" )

basic_model.addConstr( basic_model.getVars()[1]== basic_model.getVars()[6] +basic_model.getVars()[7], name = "Drug 2 Creation" )

basic_model.addConstr( basic_model.getVars()[4] +basic_model.getVars()[6]
                       <=basic_model.getVars()[2] , name = "Chemical 1 usage" )

basic_model.addConstr( basic_model.getVars()[5] +basic_model.getVars()[7]
                       <=basic_model.getVars()[3] , name = "Chemical 2 usage" )

basic_model.addConstr( basic_model.getVars()[4]
                       >= 0.7*basic_model.getVars()[0] , name = "Drug_A_70_percent_chemical_A" )

basic_model.addConstr( basic_model.getVars()[7]
                       >= 0.6*basic_model.getVars()[1] , name = "Drug_A_70_percent_chemical_B" )

basic_model.addConstr( basic_model.getVars()[0]
                       <= 40 , name = "Drug A Req" )

basic_model.addConstr( basic_model.getVars()[1]
                       <= 30 , name = "Drug B Req" )


basic_model.addConstr( basic_model.getVars()[2]
                       <= 45 , name = "Chemical A Purchased" )

basic_model.addConstr( basic_model.getVars()[3]
                       <= 40 , name = "Chemical B Purchased" )

"""writting the linear programming to understand what we have written is right or wrong """
basic_model.write("Pharmacetical_company.lp")


"""optmizing the problem"""
basic_model.optimize()

"""writting the solution file"""
basic_model.write("Pharmacetical_company.sol")

for v in basic_model.getVars():
    print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % basic_model.ObjVal)

