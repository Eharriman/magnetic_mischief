from .spin_state import SpinState
import numpy as np

class Partcile:
    def __int__(self, position, velocity, spin_state):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.spin_state = spin_state

    def magnetic_moment(self) -> np.ndarray:
        #Returns magnetic moment for particle
        sz = self.spin_state.measure('z')[0]
        # g factor?
        return np.array([0, 0, sz])
