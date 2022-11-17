import csv
from datetime import datetime
import matplotlib.pyplot as plt

FNAME = '3139529.csv'

with open(FNAME) as f:
    reader = csv.reader(f)
    header = next(reader)
    # print(header)
    dates, highs, lows = [], [], []
    for row in reader:
        # try:
        if row[5] != '' and row[6] != '':
            dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
            highs.append(float(row[5]))
            lows.append(float(row[6]))
        # except ValueError:
            # print(f'Missing temperature for {row[2]}')
    # print(dates[:5])
    # print(highs[:5])
    # print(lows[:5])

plt.style.use('bmh')
fig, ax = plt.subplots()
fig.autofmt_xdate()
ax.set_title('Daily Temperatures\nSofia, 2022', fontsize=18)
ax.set_xlabel('Dates', fontsize=14)
ax.set_ylabel('Temperature (C)', fontsize=14)
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, lows, highs, color='blue', alpha=0.1)
ax.tick_params(axis='both', labelsize=12)
plt.show()
