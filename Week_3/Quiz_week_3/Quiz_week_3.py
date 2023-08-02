import gurobipy as gp
from gurobipy import GRB
import pandas
import os 

# Reading the Excel file because now we will solve the same equation via data 
# df= pandas.read_csv(r"C:\Users\panch\Desktop\Gurobi\Week_3\Staffing_Problem\staffing_problem.csv")
# df.columns=[x.strip() for x in df.columns]
# df.shape[0]

Decision_variables_names = ['X0','X1','X2','X3','X4','X5','Y0','Y1','Y2','Y3','Y4','Y5']


#first step setting up the first model
basic_model=gp.Model("basic_model")
print(basic_model)  

# Create decision variables with meaningful names using list comprehension
# decision_vars = [basic_model.addVar(vtype=GRB.CONTINUOUS, name=individual_decision_variable) for individual_decision_variable in Decision_variables_names]
for name in Decision_variables_names:
    locals()[name] = basic_model.addVar(vtype=GRB.CONTINUOUS, name=name)
# second step creating of variables 
basic_model.update()

# third step setting up the objective functions 


 #writting here 
basic_model.setObjective( 
    # first month 
    ((120 + eval('X0') - eval('Y0')) *4  + eval('X0')*5 +eval('Y0')*3) +
    # second month 
    (( eval('X0')  -eval('Y0')  +eval('X1')  -eval('Y1') -90)*4 + eval('X1')*5 + eval('Y1')*3) +
    # third month 
    (( eval('X0')  -eval('Y0')  +eval('X1')  -eval('Y1') + eval('X2') -eval('Y2') -205)*4 + eval('X2')*5 +eval('Y2')*3) +
    # fourth month
    ((eval('X0')  -eval('Y0')  +eval('X1')  -eval('Y1') + eval('X2') -eval('Y2') \
      -345  +eval('X3') -eval('Y3'))*4 + eval('X3')*5 +eval('Y3')*3) +
    # fifth month  
      (( eval('X0')  -eval('Y0')  +eval('X1')  -eval('Y1') + eval('X2') -eval('Y2') +eval('X3') \
        -eval('Y3') +eval('X4') -eval('Y4') -455)*4
        + eval('X4')*4 +eval('Y4')*3) +
    # Sixth month  
      (( eval('X0')  -eval('Y0')  +eval('X1')  -eval('Y1') + eval('X2') -eval('Y2') +eval('X3') \
        -eval('Y3') +eval('X4') -eval('Y4') -655 +eval('X5') -eval('Y5'))*4
        + eval('X5')*5 +eval('Y5')*3)
      ,GRB.MINIMIZE)   


# fourth step to add constraints 
"""first constraint """
 

basic_model.addConstr((120 + eval('X0')  -eval('Y0')) >= 100 , name = "month 1 constraint" )

"second constraint"
"""Second constraint """
basic_model.addConstr((20 + eval('X0')  -eval('Y0')  \
                       +eval('X1')  -eval('Y1')) >=110 , name = "month 2 constraint" )

"""Third constraint """
basic_model.addConstr(( eval('X0')  -eval('Y0')  +eval('X1')  -eval('Y1')\
                        -90 + eval('X2') -eval('Y2'))  >= 115 , name = "month 3 constraint" )

"""fourth constraint """
basic_model.addConstr(( eval('X0')  -eval('Y0')  +eval('X1')  -eval('Y1') + eval('X2') \
                       -eval('Y2') -205 +eval('X3') -eval('Y3')) >= 140 , name = "month 4 constraint" )

"""fifth constraint """
basic_model.addConstr(( eval('X0')  -eval('Y0')  +eval('X1')  -eval('Y1') + eval('X2') -eval('Y2') \
                       -345  +eval('X3') -eval('Y3') +eval('X4') -eval('Y4')) >= 110 , name = "month 5 constraint" )

"""Sixth constraint """
basic_model.addConstr(( eval('X0')  -eval('Y0')  + eval('X1')\
                         -eval('Y1') + eval('X2') -eval('Y2') +eval('X3') -eval('Y3') +eval('X4')\
                              -eval('Y4') -455 +eval('X5') -eval('Y5')) >= 200 , name = "month 6 constraint" )

"""Seventh constraint """
basic_model.addConstrs(x >=0  for x in basic_model.getVars())

"""writting the linear programming to understand what we have written is right or wrong """
basic_model.write("Quiz_week_3.lp")


"""optmizing the problem"""
basic_model.optimize()

"""writting the solution file"""
basic_model.write("Quiz_week_3.lp.sol")

for v in basic_model.getVars():
    print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % basic_model.ObjVal)

