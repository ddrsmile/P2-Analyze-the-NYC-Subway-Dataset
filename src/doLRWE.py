import numpy as np
import pandas as pd
import lr_sklearn as sk
import lr_statsmodels as sm

def get_rsquared(data, predict):
  a = ((data - predict)**2).sum()
  b = ((data - np.mean(data))**2).sum()
  rsquared = 1 - a/b
  return rsquared


path = r'../dataSet/turnstile_weather_v2.csv'
dF = pd.read_csv(path)
dF = dF[:][dF['weekday'] == 1]
predict_sk = sk.predictions(dF)
predict_sm = sm.predictions(dF)

data = dF['ENTRIESn_hourly']

print 'R squared by Gradient Descent: ' '{0:.4f}'.format(get_rsquared(data, predict_sk))
print 'R squared by Ordinary least squares: ' '{0:.4f}'.format(get_rsquared(data, predict_sm))
