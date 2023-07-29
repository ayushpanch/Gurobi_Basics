import gurobipy as gp
from gurobipy import GRB
import pandas
import os 

# Reading the Excel file because now we will solve the same equation via data 
df= pandas.read_csv(r"C:\Users\panch\Desktop\Gurobi\Week_2_Practice_Problem\Army_transportation_problem.csv")
df.shape[0]



#first step setting up the first model
basic_model=gp.Model("basic_model")
print(basic_model)  

Army_camps= df['Army_camps'].tolist()
Base_camp=df.columns[1:].tolist()

Decision_variables_names = []
for x in Army_camps:
    for y in Base_camp:
        Decision_variables_names.append(x+"_"+y)
Decision_variables_names = [x.strip() for x in Decision_variables_names ]


# Create decision variables with meaningful names using list comprehension
decision_vars = [basic_model.addVar(vtype=GRB.CONTINUOUS, name=individual_decision_variable) for individual_decision_variable in Decision_variables_names]

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
basic_model.setObjective(gp.quicksum((a*b) for a,b in zip(weights,basic_model.getVars())),GRB.MINIMIZE)   

# fourth step to add constraints 
"""first constraint """
constraint=[x for x in Decision_variables_names if x.endswith("Base_1")]
positions = [Decision_variables_names.index(every_decision_name) for every_decision_name in constraint]
basic_model.addConstr(gp.quicksum([basic_model.getVars()[x] for x in positions]) ==200 ,"Camp_Base_1_requirement")


"""second constraint """
constraint=[x for x in Decision_variables_names if x.endswith("Base_2")]
positions = [Decision_variables_names.index(every_decision_name) for every_decision_name in constraint]
basic_model.addConstr(gp.quicksum([basic_model.getVars()[x] for x in positions]) ==250 ,"Camp_Base_2_requirement")


"""third constraint"""
constraint=[x for x in Decision_variables_names if x.endswith("Base_3")]
positions = [Decision_variables_names.index(every_decision_name) for every_decision_name in constraint]
basic_model.addConstr(gp.quicksum([basic_model.getVars()[x] for x in positions]) ==350 ,"Camp_Base_3_requirement")

"""fouth constraint"""
constraint=[x for x in Decision_variables_names if x.endswith("Base_4")]
positions = [Decision_variables_names.index(every_decision_name) for every_decision_name in constraint]
basic_model.addConstr(gp.quicksum([basic_model.getVars()[x] for x in positions]) ==300 ,"Camp_Base_4_requirement")



"""fifth constraint """
constraint=[x for x in Decision_variables_names if x.startswith("Camp_1")]
positions = [Decision_variables_names.index(every_decision_name) for every_decision_name in constraint]
basic_model.addConstr(gp.quicksum([basic_model.getVars()[x] for x in positions]) <=500 ,"Available Resources camp 1")

"""Sixth constraint """
constraint=[x for x in Decision_variables_names if x.startswith("Camp_2")]
positions = [Decision_variables_names.index(every_decision_name) for every_decision_name in constraint]
basic_model.addConstr(gp.quicksum([basic_model.getVars()[x] for x in positions]) <=400 ,"Available Resources camp 2")

"""Sixth constraint """
constraint=[x for x in Decision_variables_names if x.startswith("Camp_3")]
positions = [Decision_variables_names.index(every_decision_name) for every_decision_name in constraint]
basic_model.addConstr(gp.quicksum([basic_model.getVars()[x] for x in positions]) <=400 ,"Available Resources camp 3")

"""seventh constraint equality constraints"""
basic_model.addConstrs(x >=0  for x in basic_model.getVars())

"""writting the linear programming to understand what we have written is right or wrong """
basic_model.write("Army_transportation.lp")


"""optmizing the problem"""
basic_model.optimize()

"""writting the solution file"""
basic_model.write("Army_transportation.sol")

for v in basic_model.getVars():
    print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % basic_model.ObjVal)

