import gurobipy as gp
from gurobipy import GRB
import pandas
import os 

# Reading the Excel file because now we will solve the same equation via data 
df= pandas.read_csv(r"C:\Users\panch\Desktop\Gurobi\Week_3\Office_assignment\offc.csv")
df.shape[0]



#first step setting up the first model
basic_model=gp.Model("basic_model")
print(basic_model)  

Staff= df['Staff'].tolist()
Rooms=df.columns[1:].tolist()

Decision_variables_names = []
for x in Staff:
    for y in Rooms:
        Decision_variables_names.append(x+"_"+y)
Decision_variables_names = [x.strip() for x in Decision_variables_names ]


# Create decision variables with meaningful names using list comprehension
decision_vars = [basic_model.addVar(vtype=GRB.BINARY, name=individual_decision_variable) for individual_decision_variable in Decision_variables_names]

# second step creating of variables 
basic_model.update()

# third step setting up the objective functions 

dummy_df = df.iloc[:,1:]
numeric_values_list = dummy_df.apply(lambda row: row.tolist(), axis=1).tolist()
weights =[]
for x in numeric_values_list:
    for y in x:
        weights.append(y)

 #writting here 
basic_model.setObjective(gp.quicksum((a*b) for a,b in zip(weights,basic_model.getVars())),GRB.MAXIMIZE)   

# fourth step to add constraints 
"""first constraint """
constraint=[x for x in Decision_variables_names if x.endswith("Room_1")]
positions = [Decision_variables_names.index(every_decision_name) for every_decision_name in constraint]
# basic_model.addConstr(x >=0  for x in basic_model.getVars() ,"Room_1_2_staff_each")
for every_positions in positions:
    basic_model.addConstr(basic_model.getVars()[every_positions] == 2)

# basic_model.write("dummy.lp")


"""second constraint """
constraint=[x for x in Decision_variables_names if x.endswith("Room_2")]
positions = [Decision_variables_names.index(every_decision_name) for every_decision_name in constraint]
# basic_model.addConstr(gp.quicksum([basic_model.getVars()[x] for x in positions]) == 2 ,"Room_2_2_staff_each")
for every_positions in positions:
    basic_model.addConstr(basic_model.getVars()[every_positions] == 2)


"""third constraint"""
constraint=[x for x in Decision_variables_names if x.endswith("Room_3")]
positions = [Decision_variables_names.index(every_decision_name) for every_decision_name in constraint]
# basic_model.addConstr(gp.quicksum([basic_model.getVars()[x] for x in positions]) == 2 ,"Room_3_2_staff_each")
for every_positions in positions:
    basic_model.addConstr(basic_model.getVars()[every_positions] == 2)

"""fourth constraint """
constraint=[x for x in Decision_variables_names if x.endswith("Room_4")]
positions = [Decision_variables_names.index(every_decision_name) for every_decision_name in constraint]
# basic_model.addConstr(gp.quicksum([basic_model.getVars()[x] for x in positions]) == 1 ,"Room_4_1_staff_each")
for every_positions in positions:
    basic_model.addConstr(basic_model.getVars()[every_positions] == 1)



"""fifth constraint """
constraint=[x for x in Decision_variables_names if x.startswith("Room_5")]
positions = [Decision_variables_names.index(every_decision_name) for every_decision_name in constraint]
# basic_model.addConstr(gp.quicksum([basic_model.getVars()[x] for x in positions]) ==400000 ,"Scottsdale Manufacturing plant")
for every_positions in positions:
    basic_model.addConstr(basic_model.getVars()[every_positions] == 1)


# """Sixth constraint """
# constraint=[x for x in Decision_variables_names if x.startswith("Tuscon")]
# positions = [Decision_variables_names.index(every_decision_name) for every_decision_name in constraint]
# basic_model.addConstr(gp.quicksum([basic_model.getVars()[x] for x in positions]) ==300000 ,"Tuscon Manufacturing plant")

# """seventh constraint equality constraints"""
# basic_model.addConstrs(x >=0  for x in basic_model.getVars())

"""writting the linear programming to understand what we have written is right or wrong """
basic_model.write("office_assignment.lp")


"""optmizing the problem"""
basic_model.optimize()

"""writting the solution file"""
basic_model.write("office_assignment.sol")

for v in basic_model.getVars():
    print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % basic_model.ObjVal)

