import numpy as np
# Old import
# from .particles import Particle
from src.physics import Particle

class Magnet:
    def __init__(self, gradient: float, axis: str = 'z', length: float = 1.0):

        self.gradient = gradient
        self.axis = axis
        self.length = length
        self.axis_map = {'x':0, 'y':1, 'z':2}

    def deflect(self, particle, dt: float) -> None:

        mu = particle.magneticMoment()
        force = np.zeros(3)
        force[self.axis_map[self.axis]] = mu[self.axis_map[self.axis]] * self.gradient

        # Position and velocity
        particle.velocity += (force / particle.mass) * dt
        particle.position += particle.velocity * dt