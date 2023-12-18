import pandas as pd
import warnings
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.compose import make_column_transformer
import gurobipy_pandas as gppd
from gurobi_ml import add_predictor_constr
import gurobipy as gp

# import sysprint(sys.executable)
# print(sys.version)
# print(sys.version_info)

avocado = pd.read_csv("HAB_data_2015to2022.csv")
avocado["date"] = pd.to_datetime(avocado["date"])
avocado = avocado.sort_values(by="date")
avocado

regions = [
    "Great_Lakes",
    "Midsouth",
    "Northeast",
    "Northern_New_England",
    "SouthCentral",
    "Southeast",
    "West",
    "Plains"
]
df = avocado[(avocado.region.isin(regions))] # & (avocado.peak==0)
df.drop(columns=['date']) #,'peak'

# plt.figure(figsize=(10, 6))
# r_plt = sns.scatterplot(data=df, x='price', y='units_sold', hue='region')
# r_plt.legend(fontsize=8)
# plt.show()


X = df[["region", "price", "year", "peak"]]
y = df["units_sold"]
# Split the data for training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.7, random_state=1
)



feat_transform = make_column_transformer(
    (OneHotEncoder(drop="first"), ["region"]),
    (StandardScaler(), ["price", "year"]),
    ("passthrough", ["peak"]),
    verbose_feature_names_out=False,
    remainder='drop'
)

reg = make_pipeline(feat_transform, LinearRegression())
scores = cross_val_score(reg, X_train, y_train, cv=5)
print("%0.4f R^2 with a standard deviation of %0.4f" % (scores.mean(), scores.std()))

reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)
print(f"The R^2 value in the test set is {np.round(r2_score(y_test, y_pred),5)}")

reg.fit(X, y)
y_pred_full = reg.predict(X)
print(f"The R^2 value in the full dataset is {np.round(r2_score(y, y_pred_full),5)}")

X.shape[0]
y.shape[0]
accuracy_report= X.copy()
accuracy_report['actual_units_sold'] = y
accuracy_report['Predicted_units_sold'] = y_pred_full

# Sets and parameters
year = 2022
B = 30  # total amount of avocado supply
peak_or_not = 0  # 1 if it is the peak season; 0 if isn't
c_waste = 0.1  # the cost ($) of wasting an avocado
# the cost of transporting an avocado
c_transport = pd.Series(
    {
        "Great_Lakes": 0.3,
        "Midsouth": 0.1,
        "Northeast": 0.4,
        "Northern_New_England": 0.5,
        "SouthCentral": 0.3,
        "Southeast": 0.2,
        "West": 0.2,
        "Plains": 0.2,
    }, name='transport_cost'
)
c_transport = c_transport.loc[regions]

a_min = 0  # minimum avocado price
a_max = 2  # maximum avocado price

# Get the lower and upper bounds from the dataset for the price and the number of products to be stocked
data = pd.concat([c_transport,
                  df.groupby("region")["units_sold"].min().rename('min_delivery'),# min delivery means minimum avacodes can be sold
                  df.groupby("region")["units_sold"].max().rename('max_delivery'), # max delivery means maximum avacodes can be sold
                  df.groupby("region")["price"].max().rename('max_price'),], axis=1)

data

feats = pd.DataFrame(
    data={
        "year": year,
        "peak": peak_or_not,
        "region": regions,
    },
    index=regions
)
feats


"""Creating and initiating model"""
m = gp.Model("Avocado_Price_Allocation")

"""Setting up the Decision variables"""

p = gppd.add_vars(m, data, name="price", lb=a_min, ub=a_max) # price of an avocado for each region
x = gppd.add_vars(m, data, name="supplied_avacadoes_each_region", lb='min_delivery', ub='max_delivery') # number of avocados supplied to each reagion
s = gppd.add_vars(m, data, name="predicted_avacadoes_sold_each_region") # predicted amount of sales in each region for the given price
w = gppd.add_vars(m, data, name="predicted_avacadoes_wasted_each_region") # excess wasteage in each region
d = gppd.add_vars(m, data, lb=-gp.GRB.INFINITY, name="demand") # Add variables for the regression
# demand here means predicted units * price

"""checking the linear programm solution"""



"""setting up the constraints"""
"""first constraint"""
m.addConstr(x.sum() == B)
""" total avacodes supplied  in each region is given by input parameter"""
m.update()
""" avacodes sold in each region should be less than avacodes supplied   """
gppd.add_constrs(m, s, gp.GRB.LESS_EQUAL, x)
""" avacodes sold predicted should be less than demand"""
gppd.add_constrs(m, s, gp.GRB.LESS_EQUAL, d)
m.update()

gppd.add_constrs(m, w, gp.GRB.EQUAL, x - s)
m.update()
m.write("solution.lp")

m_feats = pd.concat([feats, p], axis=1)[["region", "price", "year", "peak"]]
m_feats
""" gp_model, predictor, input_vars, output_vars=None
in the below function please find here 
m - stands for model 
reg - stands for predictor dont know basically what it meants
m_feats - stands for input features
d - demand decision variable which will be output variable

"""
pred_constr = add_predictor_constr(m, reg, m_feats, d)
pred_constr.print_stats()

""" writting the objective function """
m.setObjective((p * s).sum() - c_waste * w.sum() - (c_transport * x).sum(),
               gp.GRB.MAXIMIZE)

"""
In our model, the objective is quadratic since we take the product of price and the predicted sales,
 both of which are variables. Maximizing a quadratic term is said to be non-convex,
   and we specify this by setting the value of the Gurobi NonConvex parameter to be  2 .

"""
m.Params.NonConvex = 2
m.optimize()

"""writting the solution file"""
m.write("solution.sol")

solution = pd.DataFrame(index=regions)

solution["Price"] = p.gppd.X
solution["Allocated"] = x.gppd.X
solution["Sold"] = s.gppd.X
solution["Wasted"] = w.gppd.X
solution["Pred_demand"] = d.gppd.X

opt_revenue = m.ObjVal
print("\n The optimal net revenue: $%f million" % opt_revenue)
solution.round(4)


m

