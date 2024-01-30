import tensorly as tl
import pandas as pd
import time
file_path = "data/uber-raw-data-apr14.csv"
selected_col = ['Lat', 'Lon']
data = pd.read_csv(file_path, usecols=selected_col)
lat = data.Lat.tolist()
lon = data.Lon.tolist()

# lat = [2,2.16,4,5.82,6]
# lon = [2,2.16,4,5.82,6]
print("Info of latitudes: ")
print("Min: " + str(min(lat)))
print("Max: " + str(max(lat)))
print("Len: " + str(len(lat)))

print("\nInfo of latitudes: ")
print("Min: " + str(min(lon)))
print("Max: " + str(max(lon)))
print("Len: " + str(len(lon)))

#Preset Variables
subdiv = 25 #25x25 grid
tensor = []
for i in range(25): #create tensor starting values
    tensor.append([])
    for x in range(25):
        tensor[i].append(0)

# print(tensor)

#get incremental values of both arrays
lat_inc = round((max(lat) - min(lat))/subdiv, 7) 
lon_inc = round((max(lon) - min(lon))/subdiv, 7)
print(str(lat_inc) + " " + str(lon_inc))

latmin = min(lat)
lonmin = min(lon)
for i in range(len(lon)):
    #loop_time = time.time()

    temp = lon[i] - lonmin  
    lonx = int(temp / lon_inc)
    
    temp = lat[i] - latmin
    latx = int(temp / lat_inc)

    tensor[lonx][latx] += 1
    if i % 10000 == 0:
        print(i)
    #print('Time {}'.format(1 / (time.time() - loop_time)))    

for i in tensor:
    print(i)