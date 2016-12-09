#import numpy as np
import matplotlib.pyplot as plt
#matplotlib.use('Agg')
import csv
from operator import itemgetter

print('in bubble_chart_per_mois_def_bte.py')

def plot_graph(pop, county_labs, percent_def):
    print('plotting graph')
	#setting up variables for graph
    colors = ['blue', 'royalblue', 'lightskyblue', 'powderblue', 'indianred'] #these are corresponding to the order of minimum average soil moisture (just the order, no scaling)
    max_marker_size = 1250
    min_marker_size = 75
    marker_range = max_marker_size - min_marker_size
    area = []
    county = [0,1,2,3,4]
	#scale the population values into marker size range
    for population in pop:
        area.append(min_marker_size+marker_range*(population-min(pop))/(max(pop)-min(pop)))

	#make county names appear on xaxis
	plt.xticks(county, county_labs)


    cm = plt.cm.get_cmap('RdYlBu')
    plt.scatter(county, percent_def, s=area, c=min_mois, alpha=0.5, label=''+str(pop), vmin=0.08, vmax=0.10, cmap=cm)
    plt.xlabel("County")
    plt.annotate('  pop. \n226,073', xy=(2.65, 73.55), xytext=(3.65, 73.55),)
    plt.annotate('  pop. \n28,961', xy=(2.5, 75), xytext=(2.80, 75),)
    plt.annotate('  pop. \n33,140', xy=(1, 75.1), xytext=(1.75, 75.1),)
    plt.annotate('  pop. \n23,956', xy=(.78, 76), xytext=(0.75, 76),)
    plt.annotate('  pop. \n55,342', xy=(-0.1, 75.6), xytext=(-0.1, 75.6),)
    plt.ylabel("Soil Moisture Decrease(%)")
    plt.ylim(73,76.5)
    cbr=plt.colorbar(orientation='horizontal', ticks=[0.08,0.085, 0.09, 0.095, 0.10])
    cbr.set_label('Minimum Deep Soil Moisture (%)')

        #plt.title("% Decrease in the Deep Soil Moisture per county")


	#lgd = plt.legend(scatterpoints=1, labelspacing=1.0, borderaxespad=0., borderpad=1.0, markerscale = 0.750, title = 'Minimum soil moisture (%)',fontsize =12)
    #lgd = plt.legend(scatterpoints=1, labelspacing=1.0, borderaxespad=0., borderpad=1.0, markerscale = 0.750, title = 'Minimum soil moisture (%)',fontsize =12)
    plt.savefig('/PopulationVsDeepsoilMoisture1.pdf', bbox_inches='tight')
    plt.show()


#get data from the csv in rows as individual lists and put them in one list
all_data = []
with open('./decrease.csv', 'rb') as csvfile:
	rdr = csv.reader(csvfile, delimiter=',')
	for row in rdr:
		all_data.append(row)
del all_data[0] #delete column headings

#sort by minimum average soil moisture for color gradient in plot
all_data = sorted(all_data, key=itemgetter(2))

#put lists of rows into lists of columns
county_labs = []
pop = []
percent_def = []
min_mois = []
for row in all_data:
    county_labs.append(row[0])
    pop.append(int(row[1]))
    percent_def.append(float(row[4]))
    min_mois.append(float(row[2]))


plot_graph(pop, county_labs, percent_def)
