import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import mlab as mlab
from matplotlib import gridspec as gc

def plotBarDayWeek(dF, ax):
  entries_rainy = []
  entries_nonrainy = []
  days = np.arange(7)
  for day in days:
    rainy_day = np.mean(dF['ENTRIESn_hourly'][dF['day_week'] == day][dF['rain'] == 1])
    nonrain_day = np.mean(dF['ENTRIESn_hourly'][dF['day_week'] == day][dF['rain'] == 0])
    entries_rainy.append(rainy_day)
    entries_nonrainy.append(nonrain_day)

  daysLabel = ['Sun.', 'Mon.', 'Tue.', 'Wed.', 'Thur.', 'Fri.', 'Sat.']
  ax.bar(days - 0.15, entries_nonrainy, color='b', align='center', label='non rainy days', width = 0.3)
  ax.bar(days + 0.15, entries_rainy, color='g', align='center', label='rainy days', width = 0.3)
  ax.set_title('Daily Entries')
  ax.legend(loc='upper right')
  ax.set_xticks(days)
  ax.set_xticklabels(daysLabel)
  ax.set_xlabel('Day [day]')
  ax.set_ylabel('Average Entries per Day [-]')

def plotBarHourly(dF, ax):
  entries = []
  hours = range(0, 24, 4)
  for hour in hours:
    entry_hourly = np.mean(dF['ENTRIESn_hourly'][dF['hour'] == hour])
    entries.append(entry_hourly)
  ax.bar(hours, entries, align='center', width=3)
  ax.set_title('Hourly Entries')
  ax.set_xlabel('Hour [hour]')
  ax.set_xticks(hours)
  ax.set_ylabel('Average Entries per Hour [-]')

path = r'../dataSet/turnstile_weather_v2.csv'
dF = pd.read_csv(path)
fig = plt.figure(num=None, figsize=(20, 5), dpi = 80)
gs = gc.GridSpec(1,2)
gs.update(hspace = 0, bottom = 0.15)
ax1 = fig.add_subplot(gs[0])
plotBarDayWeek(dF, ax1)
ax2 = fig.add_subplot(gs[1]) 
plotBarHourly(dF, ax2)


plt.show()
