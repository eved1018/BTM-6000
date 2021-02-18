import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem
import nhanes
from nhanes.load import load_NHANES_data, load_NHANES_metadata

def hist_plot(X,col_name,path):
    hist = X.hist(column=col_name, edgecolor='black',color="gray")
    plt.xlabel("{}".format(col_name))
    plt.ylabel("Frequency")
    plt.title("{} distribution".format(col_name))
    plt.tight_layout
    plt.style.use('fivethirtyeight')
    min = X[col_name].min()
    max = X[col_name].max()
    plt.xlim([min, max])
    if path is False:
        return plt
    else:
        plt.savefig(path)
        plt.clf()

def dbinom(x,size,prob):
    result=binom.pmf(k=x,n=size,p=prob,loc=0)
    return result

def pbinom(q,size,prob):
    result=binom.cdf(k=q,n=size,p=prob,loc=0)
    return result

def CLT_stats(df,col):
    mean = df[col].mean()
    median =df[col].median()
    mode =df[col].mode()[0]
    stdev = df[col].std()
    print("mean: {} \nmedian: {} \nmode: {} \nSTDEV: {}\n".format(mean,median,mode,stdev))
    

def Strata(df, col):
    Q4 = df[col].min()
    Q3 = df[col].quantile(0.25)
    Q2 = df[col].quantile(0.5)
    Q1 = df[col].quantile(0.75)
    Q1I = df[df[col] > Q1]
    Q2I = df[(df[col] > Q2) & (df[col] < Q1)]
    Q3I = df[(df[col] > Q3) & (df[col] < Q2)]
    Q4I = df[(df[col] > Q4) & (df[col] < Q3)]

    frames = {
        "Q1 Interval" : Q1I,
        "Q2 Interval" : Q2I,
        "Q3 Interval" : Q3I,
        "Q4 Interval": Q4I
    }
    for i in frames:
        print("{} observations:".format(i),len(frames[i]) )
        mean = frames[i][col].mean()
        print("{} mean:{}".format(i, mean))