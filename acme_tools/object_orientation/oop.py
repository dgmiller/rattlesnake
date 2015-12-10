# name this file 'solutions.py'
"""Volume II Lab 2: Object Oriented Programming
Derek Miller
Jarvis
10 September 2015
"""

from Backpack import Backpack


# Problem 1: Modify the 'Backpack' class in 'Backpack.py'.


# Study the 'Knapsack' class in 'Backpack.py'. You should be able to create a 
#   Knapsack object after finishing problem 1.


# Problem 2: Write a 'Jetpack' class that inherits from the 'Backpack' class.
class Jetpack(Backpack):
    """A Jetpack object class. Inherits from the Backpack class.
    
    Attributes:
        color (str): the color of the jetpack.
        contents (list): the contents of the jetpack.
        name (str): the label for the jetpack.
        max_size (int): total object capacity of jetpack.
        fuel (int): total fuel capacity of jetpack.
    """
    def __init__(self, color='silver', name='jetpack', max_size=2, fuel=10):
        """Constructor for a jetpack object that inherits from 'backpack'.
        Overrides some attributes of the backpack class.
        
        Inputs:
            color (str, opt): the jetpack color. Defaults to 'silver'.
            name (str): the jetpack label. Defaults to 'jetpack'.
            max_size (int): total object capacity of jetpack. Defaults to 2.
            fuel (int): total fuel left in jetpack. Defaults to 10.

        Returns:
            A jetpack object with no contents and a full tank.
        """

        Backpack.__init__(self, color, name, max_size)
        self.fuel = fuel

    def fly(self, fuel):
        if fuel <= self.fuel:
            self.fuel -= fuel
        else:
            print "Not enough fuel!"

    def dump(self):
        """Removes all contents and fuel from the jetpack."""
        self.contents = []
        self.fuel = 0



# Problem 3: write __str__ and __eq__ for the 'Backpack' class in 'Backpack.py'


# Problem 4: Write a ComplexNumber class.
class ComplexNumber(object):
    """A Complex number object class. Has a real and imaginary part.
    
    Attributes:
        real (float): the real part of the complex number.
        imag (float): the imaginary part of the complex number.
    
    """
    def __init__(self, real, imag):
        """Constructor for a complex number.
        
        Input:
            real (float): the real part of the complex number. 
            imag (float): the imaginary part of the complex number. 

        Output:
           Returns a complex number object.
        """

        self.real = float(real)
        self.imag = float(imag)


    def conjugate(self):
        """Produces the complex conjugate of a complex number object."""
        new_imag = self.imag * (-1)
        return ComplexNumber(self.real,new_imag)

    def norm(self):
        """Returns the magnitude of a complex number object."""
        return (self.real**2 + self.imag**2)**.5

    def __add__(self, other):
        """Returns the sum of a complex number object."""
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        return ComplexNumber(new_real,new_imag)

    def __sub__(self, other):
        """Returns the difference between two complex number objects."""
        new_real = self.real - other.real
        new_imag = self.imag - other.imag
        return ComplexNumber(new_real,new_imag)

    def __mul__(self, other):
        """Returns the product of two complex number objects."""
        new_real = (self.real * other.real) - (self.imag * other.imag)
        new_imag = (other.real * self.imag) + (self.real * other.imag)
        return ComplexNumber(new_real,new_imag)

    def __div__(self, other):
        """Returns the quotient of two complex number objects."""
        new_real = ((self.real * other.real) + (self.imag * other.imag)) / (other.real ** 2 + other.imag ** 2)
        new_imag = ((self.imag * other.real) - (self.real * other.imag)) / (other.real ** 2 + other.imag ** 2)
        return ComplexNumber(new_real,new_imag)


# =============================== END OF FILE =============================== #

