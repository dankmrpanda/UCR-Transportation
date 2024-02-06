# UCR-Transportation
Tensor methods are very effective in modeling and extracting knowledge from multi-aspect data. Spatiotemporal data (e.g., trajectory data, satellite image data, etc) are inherently multi-aspect and can be expressed as tensors. In this project, we will explore the power of tensor methods for modeling and mining spatiotemporal data.

## Todo
- [x] Create 2d heatmap | fin 1/30
- [x] Use numpy to optimize https://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/VectorizedOperations.html | fin 1/31
- [x] remove outliers | fin 2/5
- [x] make x and y increments same | fin 2/5
- [ ] make code run on GPU (for fun)
- [ ] Use time as layers (1-2pm change heatmap)
- [ ] Create 3d heatmap
- [ ] Create 3d changes with time


## Installation
```
pip install -U tensorly
pip install pandas
pip install matplotlib
```

## File Navigation
`archive/`: contains all other datasets

`data/`: contains usable datasets

`heatmap test.py`: initial testing for heatmap creation

`natCode.py`: most updated file, used for testing but should be main file to run

`heatmap.py`: stable file to run, generates heatmap according to datasets

`tensor creation.py`: testing for tensor array creation, has logic in comments
