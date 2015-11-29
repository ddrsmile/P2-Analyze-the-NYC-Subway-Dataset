import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plotHistRain(dF):
  plt.figure()
  nRain = dF['ENTRIESn_hourly'][dF['rain'] == 0].values #not raining
  yRain = dF['ENTRIESn_hourly'][dF['rain'] == 1].values #raining

  plt.hist(nRain, bins=100, label='non rainy days')
  plt.hist(yRain, bins=100, label='rainy days')
  plt.legend(loc='upper right')
  plt.axis([0, 10000, 0, 10000])
  plt.title('Histogram of ENTRIESn_hourly')
  plt.xlabel('ENTRIESn_hourly [-]')
  plt.ylabel('Frequency [-]')
  plt.show()

path = r'../dataSet/turnstile_weather_v2.csv'
dF = pd.read_csv(path)
plotHistRain(dF)
