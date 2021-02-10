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