import tensorly as tl
import pandas as pd
import matplotlib.pyplot as plt

def start():
    file_path = "data/uber-raw-data-apr14.csv"
    selected_col = ['Lat', 'Lon']
    data = pd.read_csv(file_path, usecols=selected_col)
    global lat 
    lat = data.Lat.tolist()
    global lon
    lon = data.Lon.tolist()

    print("Info of latitudes: ")
    print("Min: " + str(min(lat)))
    print("Max: " + str(max(lat)))
    print("Len: " + str(len(lat)))

    print("\nInfo of longitudes: ")
    print("Min: " + str(min(lon)))
    print("Max: " + str(max(lon)))
    print("Len: " + str(len(lon)))

def tensor_create(subdiv):
    global tensor
    tensor = []
    for i in range(subdiv):
        tensor.append([])
        for x in range(subdiv):
            tensor[i].append(0)

    lat_inc = round(((max(lat) - min(lat))+1)/subdiv, 7)
    lon_inc = round(((max(lon) - min(lon))+1)/subdiv, 7)

    latmin = min(lat)
    lonmin = min(lon)


    for i in range(len(lon)):
        
        tempa = round(lon[i] - lonmin, 7)
        lonx = int(tempa // lon_inc)
        
        tempb = round(lat[i] - latmin, 7)
        latx = int(tempb // lat_inc)

        tensor[lonx][latx] += 1
        if i % 10000 == 0:
            print(i)


def main():
    subdiv = 1000
    start()
    tensor_create(subdiv)
    global tensor
    tensor = tl.tensor(tensor)
    plt.imshow(tensor, cmap='viridis', interpolation='nearest')
    plt.colorbar()
    plt.title('Tensor Heatmap')
    plt.show()
    
if __name__ == "__main__":
    main()