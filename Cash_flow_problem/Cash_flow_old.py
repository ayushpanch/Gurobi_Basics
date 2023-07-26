import gurobipy as gp
from gurobipy import GRB

""" in this we will read the excel and we will try to formulate according to Excel not manually writting it """

#first step setting up the first model
basic_model=gp.Model("basic_model")
print(basic_model)  

# second step creating of variables 


decision_variables= basic_model.addVars([x for x in range(9)],vtype =GRB.CONTINUOUS,name ="Decision Variables")
basic_model.update()

#objective functions
basic_model.setObjective(basic_model.getVars()[1] + 1.9*basic_model.getVars()[3] +\
                          1.5*basic_model.getVars()[4] + 1.08*basic_model.getVars()[7]
                        ,GRB.MAXIMIZE)




# fourth step Add constraints 
"""first constraint"""
basic_model.addConstr(basic_model.getVars()[0] + \
                      basic_model.getVars()[2] +\
                      basic_model.getVars()[4] + basic_model.getVars()[5]   == 100000,"initial investment")


"""second constraint"""
basic_model.write("cashflow_ip.lp")
basic_model.addConstrs(x <=75000  for x in basic_model.getVars())

"""third constraint"""
basic_model.addConstr(0.5 * (basic_model.getVars()[0]) + 1.2*(basic_model.getVars()[2]) + 1.08*basic_model.getVars()[5]   
                            ==  basic_model.getVars()[1],"Long Investment")

"""fourth constraint"""
# basic_model.addConstr(X2 +X3  +X5  <= 262500,"High Risk Investment")
basic_model.addConstr(((basic_model.getVars()[0] + basic_model.getVars()[0]*.5) + 
                      (basic_model.getVars()[1] + basic_model.getVars()[1]*.5)) + 
                      
                      0.8*(((basic_model.getVars()[0] + basic_model.getVars()[0]*.5) + 
                      (basic_model.getVars()[1] + basic_model.getVars()[1]*.5)))
                        == basic_model.getVars()[4],"High Risk Investment")


# write the linear programming equation
basic_model.write('cash_flow.lp')

# optimise the solution
basic_model.optimize()

# write the solution to .sol file
basic_model.write("Cash_flow.sol")


basic_model
for v in basic_model.getVars():
    print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % basic_model.ObjVal)
