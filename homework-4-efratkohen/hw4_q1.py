import numpy as np
import matplotlib.pyplot as plt


def mandel(
    n: int,
    thresh: float = 50.0,
    xlims: np.ndarray = np.array([-2, 1]),
    nx: int = 1500,
    ylims: np.ndarray = np.array([-1.5, 1.5]),
    ny: int = 1500,
) -> np.ndarray:
    """Computes the Mandelbrot fractal on some given set of numbers.

    Parameters
    ----------
    n : int
        Number of iterations.
    thresh : float
        Threshold which decides if a number is a part of the set.
    xlims, ylims : np.ndarray
        Limits for the computation of the fractal.
    nx, ny : int
        Number of points between xlims.min() and xlims.max() to calculate the set on.

    Returns
    -------
    img : np.ndarray
        A binary image with a value of 1 if the point belongs to the set.
        The shape of the resulting image is (nx, ny).
    """
    x_arr=build_arr(xlims,nx)
    y_arr=build_arr(ylims,ny)
    c_arr=build_complex_arr(x_arr,y_arr,nx,ny)
    mandel_arr=mandel_fig(nx,ny,c_arr,thresh,n)
    extent = (xlims[0], xlims[1], ylims[0], ylims[1])
    plt.imshow(mandel_arr,cmap='gray' ,extent=extent)
    plt.show()
    return mandel_arr

def build_arr(lims, n):
    """array of x values in the xlims limits and nx points"""
    sep=(lims[1]-lims[0])/n
    arr=np.arange(lims[0],(lims[1]+sep),sep)
    return arr

def build_complex_arr(x_arr,y_arr,lx,ly):
    """array of complex number values in the x,y limits"""
    c_arr=np.zeros((lx,ly),dtype=complex)
    i=0
    j=0
    while i<lx:
        while j<ly:
            c_arr[i,j]=complex(x_arr[i],y_arr[j])
            j=j+1
        i=i+1
        j=0
    return c_arr

def mandel_iter(c: complex, thresh: float, n: int):
    """find out if a complex number C is a mandel kind, return true if so"""
    i=0
    z1=complex(0,0)
    while i<=n:
        z1=z1**2+c
        i=i+1
    if abs(z1)<thresh:
        return 1
    else:
        return 0
def mandel_fig(nx,ny,c_arr,thresh: float, n: int):
    """build array with zeroes and ones to create a mandelbrot fig"""
    mandel_arr=np.zeros((nx,ny))
    i=0
    j=0
    while i<nx:
        while j<ny:
            mandel_arr[i,j]=mandel_iter(c_arr[i,j],thresh,n)
            j=j+1
        i=i+1
        j=0
    return mandel_arr.T


