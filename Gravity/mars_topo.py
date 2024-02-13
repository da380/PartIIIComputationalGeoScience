import matplotlib.pyplot as plt
import pyshtools as pysh
from pyshtools import constants


def Topo(): 
    
    clm = pysh.datasets.Mars.GMM3()
    clm.set_omega(constants.Mars.omega.value) 
    a = constants.Mars.a.value
    b = constants.Mars.b.value
    f = constants.Mars.f.value
    u0 = constants.Mars.u0.value
    grav = clm.expand(lmax=95, a=a, f=f)
    mars_geoid = clm.geoid(u0, lmax=719)
    mars_geoid_ellipsoid = clm.geoid(u0, a=a, f=f, lmax=719)
    shape = pysh.datasets.Mars.MarsTopo719()
    shape_grid = shape.expand(grid='DH2')
    topo_grid = (shape_grid - mars_geoid.a - mars_geoid.geoid) / 1.e3
    topo_lm = topo_grid.expand(normalization = 'ortho')
    topo = 1000*topo_lm.expand()
    return topo
