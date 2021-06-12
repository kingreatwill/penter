import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.001)
y = 1 / (1 + np.exp(-x))
plt.plot(x, y)
plt.suptitle(r'$y=\frac{1}{1+e^{-x}}$', fontsize=20)
plt.grid(color='gray')
plt.grid(linewidth='1')
plt.grid(linestyle='--')
plt.show()

x = np.linspace(-10, 10, 100)
y = 1 / (1 + np.exp(-x))
plt.xlabel("x")
plt.ylabel("y")
plt.title("sigmoid function and its derivative image")
plt.plot(x, y, color='r', label="sigmoid")
y = np.exp(-x) / pow((1 + np.exp(-x)), 2)
plt.plot(x, y, color='b', label="sigmoid derivative")
plt.legend()  # 将plot标签里面的图注印上去
plt.show()

r = np.linspace(-20, 20, 500)
plt.xlabel("r")
plt.ylabel("y")
plt.title("Gaussian RBF")
for delta in [1, 5, 0.5]:
    y = np.exp(-(r ** 2 / (2 * delta ** 2)))
    plt.plot(r, y, label="δ = " + str(delta))

plt.legend()  # 将plot标签里面的图注印上去
plt.show()

r = np.linspace(-20, 20, 500)
plt.xlabel("r")
plt.ylabel("y")
plt.title("Inverse multiquadrics RBF")
for delta in [1, 5, 0.5]:
    y = 1 / (np.sqrt(r ** 2 + delta ** 2))
    plt.plot(r, y, label="δ = " + str(delta))

plt.legend()
plt.show()

r = np.linspace(-10, 10, 500)
plt.xlabel("r")
plt.ylabel("y")
plt.title("Reflected Sigmoidal RBF")
for delta in [1, 5, 0.5]:
    y = 1 / (1 + np.exp(r ** 2 / delta ** 2))
    plt.plot(r, y, label="δ = " + str(delta))

plt.legend()
plt.show()

# sympy 绘制图像
# from sympy.plotting import plot
# from sympy import symbols
#
# x = symbols('x')
# p2 = plot(x*x, (x, -10, 10))
from sympy.plotting import plot
from sympy import symbols
from sympy.functions import exp

r = symbols('r')
p = []
for delta in [1, 5, 0.5]:
    y = 1 / (1 + exp(r ** 2 / delta ** 2))
    p.append((y, (r, -10, 10)))
p2 = plot(*p)


