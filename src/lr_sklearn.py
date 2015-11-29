import numpy as np
import pandas as pd
from sklearn.linear_model import SGDRegressor as sg
from dataExtract import getAnalysisData as gad

def normalize_feature(features):
  means = np.mean(features, axis=0)
  std_devs = np.std(features, axis=0)
  normalized_features = (features - means)/std_devs
  return means, std_devs, normalized_features

def recover_params(means, std_devs, norm_intercept, norm_params):
  intercept = norm_intercept - np.sum(means*norm_params/std_devs)
  params = norm_params/std_devs
  return intercept, params

def linear_regression(features, values):
  model = sg(eta0=0.001, n_iter=50)
  model = model.fit(features, values)
  intercept = model.intercept_
  params = model.coef_
  return intercept, params

def predictions(dF):
  """
  features = dF[['rain']]
  dummy_units = pd.get_dummies(dF['UNIT'], prefix='unit')
  dummy_hour = pd.get_dummies(dF['hour'], prefix='hour')
  dummy_daywk = pd.get_dummies(dF['day_week'], prefix='day_week')
  features = features.join(dummy_units).join(dummy_hour).join(dummy_daywk)

  #Values
  values = dF['ENTRIESn_hourly']
  """
  features, values = gad(dF)
  #Get arrays
  features_arr = features.values
  values_arr = values.values
  means, std_devs, normalized_features_arr = normalize_feature(features_arr)

  #Perform linear regression withgradient descent
  norm_intercept, norm_params = linear_regression(normalized_features_arr, values_arr)
  intercept , params = recover_params(means, std_devs, norm_intercept, norm_params)
  print len(params)
  print 'Coefficient of non dummy variable by Gradient Descent is ', params[0] 
  predictions = intercept + np.dot(features_arr, params)

  return predictions
