################################################################################

########## Filtering the VIC Model output flux file#############################


################################################################################
#Define Function in order to sort the data ascendingly based on deep soil moisture
# %  column

def getkey(item):
    return float(item[7])
################################################################################

# Open the file that needs to be filtered
reader = open(r"/spatiotempSoilMoistureEcohydro.csv",'r')
# Read lines in this file
reader.readline()

# New csv file will be created to save the output from the python code

writer = open(r"/VICModelOutputFiltered_MAX.csv", "w")

#In this file write the header names the purpose of \n is to go to the next line

writer.write("long, lat, duration,SoilMoisture_D(%), \n")

# Open an empty array to append the data in the file

Data=[]

#Split each value in the data file using the ",". Since this file is csv then
#the separator is",". This data will be temporary stored in array called value.
# Afterthat append the seperated values in the newly created array Data.

for line in reader:
    value = line.split(",")

    Data.append(value)


B = sorted(Data, key=getkey)

# Create a variable called target_duration. This array will contain the year and
# the month that have the least value for the Deep soil moisture content %
#in the whole data set

target_duration=int(B[-1][2])


#Looping inside the Data array to get the corresponding row to the target duration value
# counter i
i=0

# For any i  less than the length of the Data array. An If codition is made to
#compare column 2 (duartion) in the sorted data with th target duration,
#if they are equal then append certain columns values row i to VICModelOutputFiltered.csv file

while i < len(Data):

    if int(B[i][2]) == target_duration:

        writer.write(B[i][1]+","+B[i][0]+","+B[i][2]+","+B[i][7]+"\n")


    i += 1
#Close the writer
writer.close()

