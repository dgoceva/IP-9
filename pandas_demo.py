import pandas as pd
import matplotlib.pyplot as plt

FNAME = '3139529.csv'

data = pd.read_csv(FNAME).dropna()
# print(data)

data.plot(title='Daily Temperatures\nSofia, 2022',
          x='DATE', y=['TMIN', 'TMAX'], rot=15,
          xlabel='Date', ylabel='Temperature, C', color=['blue', 'red'],
          alpha=0.6)
plt.fill_between(data['DATE'], data['TMIN'],
                 data['TMAX'], color='blue', alpha=0.1)
plt.show()
