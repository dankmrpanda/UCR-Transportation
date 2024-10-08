# UCR-Transportation
Tensor methods are very effective in modeling and extracting knowledge from multi-aspect data. Spatiotemporal data (e.g., trajectory data, satellite image data, etc) are inherently multi-aspect and can be expressed as tensors. In this project, we will explore the power of tensor methods for modeling and mining spatiotemporal data.

# Heatmap Generation Summary
The heatmap takes into account the number of occurrences of rides in a certain interval, determined by the preset size of the tensor.

1. After reading the longitude and latitude data from the CSV, we will filter out outliers using standard deviation
  - The amount of outliers removed is managed by a variable called "tolerance"
2. It will then generate the tensor, in the form of a numpy array.
  - The size of this array is managed by a variable called "subDiv"
  - its subDiv by subDiv
  - This tensor is generated by determining which interval a set of longitude and latitudes belong in, then adding one to that position in the tensor
  - While doing this I noticed that the data was rotated 90 degrees so some adjustments were needed to rotate it back
3. Then we will log scale each value of the tensor to make the smaller values more visible.
  - While doing this, this is where the numpy array comes in handy
  - If we were to do this normally (using for loops) it would take an insane amount of time (since we have around 80k values)
  - Therefore, by using NumPy's ability of a vectorized function, which runs the function's code in C which speeds up the time by 3x
4. Then we generate a heatmap using matplotlib, an example picture is shown below (tolerance = 7, subDiv = 8000):

![image](https://github.com/user-attachments/assets/6667945d-6c4e-494e-a9d2-ed3a138baf88) ![image](https://github.com/user-attachments/assets/2d56afee-4b13-49fb-b4aa-6245ef2f4452)

On average, this entire program takes around 13 seconds to process 80k values and a tensor array 8000 by 8000


## Installation
```
pip install -U tensorly
pip install pandas
pip install matplotlib
pip install numpy
```

## File Navigation
`heatmap.py`: stable & main file to run, generates heatmap according to datasets

`archive/`: contains all other datasets

`data/`: contains usable datasets

`heatmap test.py`: initial testing for heatmap creation (outdated)

`testing.py`: most recently edited file, may be unstable

`tensor creation.py`: testing for tensor array creation, has logic in comments (outdated)

## Todo
- [x] Create 2d heatmap | fin 1/30
- [x] Use numpy to optimize https://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/VectorizedOperations.html | fin 1/31
- [x] remove outliers | fin 2/5
- [x] make x and y increments same | fin 2/5
- [ ] make code run on GPU (for fun)
- [ ] fix blank lines showing at high subDiv values (either data problem or generation problem)
- [ ] Use time as layers (1-2pm change heatmap)
- [ ] Create 3d heatmap
- [ ] Create 3d changes with time
