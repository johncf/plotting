#!/bin/python2
# source: http://fredrik-j.blogspot.in/2009/08/3d-visualization-of-complex-functions.html

import sys
sys.path.append('/opt/vtk6/lib/python2.7/site-packages')

import numpy as np
from mayavi import mlab
#from scipy import special as sp

# Use instead of arg for a continuous phase
def arg2(z):
    return np.sin(np.angle(z))

#f = lambda z: np.abs(sp.loggamma(z))
#f = lambda z: arg2(np.exp(z))
#f = lambda z: np.abs(sp.jv(3,z))
f = lambda z: arg2(np.cos(z))

X, Y = np.ogrid[-5:5:0.125, -5:5:0.125]
Z = X + 1j * Y
xn, yn = X.shape[0], Y.shape[1]
W = f(Z)

mlab.figure(size=(400, 300))
mlab.surf(W, colormap='gist_earth', warp_scale='auto', vmax=1.5)

mlab.show()
