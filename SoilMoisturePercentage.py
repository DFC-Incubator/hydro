import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import sys
from operator import itemgetter

print 'hello from SoilMoisturePercentage.py'

print("Path at terminal when executing this file")
print(os.getcwd() + "\n")

if os.path.isfile('./populationVsSoilMoisture.csv'):
   print 'my expected input file is there'
else:
   sys.exit('my  soil moisture file is missing')

# open populationVsSoilMoisture.csv and extract data
min_data = []
with open('./populationVsSoilMoisture.csv', 'rb') as csvfile:
 rdr = csv.reader(csvfile, delimiter=',')
 for row in rdr:
  min_data.append(row)
del min_data[0]  # delete column headings
min_data.sort()
csvfile.close()

# open populationVsSoilMoisture_Max.csv and extract data
max_data = []
with open('./populationVsSoilMoisture_Max.csv', 'rb') as csvfile:
 rdr = csv.reader(csvfile, delimiter=',')
 for row in rdr:
  max_data.append(row)
del max_data[0]  # delete column headings
max_data.sort()
csvfile.close()

# create new file to append all the extracted data besides the calculated deficit
with open('/decrease.csv', 'wb') as csvfile:
 headings = 'County, Population, Avg. Deep Soil Moisture Min,' \
            ' Avg. Deep Soil Moisture Max, Decrease in water deficit (%)' + '\n'
 csvfile.write(headings)
 for i in range(len(min_data)):
  if min_data[i][0] == max_data[i][0] and min_data[i][1] == max_data[i][1]:
   deficit = (float(max_data[i][2]) - float(min_data[i][2]))/float(max_data[i][2]) * 100.0
   line = str(min_data[i][0])+','+str(min_data[i][1])+','+str(min_data[i][2])\
          + ','+str(max_data[i][2]) + ',' + str(deficit) + '\n'
   csvfile.write(line)
csvfile.close()