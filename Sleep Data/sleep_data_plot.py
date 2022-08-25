from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import json
import glob

data = []

for file_path in glob.glob('./sleep/*.json'):
    with open(file_path) as file:
        for item in json.load(file):
            data.append(item)

data2 = [{'startTime': data[0]['startTime'].split('T')[0] + 'T00:00:00.00',
          'endTime': data[0]['startTime'].split('T')[0] + 'T00:00:00.00'}]
for record in data:
    if record['startTime'].split('T')[0] != record['endTime'].split('T')[0]:
        data2.append({'startTime': record['startTime'],
                      'endTime': record['startTime'].split('T')[0]+"T23:59:59.999"})
        data2.append({'startTime': record['endTime'].split('T')[0]+"T00:00:00.000",
                      'endTime': record['endTime']})
    else:
        data2.append({'startTime': record['startTime'],
                      'endTime': record['endTime']})

time_array = np.array([[mdates.datestr2num(record['startTime'].split('T')[0]),
                        mdates.datestr2num(record['startTime'].split('T')[0])] for record in data2])
time_array2 = np.array([[mdates.datestr2num(record['startTime'].split('T')[1])] for record in data2])
time_array3 = np.array([[mdates.datestr2num(record['endTime'].split('T')[1])] for record in data2])

fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

for date, date2, date3 in zip(time_array, time_array2, time_array3):
        ax.plot((date2,date3), date, "b")

ax.yaxis.set_major_locator(plt.LinearLocator(20))
ax.set_xticks(ticks=[mdates.datestr2num('00:00:00.000'), mdates.datestr2num('01:00:00.000'), mdates.datestr2num('02:00:00.000'), mdates.datestr2num('03:00:00.000'), mdates.datestr2num('04:00:00.000'), mdates.datestr2num('05:00:00.000'), mdates.datestr2num('06:00:00.000'), mdates.datestr2num('07:00:00.000'), mdates.datestr2num('08:00:00.000'), mdates.datestr2num('09:00:00.000'), mdates.datestr2num('10:00:00.000'), mdates.datestr2num('11:00:00.000'), mdates.datestr2num('12:00:00.000'), mdates.datestr2num('13:00:00.000'), mdates.datestr2num('14:00:00.000'), mdates.datestr2num('15:00:00.000'), mdates.datestr2num('16:00:00.000'), mdates.datestr2num('17:00:00.000'), mdates.datestr2num('18:00:00.000'), mdates.datestr2num('19:00:00.000'), mdates.datestr2num('20:00:00.000'), mdates.datestr2num('21:00:00.000'), mdates.datestr2num('22:00:00.000'), mdates.datestr2num('23:00:00.000'), mdates.datestr2num('23:59:59.999')])
plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
ax.set_xlim(mdates.datestr2num('00:00:00.000'), mdates.datestr2num('23:59:59.999'))
ax.set_ylim(mdates.datestr2num('2018-05-09'), mdates.datestr2num('2021-03-31'))
plt.show()

