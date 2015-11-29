import numpy as np
import scipy as sc
import scipy.stats as st
import pandas as pd

def mann_whitney_u_test(dF):
  nRain = dF['ENTRIESn_hourly'][dF['rain'] == 0] #No Rain
  yRain = dF['ENTRIESn_hourly'][dF['rain'] == 1] # Rain

  meanNR = np.mean(nRain)
  meanYR = np.mean(yRain)
    

  U, p = st.mannwhitneyu(yRain.tolist(), nRain.tolist())
  return meanYR, meanNR, U, p

path = r'../dataSet/turnstile_weather_v2.csv'
dF = pd.read_csv(path)

meanYR, meanNR, U, p = mann_whitney_u_test(dF)
print "the mean of data set with raining: ", meanYR
print "the mean of data set without raining: ", meanNR
print "the Mann Whitney U test is ", U
print "the p-value is ", p
