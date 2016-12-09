import ogr, sys

driver = ogr.GetDriverByName('ESRI Shapefile')
datasource = driver.Open('./de-app-work/hydro/TerraPopData/boundaries_US_SLAD_2010.shp', 0)

reader = open(r"./VICModelOutputFiltered.csv",'r')
reader.readline()

#writer = open(r"./TerraPopCalculations", "w")
file = open('SoilMoistureandCounties.csv', 'w')
file.write("long, lat, County, GEOID, SoilMoisture_D(%),population \n")
s= []


for line in reader:
    value = line.split(",")
    s.append(value)

#layer = datasource.GetLayer()
#feature = layer.GetNextFeature()

i = 0
while i < len(s):
    print i
    point = ogr.Geometry(ogr.wkbPoint)
    point.AddPoint(float(s[i][0]), float(s[i][1]))
    #dod=raw_input("hi")
    layer = datasource.GetLayer()
    feature = layer.GetNextFeature()
    #dod=raw_input("hi2")
    y=0
    while feature:
        LABEL = feature.GetFieldAsString('LABEL')
        GEOID = feature.GetFieldAsString('GEOID')

        geom = feature.GetGeometryRef()
        if geom.Contains(point) == True:
            file.write(str(s[i][0])+','+str(s[i][1])+','+LABEL+','+ GEOID+ ',' +s[i][3])

    # write info out to the text file
        #file.write(LABEL + ' ' + x + ' ' + y + ' ' + GEOID +' '+ str(geom)  + '\n')
    #print geom

    # destroy the feature and get a new one
        feature.Destroy()
        feature = layer.GetNextFeature()
        y += 1

    datasource.Destroy()
    datasource = driver.Open('./de-app-work/hydro/TerraPopData/boundaries_US_SLAD_2010.shp', 0)





    print "y", y

    point.Destroy()
    i += 1

#datasource.Destroy()
file.close()
