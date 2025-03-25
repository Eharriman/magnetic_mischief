import numpy as np
from typing import Tuple, Union
from numpy.typing import NDArray


class SpinState:

    def __init__(self, state_vector: Union[NDArray, Tuple[complex, complex]]):
        self.state_vector = np.array(state_vector, dtype=complex)
        self._normalize()
        self._pauli_matrices = {
            'z': np.array([[1, 0], [0, -1]], dtype=complex),
            'x': np.array([[0, 1], [1, 0]], dtype=complex),
            'y': np.array([[0, -1j], [1j, 0]], dtype=complex)
        }

    def measureSpin(self):
        # 1. Error check for appropriate Cartesian measurement
        # 2. Calculate eigenvalues/states for Pauli matrices
        # 3. Calculate spin measurement probabilities
        # 4. Check outcome after random measurement
        return None