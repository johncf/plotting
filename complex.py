#!/bin/python3
# source: http://fredrik-j.blogspot.in/2009/08/3d-visualization-of-complex-functions.html

import numpy as np

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import pyplot as plt
import mpmath
mpmath.dps = 5

# Use instead of arg for a continuous phase
def arg2(x):
    return mpmath.sin(mpmath.arg(x))

#f = lambda z: abs(mpmath.loggamma(z))
#f = lambda z: arg2(mpmath.exp(z))
#f = lambda z: abs(mpmath.besselj(3,z))
f = lambda z: arg2(mpmath.cos(z))

fig = plt.figure()
ax = Axes3D(fig)
X, Y = np.ogrid[-5:5:0.125, -5:5:0.125]
Z = X + 1j * Y

fv = np.vectorize(f)
W = fv(Z)

X, Y = np.meshgrid(X, Y)

#ax.plot_surface(X, Y, W, rstride=1, cstride=1, cmap=cm.jet)
ax.plot_wireframe(X, Y, W, rstride=5, cstride=5)

plt.show()
