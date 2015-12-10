# Visualizations
"""Volume I Lab 3: Plotting with matplotlib
Derek Miller
15 September 2015
"""

# Add your import statements here.
import numpy as np
from matplotlib import pyplot as plt
from mayavi import mlab

# mayavi messes up numpy. In the command line, type 'export QT_API=pyqt' to fix.

# Problem 1
def curve():
    """Plot the curve 1/(x-1) on [-2,6]. Plot the two sides of the curve separately
    (still with a single call to plt.plot()) so that the graph looks discontinuous 
    at x = 1.
    """
    x1 = np.linspace(-2,.9999999)
    x2 = np.linspace(1.0000001,6)
    y1 = 1./(x1-1)
    y2 = 1./(x2-1)
    plt.plot(x1,y1,'m',x2,y2,'m',lw=6,ls='--')
    plt.ylim(-6,6)
    plt.show()

# Problem 2
def colormesh():
    """Plot the function f(x,y) = sin(x)sin(y)/(xy) on [-2*pi, 2*pi]x[-2*pi, 2*pi].
    Include the scale bar in your plot.
    """
    x = np.linspace(-2*np.pi,2*np.pi,1000) # values of x
    y = np.linspace(-2*np.pi,2*np.pi,1000) # values of y
    X,Y = np.meshgrid(x,y) # new X and Y of meshgrid data type
    f = (np.sin(X)*np.sin(Y))/(X*Y) # function of sin(X)*sin(Y)/(X*Y)
    plt.pcolormesh(X,Y,f,cmap='seismic') # plots heat map w/ seismic color scheme.
    plt.ylim(-2*np.pi,2*np.pi) # sets y-axis boundary
    plt.xlim(-2*np.pi,2*np.pi) # sets x-axis boundary
    plt.colorbar() # produces the scale bar
    plt.gca().set_aspect('equal') # makes the image square
    plt.show()

# Problem 3
def histogram():
    """Plot a histogram and a scatter plot of 50 random numbers chosen in the
    interval [0,1)
    """
    a = range(1,51) # x-axis
    b = np.random.rand(50) # 50 random numbers in [0,1)
    m = np.array([np.mean(b),np.mean(b)]) # mean value of b expressed as array of 2
    p = np.array([1,50]) # plot the mean along the x-axis
    
    # subplot 1: Histogram
    plt.subplot(1,2,1)
    plt.hist(b,bins=5)
    
    #subplot 2: Scatterplot
    plt.subplot(1,2,2)
    plt.scatter(a,b,s=50)
    plt.plot(p,m,'r')
    
    plt.show()
    
# Problem 4
def ripple():
    """Plot z = sin(10(x^2 + y^2))/10 on [-1,1]x[-1,1] using Mayavi."""

    X,Y = np.mgrid[-4:4:0.025,-4:4:0.025]
    Z = np.sin(10.*(X**2+Y**2))/10.
    mlab.surf(X,Y,Z,colormap='RdYlGn')
    mlab.show()
