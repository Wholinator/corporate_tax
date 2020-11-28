import matplotlib.pyplot as plt 
import csv

data_file = open('data.csv')

csvr = csv.reader(data_file)

dates = []
rates = []
xticks = [i for i in range(1912, 2020, 4)]
xticks.insert(0, 1909)
print(xticks)

header = next(csvr)
for row in csvr:
  date = float(row[0])
  rate = float(row[1])

  dates.append(date)
  rates.append(rate)

plt.plot(dates, rates)
plt.xticks(xticks, rotation=70)
plt.show()



