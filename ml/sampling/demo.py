target_x_0 = [-1.0, 1.0]
target_x_1 = [-1.0, 1.0]
import numpy as np
import matplotlib.pyplot as plt

vertexes = np.array([[target_x_0[0], target_x_1[0]],
                         [target_x_0[0], target_x_1[1]],
                         [target_x_0[1], target_x_1[1]],
                         [target_x_0[1], target_x_1[0]],
                         [target_x_0[0], target_x_1[0]]]
                       )
g1 = lambda x: x[0]
g2 = lambda x: x[1]
plt.plot(g1(vertexes), g2(vertexes), 'red')
plt.show()