import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages



reader = open(r"./SoilMoistureandCounties.csv",'r')
writer = open(r"./populationVsSoilMoisture.csv", "w")
writer.write("County, Population, Average Deep SoilMoisture_D(%), \n")


reader.readline()

datainput = []

for line in reader:
    r= line.split(",")
    datainput.append(r)


def getkey(item):
    return (item[3])
b = sorted(datainput, key=getkey)


#target_duration=int(B[0][2])




geoid = []
county = []

c=[]

avg_data=[]

i=0

for i in  range(len(b)-1):


    if b[i][3] == b[i+1][3]:
        c.append(float(b[i][4]))

    if b[i][3] != b[i+1][3]:
        c.append(float(b[i][4]))
        avg_data.append(sum(c)/len(c))
        geoid.append(b[i][3])
        county.append(b[i][2])
        c=[]


if b[i][3] == b[i+1][3]:
    c.append(float(b[i+1][4]))
    avg_data.append(sum(c)/len(c))
    geoid.append(b[i+1][3])
    county.append(b[i+1][2])


if b[i][3] != b[i+1][3]:
    avg_data.append(float(b[i+1][4]))
    geoid.append(b[i+1][3])
    county.append(b[i+1][2])



file = open(r"./de-app-work/hydro/TerraPopData/data_US_SLAD_2010.csv",'r')


file.readline()

l = []

for line in file:
    z= line.split(",")
    l.append(z)

t= []




for k in range(len(geoid)):
    for j in range(len(l)):
       if geoid[k] == l[j][1]:
            t.append(l[j][2])
print t



for g in range(len(county)):
    writer.write(county[g]+","+str(t[g])+","+str(avg_data[g])+"\n")


file.close()
reader.close()
writer.close()

#plt.figure()
#for i in range(len(avg_data)):
    #print avg_data[i],t[i],county[i]
#    plt.plot(avg_data[i],t[i], 'o', label=county[i])
#plt.xlabel("Average Deep Soil Moisture %")
#plt.ylabel("Population")
#plt.legend(loc='upper right')
#plt.title('Population per County versus Average Deep Soil Moisture %')
##plt.show()


#plt.savefig('PopulationVsDeepsoilMositure.pdf')
#plt.close()

#print 'hi'

##with PdfPages('test.pdf') as pdf:
##
##
##    fig1 = plt.figure()
##    pdf.savefig(fig)
##    pdf.savefig()
##    plt.close


##plt.show()
##plt.draw()
##fig1.savefig('tessstttyyy.png', dpi=100)




