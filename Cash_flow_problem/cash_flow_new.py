import gurobipy as gp
from gurobipy import GRB


#first step setting up the first model
basic_model=gp.Model("basic_model")
print(basic_model)  

# second step creating of variables 
decision_variables= basic_model.addVars([x for x in range(8)],vtype =GRB.CONTINUOUS,name ="Decision Variables")
basic_model.update()

# third step setting up the objective functions 
basic_model.setObjective(basic_model.getVars()[1] + 
                         1.9*basic_model.getVars()[3] +
                           1.5*basic_model.getVars()[4] +
                             1.08*basic_model.getVars()[7],GRB.MAXIMIZE )   
basic_model.write('test.lp')

# fourth step to add constraints 
"""first constraint at year 0"""
basic_model.addConstr(basic_model.getVars()[0] + \
                      basic_model.getVars()[2] +\
                      basic_model.getVars()[3] + basic_model.getVars()[5]   == 100000,"initial investment")


"""second constraint criteria that not more than 75 k can be invested in any portfolios since there are 5 portfolios hence """
basic_model.addConstr(basic_model.getVars()[0] <=75000,"criteria DV0"  )
basic_model.addConstr(basic_model.getVars()[1] <=75000,"criteria DV1"  )
basic_model.addConstr(basic_model.getVars()[2] <=75000,"criteria DV2"  )
basic_model.addConstr(basic_model.getVars()[3] <=75000,"criteria DV3"  )
basic_model.addConstr(basic_model.getVars()[4] <=75000,"criteria DV4"  )


"""third constraint at year 1 """
basic_model.addConstr(0.5*basic_model.getVars()[0] + \
                      1.2*basic_model.getVars()[2] +\
                      1.08*basic_model.getVars()[5]   == basic_model.getVars()[1] + basic_model.getVars()[6] ,"at year 1 ")

"""fourth constraint at year 2"""
basic_model.addConstr(basic_model.getVars()[0] + 
                      0.5*basic_model.getVars()[1] + 
                      1.08*basic_model.getVars()[6] 
                      == basic_model.getVars()[4] + basic_model.getVars()[7],"at year 2"  )


"""fifth constraint equality constraints"""
basic_model.addConstrs(x >=0  for x in basic_model.getVars())

"""writting the linear programming to understand what we have written is right or wrong """
basic_model.write("cash_flow_part2.lp")


"""optmizing the problem"""
basic_model.optimize()

"""writting the solution file"""
basic_model.write("cash_flow_part2.sol")

for v in basic_model.getVars():
    print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % basic_model.ObjVal)

