import numpy as np
from .particles import Particle

class Magnet:
    def __int__(self, gradient: float, axis: str = 'z', length: float = 1.0):

        self.gradient = gradient
        self.axis = axis
        self.length = length
        self.axis_map = {'x':0, 'y':1, 'z':2}

    def deflect(self, particle, dt: float) -> None:

        #mu = particle.magnetic