import pandas as pd 
import matplotlib.pyplot as plt

# load data set
cdc_data = pd.read_csv("http://www.openintro.org/stat/data/cdc.csv")
# show first few lines of data set
print(cdc_data)
# this data set contains health information related to 20000 individuals.
# the variables involved in the dataset are:
#  general health, health plan, exercise habbits, smoking habbit, height, weight, desired weight, age and gender
# the exercise, healthplan , smoking habbit and gender are boolean variables
# height, weight and age are 
# 
males = len(cdc_data[cdc_data['gender'] == 'm'])
print("number of males:",males)
# 9569 males
females = len(cdc_data[cdc_data['gender'] == 'f'])
print("number of females:",females)
# 10431 females
older_25 = len(cdc_data[cdc_data['age'] > 25])
print("number older than 25:",older_25)
# 17272 older than 25
older_35 = len(cdc_data[cdc_data['age'] > 35])
print("number older than 35:",older_35)
# 13216 older than 35
# Histogram plot for age 
hist = cdc_data.hist(column="age",grid="False")
plt.show()
# plt.savefig("/Users/evanedelstein/Desktop/School/2021/Spring2021/BTM-6000/module3/age_hist.png")
# plt.clf()
# mean
mean = cdc_data["age"].mean()
print("mean age:", mean)
median = cdc_data["age"].median()
print("median age:", median)
mode = cdc_data["age"].mode()
print("mode age:", mode)