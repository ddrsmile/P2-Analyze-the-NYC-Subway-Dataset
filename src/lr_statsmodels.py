import numpy as np
import pandas as pd
import statsmodels.api as sm
from dataExtract import getAnalysisData as gad

def linear_regression(features, values):
  """
  Perform linear regression with statsmodels module
  """
  features = sm.add_constant(features)
  model = sm.OLS(values, features)
  results = model.fit()
  
  intercept = results.params[0]
  params = results.params[1:]
  print 'Coefficient of non dummy variable by Ordinary least Squares is ', params[0]
  return intercept, params

def predictions(dF):
  """
  #Features
  features = dF[['rain']]
  dummy_units = pd.get_dummies(dF['UNIT'], prefix='unit')
  dummy_hour = pd.get_dummies(dF['hour'], prefix='hour')
  dummy_daywk = pd.get_dummies(dF['day_week'], prefix='day_week')
  features = features.join(dummy_units).join(dummy_hour).join(dummy_daywk)

  #Values
  values = dF['ENTRIESn_hourly']
  """
  features, values = gad(dF)
  #Perform linear regression
  intercept, params = linear_regression(features, values)
  print len(params)
  predictions = intercept + np.dot(features, params)
  return predictions

