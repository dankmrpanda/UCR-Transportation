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

import math
import stat
import matplotlib.pyplot as plt
import tensorly as tl
import pandas as pd
import time
import numpy as np
import statistics
total = time.time()

np.seterr(divide = 'ignore')

loop_time = time.time()
file_path = "data/uber-raw-data-apr14.csv"
selected_col = ['Lat', 'Lon']
data = pd.read_csv(file_path, usecols=selected_col)
lat = data.Lat.tolist()
lon = data.Lon.tolist()
print('Time took to read data: {}'.format((time.time() - loop_time)*1000))

loop_time = time.time()
latStDev = statistics.stdev(lat)
lonStDev = statistics.stdev(lon)

latMean = sum(lat) / len(lat)
lonMean = sum(lon) / len(lon)

i = 0
stdVal = 10
while i < len(lat):
    if (abs(lat[i] - latMean) > abs(latStDev) * stdVal or abs(lon[i] - lonMean) > abs(lonStDev) * stdVal):
        del lat[i], lon[i]
        i -= 1
    if i % 100000 == 0:
        print(i)
    i += 1
del(i)
print('Time took to filter out outliers: {}'.format((time.time() - loop_time)*1000))

print("Info of latitudes: ")
print("Min: " + str(min(lat)))
print("Max: " + str(max(lat)))
print("Len: " + str(len(lat)))
print("Range: " + str(max(lat) - min(lat)))

print("\nInfo of longitudes: ")
print("Min: " + str(min(lon)))
print("Max: " + str(max(lon)))
print("Len: " + str(len(lon)))
print("Range: " + str(max(lon) - min(lon)))

#Preset Variables
subdiv = 7000 #use with lower numbers, preferably < 7000
tensor = np.zeros((subdiv, subdiv))

#get incremental values of both arrays
lat_inc = ((max(lat) - min(lat)))/ (subdiv - 1)
lon_inc = ((max(lon) - min(lon)))/ (subdiv - 1)
print("Latitude Increment Value: " + str(lat_inc) + 
      "\nLongitude Increment Value: " + str(lon_inc))

latmin = min(lat)
latmax = max(lat)

lonmin = min(lon)
lonmax = max(lon)

loop_time = time.time()
for i in range(len(lon)):
    
    tempa = lon[i] - lonmin
    lonx = int(tempa // lon_inc) #this is the index of the tensor that the value goes into
    
    tempb = lat[i] - latmin
    latx = int(tempb // lat_inc)
    
    tensor[subdiv - latx - 1][lonx] += 1 #counts the amount of times an interval is reached
    if i % 100000 == 0: #logger
        print(i)
    
print('Time took to generate tensor: {}'.format((time.time() - loop_time)*1000))
def log(x):
    return np.where(x != 0, np.log(x), x)

loop_time = time.time()
tensor = log(tensor)
print('Time took to log scale: {}'.format((time.time() - loop_time)*1000))

loop_time = time.time()
tensor = tl.tensor(tensor)
plt.imshow(tensor, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.title('Tensor Heatmap')
print('Heatmap generation took: {}'.format((time.time() - loop_time)*1000))
print('Total time took: {}'.format((time.time() - total)*1000))
plt.show()