import pandas as pd

def getHourlyEntries(dF):
  dF['ENTRIESn_hourly'] = (dF['ENTRIESn'] - dF['ENTRIESn'].shift(1)).fillna(1)
  return dF

def getHour(dF):
  times = dF['TIMEn'].values
  hours = [int(time.split(':')[0]) for time in times]
  dF['hour'] = hours
  return dF
