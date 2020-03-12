from statsmodels.tsa.stattools import adfuller
from numpy import log
import pandas as pd

data = pd.read_csv("2020-02-09_Slussen_3.txt", index_col=0)
data.index = pd.to_datetime(data.index)
result = adfuller(data.value.dropna())
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])