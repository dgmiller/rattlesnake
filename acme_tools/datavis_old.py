#Implement this function

from matplotlib import pyplot as plt
import numpy as np
from numpy.random import normal
from scipy.misc import comb

def problemOne():
    '''
    Order and plot the data as a horizontal bar chart.
    '''
    male = np.array([179.2,160.0,177.8,178.9,178,176,172.5,165.6,170.8,183.2,182.4,164,163.6,175.4,174,176.1,165.7])
    female = np.array([167.6,142.2,164.5,165.3,165,164,158,154.9,157.4,168.4,168,151,151.4,164,158.9,162.1,155.2])
    country = 'Austria', 'Bolivia', 'England', 'Finland', 'Germany', 'Hungary', 'Japan','North Korea', 'South Korea', 'Montenegro', 'Norway', 'Peru','Sri Lanka', 'Switzerland', 'Turkey', 'U.S.', 'Vietnam'
    pos = np.arange(17)+.5
    plt.subplot(2,1,1)
    plt.title('Male Avg Height')
    plt.barh(pos, np.sort(male), align='center', color='b')
    plt.yticks(pos, country[::-1])
    plt.subplot(2,1,2)
    plt.title('Female Avg Height')
    plt.barh(pos, np.sort(female), align='center', color='r')
    plt.yticks(pos, country[::-1])
    plt.show()

# Implement this function
def problemTwo():
    '''
    Plot some histograms with white reference lines.  Do this for 20 bins,
    10 bins, 5 bins, and 3 bins
    '''
    normal_numbers = normal(size=1000)
    plt.subplot(2,2,1)
    plt.hist(normal_numbers, 20)
    plt.grid(True, color='w', linestyle='-')
    plt.subplot(2,2,2)
    plt.hist(normal_numbers, 10)
    plt.grid(True, color='w', linestyle='-')
    plt.subplot(2,2,3)
    plt.hist(normal_numbers, 5)
    plt.grid(True, color='w', linestyle='-')
    plt.subplot(2,2,4)
    plt.hist(normal_numbers, 3)
    plt.grid(True, color='w', linestyle='-')
    plt.show()

# Implement this function
def problemThree():
    '''
    Plot y = x^2 * sin(x) using 1000 data points and x in [0,100]
    '''
    x = np.linspace(0,100,1000)
    y = x**2 * np.sin(x)
    plt.plot(x,y,linewidth=2.0)
    plt.show()

# Implement this function
def problemFour():
    '''
    Plot a scatter plot of the average heights of men against women
    using the data from problem 1.
    '''
    male = np.array([179.2,160.0,177.8,178.9,178,176,172.5,165.6,170.8,183.2,182.4,164,163.6,175.4,174,176.1,165.7])
    female = np.array([167.6,142.2,164.5,165.3,165,164,158,154.9,157.4,168.4,168,151,151.4,164,158.9,162.1,155.2])
    plt.plot(female,male,'ro')
    plt.show()
    
# Implement this function
def problemFive():
    '''
    Plot a contour map of z = sin(x) + sin(y) where x is in [0,12*pi] and
    y is in [0,12*pi]
    '''
    x = np.linspace(0,12*np.pi,400)
    y = np.linspace(0,12*np.pi,400)
    z = np.sin(x) + np.sin(y)
    X, Y = np.meshgrid(x,y)
    Z = np.sin(X) + np.sin(Y)
    CS = plt.contourf(X,Y,Z,cmap='seismic')
    plt.colorbar(CS)
    plt.show()
    
# Implement this function
def problemSix():
    '''
    Plot each data set.
    '''
    dataI = np.array([[10,8.04],[8.,6.95],[13.,7.58],[9,8.81],[11.,8.33],[14.,9.96],[6.,7.24],[4.,4.26],[12.,10.84],[7.,4.82],[5.,5.68]])
    dataII = np.array([[10,9.14],[8.,8.14],[13.,8.74],[9,8.77],[11.,9.26],[14.,8.10],[6.,6.13],[4.,3.10],[12.,9.13],[7.,7.26],[5.,4.74]])
    dataIII = np.array([[10,7.46],[8.,6.77],[13.,12.74],[9,7.11],[11.,7.81],[14.,8.84],[6.,6.08],[4.,5.39],[12.,8.15],[7.,6.42],[5.,5.73]])
    dataIV = np.array([[8.,6.58],[8.,5.76],[8.,7.71],[8.,8.84],[8.,8.47],[8.,7.04],[8.,5.25],[19.,12.50],[8.,5.56],[8.,7.91],[8.,6.89]])
    plt.subplot(2,2,1)
    plt.plot(dataI[:,0],dataI[:,1],'ro')
    plt.axis([0,20,0,15])
    plt.subplot(2,2,2)
    plt.plot(dataII[:,0],dataII[:,1], 'bo')
    plt.axis([0,20,0,15])
    plt.subplot(2,2,3)
    plt.plot(dataIII[:,0],dataIII[:,1], 'go')
    plt.axis([0,20,0,15])
    plt.subplot(2,2,4)
    plt.plot(dataIV[:,0],dataIV[:,1], 'yo')
    plt.axis([0,20,0,15])
    plt.show()

# Implement this function
def problemSeven():
    '''
    Change the surface to a heatmap or a contour plot.  Return a string
    of the benefits of each type of visualization.
    '''
    x = np.linspace(-2*np.pi,2*np.pi,num=400)
    y = np.linspace(-2*np.pi,2*np.pi,num=400)
    X,Y = np.meshgrid(x,y)
    Z = np.exp(np.cos(np.sqrt(X**2 + Y**2)))
    CS = plt.contourf(X,Y,Z,cmap='autumn')
    plt.colorbar(CS)
    plt.show()
    answer = "3D Viz: good for modeling the physical world\nContour Map: good for visualizing a high variance third variable over a large range of the other two variables\nHeat Map: good for visualizing general flux of one variable over a stable grid"

# Implement this function
def problemEight():
    '''
    Plot y = x^2 * sin(x) where x is in [0,100] and adjust to y limit to be
    [-10^k,10^k] for k = 0,1,2,3,4.
    '''
    x = np.linspace(0,100,1000)
    y = x**2 * np.sin(x)
    for k in range(5):
        plt.subplot(3,2,k+1)
        plt.plot(x,y,linewidth=2.0)
        plt.ylim(-10.**k,10**k)
    plt.show()


# Implement this function
def problemNine():
    '''
    Simplify one of your previous graphs.
    '''
    x = np.linspace(0,12*np.pi,400)
    y = np.linspace(0,12*np.pi,400)
    z = np.sin(x) + np.sin(y)
    X, Y = np.meshgrid(x,y)
    Z = np.sin(X) + np.sin(Y)
    CS = plt.contourf(X,Y,Z,cmap='bone')
    axis = plt.gca()
    axis.spines['right'].set_visible(False)
    axis.spines['top'].set_visible(False)
    plt.xlim(0,31)
    plt.ylim(0,31)
    plt.xticks(np.arange(0,31,10))
    plt.yticks(np.arange(0,31,10))
    plt.colorbar(CS)
    plt.show()
   

# Implement this function
def problemTen():
    '''
    Plot the Bernstein polynomials for v,n in [0,3] as small multiples
    and as the cluttered version.
    '''
    x = np.linspace(0,1,1000)
    i = 1
    for n in range(1,5):
        for v in range(n+1):
            plt.subplot(4,4,i)
            Bernstein = comb(n,v) * np.power(x,v) * np.power(1-x,n-v)
            plt.plot(x,Bernstein)
            i += 1
    plt.show()


problemSeven()
