import streamlit as st
from gurobipy import Model, GRB

def optimize(x_coeff, y_coeff, constraint_a, constraint_b, sense, rhs):
    # Create a Gurobi model
    model = Model()

    # Create decision variables
    x = model.addVar(name="X")
    y = model.addVar(name="Y")

    # Set the objective function to maximize X + Y
    model.setObjective(x_coeff * x + y_coeff * y, GRB.MAXIMIZE)

    # Add user-defined constraints
    if sense == "=":
        model.addConstr(x + y == rhs, "constraint")
    elif sense == "<=":
        model.addConstr(x + y <= rhs, "constraint")
    elif sense == ">=":
        model.addConstr(x + y >= rhs, "constraint")

    # Optimize the model
    model.optimize()

    # Get the results
    x_value = x.x
    y_value = y.x
    objective_value = model.objVal

    return x_value, y_value, objective_value

def main():
    st.title("Linear Optimization with Gurobi")

    # User input for coefficients and constraints
    st.sidebar.header("Objective Function Coefficients:")
    x_coeff = st.sidebar.number_input("Coefficient for X", value=1.0)
    y_coeff = st.sidebar.number_input("Coefficient for Y", value=1.0)

    st.sidebar.header("Linear Constraint:")
    constraint_a = st.sidebar.number_input("Coefficient for X in Constraint", value=1.0)
    constraint_b = st.sidebar.number_input("Coefficient for Y in Constraint", value=1.0)
    sense = st.sidebar.selectbox("Constraint Type", ["=", "<=", ">="])
    rhs = st.sidebar.number_input("Right-hand side of Constraint", value=10.0)

    # Optimize button
    if st.sidebar.button("Optimize"):
        x_value, y_value, objective_value = optimize(x_coeff, y_coeff, constraint_a, constraint_b, sense, rhs)

        # Display results
        st.header("Optimization Results:")
        st.write(f"Optimal X Value: {x_value}")
        st.write(f"Optimal Y Value: {y_value}")
        st.write(f"Optimal Objective Value (X + Y): {objective_value}")

if __name__ == "__main__":
    main()
