'''
Logic Trail for following

1. Loop through all the values of longitude & latitude
2. Find the intervals for each tensor value
    1. Get the difference between the max and min values + 1
    2. Divide that by the number of sub-divisions to get the increment value between each interval
3. Subtract value by the smallest value of dataset
4. Integer divide the new value by the interval value to get the interval location
5. Latitude will be the outter array (tensor[])
6. Longitude will be inner array (tensor[][])


Ex: 
Lat: [1, 2, 3, 4, 5]
Long: [1, 2, 3, 4, 5]
subdiv = 5 (5x5 graph)

increment_value_lat = (max(Lat) - min(Lat)) / subdiv # = 1
increment_value_long = (max(Long) - min(Long)) / subdiv # = 1
'''


import tensorly as tl
import pandas as pd
import time
file_path = "data/uber-raw-data-apr14.csv"
selected_col = ['Lat', 'Lon']
data = pd.read_csv(file_path, usecols=selected_col)
lat = data.Lat.tolist()
lon = data.Lon.tolist()

print("Info of latitudes: ")
print("Min: " + str(min(lat)))
print("Max: " + str(max(lat)))
print("Len: " + str(len(lat)))

print("\nInfo of longitudes: ")
print("Min: " + str(min(lon)))
print("Max: " + str(max(lon)))
print("Len: " + str(len(lon)))

#Preset Variables
subdiv = 100 #25x25 grid
tensor = []
for i in range(subdiv): #create tensor starting values
    tensor.append([])
    for x in range(subdiv):
        tensor[i].append(0)


#get incremental values of both arrays
lat_inc = round(((max(lat) - min(lat))+1)/subdiv, 7)
lon_inc = round(((max(lon) - min(lon))+1)/subdiv, 7)
print(str(lat_inc) + " " + str(lon_inc))

latmin = min(lat)
lonmin = min(lon)


for i in range(len(lon)):
    #loop_time = time.time()
    
    tempa = round(lon[i] - lonmin, 7) #use round() to fix floating point error
    lonx = int(tempa // lon_inc) #this is the index of the tensor that the value goes into
    
    tempb = round(lat[i] - latmin, 7)
    latx = int(tempb // lat_inc)

    #region debugging
    
    # if (lat[i] == 42.1166):
    #     print(i)
    #     print(str(lat[i]) + str(lon[i]))
    #     print("lonx: " + str(lonx))
    #     print("latx: " + str(latx))
    #     print("tempa: " + str(tempa))
    #     print("tempb: " + str(tempb))
    #     print("lat: " + str(lat[i]))
    #     print("lon: " + str(lon[i]))

    #endregion

    tensor[lonx][latx] += 1 #counts the amount of times an interval is reached
    if i % 10000 == 0: #logger
        print(i)
    #print('Time {}'.format(1 / (time.time() - loop_time)))  

for i in tensor:
    print(i)