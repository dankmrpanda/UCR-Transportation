import math
import matplotlib.pyplot as plt
import tensorly as tl
import pandas as pd
import statistics
import time
import numpy as np
total = time.time()

np.seterr(divide = 'ignore')

def map(x, inL, inH, outL, outH):
    return (x - inL) / (inH - inL) * (outH - outL) + outL

loop_time = time.time()
file_path = "data/uber-raw-data-sep14.csv"
selected_col = ['Lat', 'Lon']
data = pd.read_csv(file_path, usecols=selected_col)
lon = data.Lon.tolist()
lat = data.Lat.tolist()
print('Time took to read data: {}'.format((time.time() - loop_time)*1000))

loop_time = time.time()
tolerance = 7 #edit this

lonStDev = statistics.stdev(lon)
latStDev = statistics.stdev(lat)

lonMean = sum(lon) / len(lon)
latMean = sum(lat) / len(lat)

cordRange = max(lonStDev, latStDev) * tolerance

i = 0
while i < len(lon):
    if(abs(lon[i] - lonMean) > cordRange or abs(lat[i] - latMean) > cordRange):
        del lon[i], lat[i]
        i -= 1
    if i % 100000 == 0: #logger
        print(i)
    i += 1
del(i)
print('Time took to filter out outliers: {}'.format((time.time() - loop_time)*1000))

print("\nInfo of longitudes: ")
print("Min: " + str(min(lon)))
print("Max: " + str(max(lon)))
print("Len: " + str(len(lon)))
print("Range: " + str(max(lon) - min(lon)))

print("\nInfo of latitudes: ")
print("Min: " + str(min(lat)))
print("Max: " + str(max(lat)))
print("Len: " + str(len(lat)))
print("Range: " + str(max(lat) - min(lat)))

#Preset Variables
subDiv = 8000 #use with lower numbers, preferably < 8000
tensor = np.zeros((subDiv, subDiv))

#get incremental values of both arrays
increment = cordRange / subDiv

lonMin = lonMean - cordRange
lonMax = lonMean + cordRange

latMin = latMean - cordRange
latMax = latMean + cordRange

print("Increment Value: " + str(increment))

loop_time = time.time()
for i in range(len(lon)):
    
    lonx = math.floor(map(lon[i], lonMin, lonMax, 0, subDiv - 1))
    
    laty = math.floor(map(lat[i], latMin, latMax, subDiv - 1, 0))

    tensor[laty][lonx] += 1 #counts the amount of times an interval is reached

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