import numpy as np

class Magnet:
    def __int__(self, gradient: float, axis: str = 'z', length: float = 1.0):

        self.gradient = gradient
        self.axis = axis
        self.length = length
        self.axis_map = {'x':0, 'y':1, 'z':2}