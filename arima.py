import pandas as pd
import chart_studio.plotly as ply
import cufflinks as cf
import matplotlib.pyplot as plt
import numpy as np
from chart_studio.plotly import plot_mpl
from statsmodels.tsa.seasonal import seasonal_decompose

#from plotly.offline import download_plotlyjs, init_notebook_mode, plot,iplot
#init_notebook_mode(connected=True)


data = pd.read_csv("2020-02-09_Slussen_3.txt", index_col=0)
data.index = pd.to_datetime(data.index)

data.iplot(title="Slussen 3 20-02-09")
da1 = data.values
#da1 = da1.transpose()
plt.plot(data.index, da1)

result = seasonal_decompose(data, model="multiplicative")
fig = result.plot()
plot_mpl(fig)
#tsaplots.plot_acf(data.value)