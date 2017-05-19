__author__ = 'Ralph van der Neut'
import pandas as pd
from pandas import DataFrame

boodschappen = pd.read_csv("D:/Code/Blog/MachineLearning/MachineLearning/Data/boodschappen/boodschappen.csv",header=None, prefix="V") #tussen de haken staat locatie van document.
#code print 5 eerste regels
print(boodschappen.head())
#code print 5 laatste regels
print(boodschappen.tail())
summary = boodschappen.describe()
#code print samenvatting eigenschappen 
print(summary)