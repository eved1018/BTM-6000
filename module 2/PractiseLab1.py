import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

arbutnot_data = pd.read_csv("/Users/evanedelstein/Desktop/School/2021/Spring2021/BTM-6000/module 2/arbuthnot.csv")
cdc_data = pd.read_csv("/Users/evanedelstein/Desktop/School/2021/Spring2021/BTM-6000/module 2/cdc.csv")
arbutnot_data.columns.values[0] = 'X'
girls_data = arbutnot_data["girls"]
print(girls_data)

boys_data = arbutnot_data[["X","year","boys"]]
print(boys_data)

girls_data_2 = arbutnot_data[["X","year","girls"]]
print(girls_data_2)

children_data = arbutnot_data["boys"] + arbutnot_data["girls"]

ratio = arbutnot_data["boys"]/arbutnot_data["girls"]
print(ratio)

proportion_boys = arbutnot_data["boys"]/(arbutnot_data["girls"]+ arbutnot_data["boys"])
print(proportion_boys)

arbutnot_data['proportion_boys'] = proportion_boys

arbutnot_data.plot(x="year", y="proportion_boys", kind="line",c="red")
plt.show()


