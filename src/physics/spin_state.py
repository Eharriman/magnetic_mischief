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
    def _normalize(self) -> None:
        normalized_state_vector = np.linalg.norm(self.state_vector)

        if normalized_state_vector == 0:
            raise ValueError("Zero state vector is aphysical!!!")
        # Normalize state vector --> divide by the norm
        self.state_vector /= normalized_state_vector

    def measureSpin(self, axis) -> Tuple[float, 'SpinState']:
        # 1. Error check for appropriate Cartesian measurement
        # 2. Calculate eigenvalues/states for Pauli matrices
        # 3. Calculate spin measurement probabilities
        # 4. Check outcome after random measurement
        if axis not in self._pauli_matrices:
            raise ValueError("Not a valid measurement axis. Use Cartesian: x,y,z")

        eigen_values, eigen_states = np.linalg.eig(self._pauli_matrices[axis])

        probabilities = [
            # Calculate probability of ith eigenstate of Pauli Matrix
            abs(np.vdot(eigen_states[:, i], self.state_vector))**2
            for i in range(2)
        ]

        measurement_result = np.random.choice([-1, 1], p = probabilities)

        if measurement_result == 1:
            state_index = 0
        else:
            state_index = 1

        curr_state = eigen_states[:, state_index]

        return measurement_result, SpinState(curr_state)
        #return None

    def __repr__(self) -> str:
        spin_up, spin_down = self.state_vector
        return f"{spin_up:.2f}|↑⟩ + {spin_down:.2f}|↓⟩"


#state1 = SpinState([1, 1])
#state1 = SpinState([1, 0])

#measurement, new_state = state1.measureSpin('z')

"""
for i in range(5):
    print(f"Experiment {i}")
    measurement_z, new_state1 = state1.measureSpin('z')
    print(f"The measurement of z-spin is: {measurement_z}. The new state is {new_state1}")
    measurement_y, new_state2 = new_state1.measureSpin('y')
    print(f"The measurement of y-spin is: {measurement_y}. The new state is {new_state2}")
    measurement_z2, new_state3 = new_state2.measureSpin('z')
    print(f"The measurement of z-spin AGAIN is: {measurement_z2}. The new state is {new_state3}")
"""