# #pip install -U tensorly
# #pip install numpy
# #pip install matplotlib

# import tensorly as tl
# import matplotlib.pyplot as plt
# tensor = []

# #testing incremental numbers
# x = 1
# for i in range(5):
#     tensor.append([])
#     for q in range(5):
#         tensor[i].append(x)
#         x += 1
    
# print(tensor)
# tensor = tl.tensor(tensor)
# plt.imshow(tensor, cmap='viridis', interpolation='nearest')
# plt.colorbar()
# plt.title('Tensor Heatmap')
# plt.show()
# #start with 2d -> 3d heatmap
# #use (time) as layers (1-2pm change heatmap)
import time
for i in range(1000):
    loop_time = time.time()

    print(i)
    if i % 100 == 0:
        print('Time {}'.format(1 / (time.time() - loop_time)))    