import numpy as np
import pandas as pd
import statsmodels.api as sm
import scipy as sc
import matplotlib.pyplot as plt

def linear_regression(features, values):
  """
  Perform linear regression with statsmodels module
  """
  features = sm.add_constant(features)
  model = sm.OLS(values, features)
  results = model.fit()
  intercept = results.params[0]
  params = results.params[1:]
  return intercept, params

def predictions(dF):
  #Features
  features = dF[['rain', 'precipi', 'hour', 'meantempi']]
  dummy_units = pd.get_dummies(dF['UNIT'], prefix='unit')
  features = features.join(dummy_units)

  #Values
  values = dF['ENTRIESn_hourly']

  #Perform linear regression
  intercept, params = linear_regression(features, values)
  predictions = intercept + np.dot(features, params)
  return predictions

def compute_r_squared(data, predictions):
  a = ((data - predictions)**2).sum()
  b = ((data - np.mean(data))**2).sum()
  rsquared = 1 - a/b
  return rsquared

def plotHist(dF, predictions):
  plt.figure()
  (dF['ENTRIESn_hourly'] - predictions).hist()
  plt.show()


path = r'../dataSet/turnstile_weather_v2.csv'
dF = pd.read_csv(path)

predict = predictions(dF)
rsquared = compute_r_squared(dF['ENTRIESn_hourly'], predict)
print rsquared
plotHist(dF, predict)

