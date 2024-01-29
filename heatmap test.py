#pip install -U tensorly
#pip install numpy
#pip install matplotlib

import tensorly as tl
import numpy as np
import matplotlib.pyplot as plt

tensor = tl.tensor(np.random.rand(5, 5))
print(tensor)

plt.imshow(tensor, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.title('Tensor Heatmap')
plt.show()
#start with 2d -> 3d heatmap
#use (time) as layers (1-2pm change heatmap)
