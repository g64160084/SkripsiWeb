# Python
import pandas as pd
import numpy as np
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
import plotly.offline as py
import rasterio
from rasterio import plot

#df = pd.read_csv(r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\example.csv")
df = pd.read_csv(r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\Book1.csv")

print(df)
m = Prophet()
m.fit(df)
future = m.make_future_dataframe(periods=2,freq = 'M')
future.tail()

forecast = m.predict(future)
list(forecast.columns)

forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
fig1 = m.plot(forecast)
fig2 = m.plot_components(forecast)

forecast.to_csv('C:/Users/DELL/Documents/SKRIPSI/PYCHARM/Code/test.csv')

py.init_notebook_mode()
fig = plot_plotly(m, forecast)  # This returns a plotly Figure
py.iplot(fig)



