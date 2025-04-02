import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np_normal = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np_normal)
print('min: ', np.amin(np_normal, axis=0))
print('max: ', np.amax(np_normal, axis=0))
print('min: ', np.amin(np_normal, axis=1))
print('max: ', np.amax(np_normal, axis=1))

