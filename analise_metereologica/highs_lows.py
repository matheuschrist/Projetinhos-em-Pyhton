import csv 
from matplotlib import pyplot as plt
from datetime import datetime


filename = 'death_valley_2014.csv' 
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    


# Obtém as datas e as temperaturas máximas e mínimas do arquivo

    dates,highs,lows = [],[] ,[]
    for row in reader: 
        try:
            current_date=datetime.strptime(row[0],"%Y-%m-%d")

            high=int(row[1])
            
            low=int(row[3])
            
        except ValueError:
            print(current_date,"missing Data")

        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


# Faz a plotagem dos dados 
fig = plt.figure(dpi=128, figsize=(10, 6)) 
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
  # Formata o gráfico 
fig.autofmt_xdate()
plt.title("Daily High and Low temperatures 2014", fontsize=24)
plt.xlabel('Date', fontsize=16) 
plt.ylabel("Temperature (F)", fontsize=16) 
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()




