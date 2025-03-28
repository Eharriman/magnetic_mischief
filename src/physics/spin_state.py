import numpy as np
from typing import Tuple, Union
from numpy.typing import NDArray


class SpinState:

    # Physical constants
    HALF_HBAR = 0.5

    def __init__(self, state_vector: Union[NDArray, Tuple[complex, complex]]):
        self.state_vector = np.array(state_vector, dtype=complex)
        if len(self.state_vector) != 2:
            raise ValueError("Current model only permits spin-1/2. Need 2D vector")
        self._normalize()

    def _normalize(self) -> None:
        norm_state_vector = np.linalg.norm(self.state_vector)
        self.state_vector /= norm_state_vector

    def measureSpin(self, axis) -> Tuple[float, 'SpinState']:
        # 1. Error check for appropriate Cartesian measurement
        # 2. Calculate eigenvalues/states for Pauli matrices
        # 3. Calculate spin measurement probabilities
        # 4. Check outcome after random measurement
        """if axis not in self._pauli_matrices:
            raise ValueError("Not a valid measurement axis. Use Cartesian: x,y,z")"""

        eigen_values, eigen_states = self._getEigenbasis(axis)
        #eigen_values, eigen_states = np.linalg.eig(self._pauli_matrices[axis])
        probabilities = self._getProbabilities(eigen_states)

        """probabilities = [
            # Calculate probability of ith eigenstate of Pauli Matrix
            abs(np.vdot(eigen_states[:, i], self.state_vector))**2
            for i in range(2)
        ]"""

        outcome_index = np.random.choice([0,1], p=probabilities)
        measurement_result = eigen_values[outcome_index]
        new_state = eigen_states[:, outcome_index]

        """measurement_result = np.random.choice([-1, 1], p = probabilities)

        if measurement_result == 1:
            state_index = 0
        else:
            state_index = 1

        curr_state = eigen_states[:, state_index]

        return measurement_result, SpinState(curr_state)
        #return None"""

        return measurement_result, SpinState(new_state)

    def _getEigenbasis(self, axis: str) -> Tuple[NDArray, NDArray]:
        if axis == 'z':
            return (
                np.array([self.HALF_HBAR, -self.HALF_HBAR]),
                np.array([[1, 0], [0, 1]], dtype=complex)  # |↑⟩, |↓⟩
            )
        elif axis == 'x':
            sqrt2 = np.sqrt(2)
            return (
                np.array([self.HALF_HBAR, -self.HALF_HBAR]),
                np.array([[1 / sqrt2, 1 / sqrt2],
                          [1 / sqrt2, -1 / sqrt2]], dtype=complex)  # |→⟩, |←⟩
            )
        elif axis == 'y':
            sqrt2 = np.sqrt(2)
            return (
                np.array([self.HALF_HBAR, -self.HALF_HBAR]),
                np.array([[1 / sqrt2, 1 / sqrt2],
                          [1j / sqrt2, -1j / sqrt2]], dtype=complex)  # |⊙⟩, |⊗⟩
            )
        else:
            raise ValueError("Not a valid measurement axis. Use Cartesian: x,y,z")

    def _getProbabilities(self, eigen_states: NDArray) -> NDArray:
        return np.array([
            abs(np.vdot(eigen_states[:, i], self.state_vector)) ** 2
            for i in range(2)
        ])

    def bloch_coordinates(self) -> Tuple[float, float, float]:
        a, b = self.state_vector
        x = 2 * (a.conj() * b).real
        y = 2 * (a.conj() * b).imag
        z = abs(a)**2 - abs(b)**2
        return x, y, z

    def __repr__(self) -> str:
        a, b = self.state_vector
        return f"{a.real:.2f}|↑⟩ + {b.real:.2f}|↓⟩"


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