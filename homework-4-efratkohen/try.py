from hw4_q1 import *
import numpy as np
import matplotlib.pyplot as plt


n=10
thresh=50.0
xlims= np.array([-2, 1])
nx=1500
ylims= np.array([-1.5, 1.5])
ny=1500

x_arr=build_arr(xlims,nx)
y_arr=build_arr(ylims,ny)
i=0
z1=complex(0,0)
z2=complex(-2,-1.5)
while i<=n:
    z1=z1**2+z2
print(z1)

# x_arr=mandel(n,thresh,xlims,nx,ylims,ny)
# print(x_arr)