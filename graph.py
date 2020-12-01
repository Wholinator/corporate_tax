import matplotlib.pyplot as plt 
import csv

tax_file = open('corporate_tax_rate.csv')
president_file = open('presidents.csv')

csvr = csv.reader(tax_file)
presidents = csv.DictReader(president_file)

president_dict = {}

for year in presidents:
  president_dict[int(year['year'])] = {
    'name': year['name'],
    'party': year['alignment']
  }

print(president_dict)

dates = []
rates = []
years = [i for i in range(1912, 2020, 4)]
years.insert(0, 1909)
xticks = []

for x in years:
  if x % 4 != 0:
    x = x - (x % 4)

  name = president_dict[x]['name']

  x = '{} ({})'.format(name, x).rjust(28)
  xticks.append(x)

header = next(csvr)
for row in csvr:
  date = float(row[0])
  rate = float(row[1])

  dates.append(date)
  rates.append(rate)

tax_range = [0, max(rates)]

repredback = '#FCECE9' 
dembluback = '#EAF0F9' 
repred = '#FE5C40'
demblu = '#3571C0'


fig, ax = plt.subplots()

ax.plot(dates, rates, color='black')
plt.xticks(years, xticks, rotation=70, horizontalalignment='right', verticalalignment='top')
plt.subplots_adjust(bottom=0.4, right=0.95)

for pres in president_dict.keys():
  start = pres
  end = pres + 4
  color = repred if president_dict[pres]['party'] == 'Republican' else demblu
  plt.fill_betweenx(tax_range, start, end, color=color)


plt.show()
