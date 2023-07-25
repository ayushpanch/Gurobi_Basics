import gurobipy as gp
from gurobipy import GRB

# Create a Gurobi model
basic_model = gp.Model("MyModel")

# Create six decision variables using list comprehension with meaningful names
variable_names = ["C0", "C1", "C2", "C3", "C4", "C5"]
decision_vars = [basic_model.addVar(vtype=GRB.CONTINUOUS, name=name) for name in variable_names]

# Update the model to include the variables
basic_model.update()

# Add the constraint for each decision variable (x_i <= 187500) with a given name
upper_limit = 187500
constraint_names = {i: f"constraint_{i+1}" for i in range(len(variable_names))}
basic_model.addConstrs((x <= upper_limit, constraint_names[i]) for i, x in enumerate(decision_vars))

# Set the objective function (example objective, replace this with your actual objective)
# basic_model.setObjective(gp.quicksum(x for x in decision_vars), GRB.MAXIMIZE)

# Solve the model
basic_model.optimize()

# Check if the model has an optimal solution
if basic_model.status == GRB.OPTIMAL:
    # Print the optimal objective value
    print(f"Objective value = {basic_model.objVal}")

    # Print the names and optimal values of the decision variables
    for i, x in enumerate(decision_vars):
        print(f"{x.varName} ({i}) {x.x}")
else:
    print("No optimal solution found.")
