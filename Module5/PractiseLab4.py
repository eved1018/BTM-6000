# import pandas as pd 
import random
import sys
sys.path.insert(0, '/Users/evanedelstein/Desktop/School/2021/Spring2021/BTM-6000/Mods')
from Biostats import *


# def CT_stats(df,col):
#     mean = df[col].mean()
#     median =df[col].median()
#     mode =df[col].mode()[0]
#     print("mean: {} \nmedian: {} \nmode: {} \n".format(mean,median,mode))


# load and view data set
ames_data = pd.read_csv("http://www.openintro.org/stat/data/ames.csv")
# print(ames_data)
# mean,median and mode lot area
print("total")
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

print("mean distribution",np.mean(means))

plt.hist(means,edgecolor='black',color="gray")
plt.tight_layout
plt.style.use('fivethirtyeight')
plt.xlabel("mean")
plt.ylabel("freq")
plt.show()