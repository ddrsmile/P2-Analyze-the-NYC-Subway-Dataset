import numpy as np
import pandas as pd

def getAnalysisData(dF):
  #Features
  features = dF[['rain']]
  dummy_units = pd.get_dummies(dF['UNIT'], prefix='unit')
  dummy_hour = pd.get_dummies(dF['hour'], prefix='hour')
  dummy_daywk = pd.get_dummies(dF['day_week'], prefix='day_week')
  features = features.join(dummy_units).join(dummy_hour).join(dummy_daywk)
  #Values
  values = dF['ENTRIESn_hourly']
  return features, values
