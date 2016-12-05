### this script creates the database of monthly soil moisture from 1998 to 2007 for sample sub-watersheds
## created on March 11, 2013


import csv
import os
import sys
import re
import glob
#import temporal
import spatiotempdatabase

#Path of the folder where all the files are stored
path = '/de-app-work/hydro/default/'


d = {}
e = {}
spatiotemporal_dictionary = {}
spatial_prcp = {}
temporal_evaporation = {}
temporal_precipitation = {}


# use join for multi platform compatibility
for dir, subdir, files in os.walk(path):
    for f in files:
        if f.split('_')[0]== "fluxes":
            filepath = path + f
            print filepath
            data = open(filepath, 'r')

            vals = data.readline()

            while vals:
                key = "";
                i = 0

                mct = -999
                mcm =-999
                mcd = -999




                val_list = []
                val_list.append(mct)
                val_list.append(mcm)
                val_list.append(mcd)

                try:
                    for x in vals.split('\t'):

                        try:
                            num = float(x)

                            if i <3:
                                key = key + x;


                            #save mc (top layer)
                            elif i == 8:
                                mct = num
                                val_list[0] = num
                            #save mc (mid layer)
                            elif i == 9:
                                mcm = num
                                val_list[1] = num
                            #save mc (deep layer)
                            elif i == 10:
                                mcd = num
                                val_list[2] = num

                        except:
                            pass

                        i = i+1

                except:
                    pass

                #save soil moisture based on date
                d[key] = val_list
                vals = data.readline()


            #sort the keys by date
            sorted_keys = d.keys()
            sorted_keys.sort()
            avg_mct = []
            avg_mcm = []
            avg_mcd = []

            date_time = []
            year_month = 9999

            for key in sorted_keys:
                if key[0:6] != year_month:
                    year_month = key[0:6];
                    found = False
                    amct = 0
                    amcm = 0
                    amcd = 0

                    count = 0
                    for k in sorted_keys:
                        if k[0:6] == year_month:

                            amct = amct + d[k][0]
                            amcm = amcm + d[k][1]
                            amcd = amcd + d[k][2]

                            count = count + 1
                            found = True
                        else:
                            if found == True:
                                break

                    avg_mct.append(amct/count)
                    avg_mcm.append(amcm/count)
                    avg_mcd.append(amcd/count)


                    date_time.append(year_month)


            for i in range(0,len(date_time)):
                spatiotemporal_dictionary[f.split('_')[1]+"_"+f.split('_')[2]+"_"+str(date_time[i]+"_"+str(date_time[i][0:4])+"_"+str(date_time[i][4:6]))] = avg_mct[i],  avg_mcm[i], avg_mcd[i]


        ## create a csv file that contains all grids & the months and corresponding values

            writer = open("/spatiotempSoilMoistureEcohydro.csv", "wb")
            writer.write("lat, lon, duration, year, month,SoilMoisture_T(%),SoilMoisture_M(%),SoilMoisture_D(%)\n" )
            spatiotempdatabase.write_output(spatiotemporal_dictionary,writer,',')
            writer.close()








