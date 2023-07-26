import gurobipy as gp
from gurobipy import GRB


#first step setting up the first model
basic_model=gp.Model("basic_model")
print(basic_model)  


Decision_variable_names = ["A", "B", "C", "D","E"]

# Create decision variables with meaningful names using list comprehension
decision_vars = [basic_model.addVar(vtype=GRB.CONTINUOUS, name=individual_bond_name) for individual_bond_name in Decision_variable_names]

# second step creating of variables 
basic_model.update()

# third step setting up the objective functions 
tax_yield_return =[0.043,.027,.025,.022,.045]
basic_model.setObjective(gp.quicksum((a*b) for a,b in zip(tax_yield_return,basic_model.getVars())),GRB.MAXIMIZE)   

# fourth step to add constraints 
"""first constraint manager can invest upto this 10 million in any bond"""
basic_model.addConstr(gp.quicksum(basic_model.getVars()) <=10 ,"initial investment")


"""second constraint criteria Government and Agency bond must be invested atleast 4 millions"""
basic_model.addConstr(basic_model.getVars()[1]  +basic_model.getVars()[2] + basic_model.getVars()[3] >= 4, \
                      "Government and Agency Bond"  )

"""third constraint Avg quality of Portfolio """
basic_model.addConstr( (2*basic_model.getVars()[0] +
                       2*basic_model.getVars()[1] +
                       1*basic_model.getVars()[2] +
                       1*basic_model.getVars()[3] + 
                       5*basic_model.getVars()[4]) 
                        <=1.4*(gp.quicksum(basic_model.getVars())),"Avg Quality of Portfolio")

"""fourth constraint years of maturity"""
basic_model.addConstr((9*basic_model.getVars()[0] +
                       15*basic_model.getVars()[1] +
                       4*basic_model.getVars()[2] +
                       3*basic_model.getVars()[3] + 
                       2*basic_model.getVars()[4]) 
                        <=5*(gp.quicksum(basic_model.getVars())),"Years of maturity"  )


"""fifth constraint equality constraints"""
basic_model.addConstrs(x >=0  for x in basic_model.getVars())

"""writting the linear programming to understand what we have written is right or wrong """
basic_model.write("prac_prob_week_1_advanced.lp")


"""optmizing the problem"""
basic_model.optimize()

"""writting the solution file"""
basic_model.write("prac_prob_week_1_advanced.sol")

for v in basic_model.getVars():
    print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % basic_model.ObjVal)

