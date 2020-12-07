import matplotlib.pyplot as plt 
import csv

tax_file = open('corporate_tax_rate.csv')
president_file = open('presidents.csv')
unemployment_file = open('unemployment_rate.csv', encoding='utf-8-sig')

tax_csvr = csv.DictReader(tax_file)
presidents_csvr = csv.DictReader(president_file)
unemployment_csvr = csv.DictReader(unemployment_file)

repredback = '#FCECE9' 
dembluback = '#EAF0F9' 
repred = '#FE5C40'
demblu = '#3571C0'

def get_unemployment(csvr):
  dates = []
  rates = []
  for row in csvr:
    try:
      year = float(row['Year'])
      rate = float(row['12'])

      dates.append(year)
      rates.append(rate)
    except Exception as e:
      pass

  return dates, rates

def get_presidents(csvr):
  president_dict = {}
  for year in csvr:
    president_dict[int(year['year'])] = {
      'name': year['name'],
      'party': year['alignment']
    }

  return president_dict

def get_tax(csvr):
  dates, rates = [[],[]]
  for row in csvr:
    date = float(row['year'])
    rate = float(row['max_rate'])

    dates.append(date)
    rates.append(rate)

  return dates, rates

def get_years():
  years = [i for i in range(1912, 2020, 4)]
  years.insert(0, 1909)
  return years

def get_xticks(years, presidents):

  xticks = []

  for x in years:
    if x % 4 != 0:
      x = x - (x % 4)

    name = presidents[x]['name']

    x = '{} ({})'.format(name, x).rjust(28)
    xticks.append(x)

  return xticks



years = get_years()
tax_dates, tax_rates = get_tax(tax_csvr)
presidents = get_presidents(presidents_csvr)
unp_dates, unp_rates = get_unemployment(unemployment_csvr)
xticks = get_xticks(years, presidents)


tax_range = [0, max(tax_rates)]

#fig, ax = plt.subplots()

plt.plot(tax_dates, tax_rates, color='black')
plt.plot(unp_dates, unp_rates, color='black')

plt.xticks(years, xticks, rotation=70, horizontalalignment='right', verticalalignment='top')
plt.subplots_adjust(bottom=0.4, right=0.95)

for pres in presidents.keys():
  start = pres
  end = pres + 4
  color = repred if presidents[pres]['party'] == 'Republican' else demblu
  plt.fill_betweenx(tax_range, start, end, color=color)


plt.show()
