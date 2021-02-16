# import pandas as pd 
import sys
sys.path.insert(0, '/Users/evanedelstein/Desktop/School/2021/Spring2021/BTM-6000/Mods')
from Biostats import *
import random


# load and view data set
ames_data = pd.read_csv("http://www.openintro.org/stat/data/ames.csv")
# print(ames_data)
# mean,median and mode lot area
print("Lot Area")
CT_stats(ames_data,"Lot.Area")

# random sample of 60 observations 
print("60 samples")
sample_60 = ames_data.sample(n=60)
CT_stats(sample_60,"Lot.Area")

# sample 120
sample_120 = ames_data.sample(n=120)
print("120 samples")
CT_stats(sample_120,"Lot.Area")
rand_list = random.sample(range(1, 2930), 500)
means = []
for i in rand_list:
    sample = ames_data.sample(n=i)
    mean = sample["Lot.Area"].mean()
    means.append(mean)

print("Lot Area mean distribution",np.mean(means),"\n")

plt.hist(means,edgecolor='black',color="gray")
plt.tight_layout
plt.style.use('fivethirtyeight')
plt.xlabel("mean")
plt.ylabel("freq")
# plt.show()

# SalePrice
print("sales price")
mean_total = ames_data["SalePrice"].mean()
print("mean price:",mean_total)
sample_50 = ames_data.sample(n=50)
mean_50  = sample_50["SalePrice"].mean()
print("sample 50 mean:",mean_50)
# rand_list = random.sample(range(1, 2930), 5000)
means = []
for i in range(1,5000):
    rand  = random.randint(1,2930)
    sample = ames_data.sample(n=rand)
    mean = sample["SalePrice"].mean()
    means.append(mean)

print("Price mean distribution",np.mean(means),"\n")

Q1 = ames_data['SalePrice'].quantile(0.25)
Q2 = ames_data['SalePrice'].quantile(0.5)
Q3 = ames_data['SalePrice'].quantile(0.75)
Q1I = ames_data[ames_data["SalePrice"] >= Q1]
mean_Q1I = Q1I["SalePrice"].mean()
Q3I = ames_data[ames_data["SalePrice"] < Q3]
mean_Q3I = Q3I["SalePrice"].mean()
print("total mean: {} \nQ1 mean: {}\nQ3 mean: {}".format(mean_total,mean_Q1I,mean_Q3I))