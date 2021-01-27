import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

arbutnot_data = pd.read_csv("/Users/evanedelstein/Desktop/School/2021/Spring2021/BTM-6000/module2/arbuthnot.csv")
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

# add proportion boys as column 
arbutnot_data['proportion_boys'] = proportion_boys
# plot
arbutnot_data.plot(x="year", y="proportion_boys", kind="line",c="red")
plt.show()



present_data = pd.read_csv("/Users/evanedelstein/Desktop/School/2021/Spring2021/BTM-6000/module2/present.csv")

print(present_data)
# this file contains a three column: years, boys, and girls. 
# The boys and girls column makes up discrete data. 
# The years in this data set range from 1940 to 2002.

girls_data = present_data['girls']
print(girls_data)

boys_data = present_data['boys']
print(boys_data)

children_data = girls_data + boys_data
print(children_data)

ratio = boys_data/girls_data
print(ratio)

proportion = boys_data/children_data
print(proportion)

# make new column with total children born
present_data["children"] = present_data["boys"] + present_data["girls"]
# find the index of the row with maximum births 
max_birth_year = present_data.iloc[present_data["children"].idxmax()] 
# display the year of maximum births
print(max_birth_year["year"])
# 1961

present_data.plot(x='year',y='children', kind='line')
plt.show()