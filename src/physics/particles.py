#from .spin_state import SpinState
from src.physics import SpinState
import numpy as np

class Particle:
    def __init__(self, position, velocity, spin_state: SpinState):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.spin_state = spin_state
        self.g = 2  # g-factor (electron)
        self.hbar = 1
        self.mass = 1

    def magneticMoment(self) -> np.ndarray:
        #Returns magnetic moment for particle
        sz = self.spin_state.measureSpin('z')[0]
        # g factor?
        return np.array([0, 0, sz * self.g])
