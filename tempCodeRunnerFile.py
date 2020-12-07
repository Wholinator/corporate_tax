plt.xticks(years, xticks, rotation=70, horizontalalignment='right', verticalalignment='top')
plt.subplots_adjust(bottom=0.4, right=0.95)

for pres in presidents.keys():
  start = pres
  end = pres + 4
  color = repred if presidents[pres]['party'] == 'Republican' else demblu
  plt.fill_betweenx(tax_range, start, end, color=color)