import numpy as np
import pytest
from src.physics.spin_state import SpinState, SPIN_UP, SPIN_DOWN, SPIN_X_DOWN, SPIN_X_UP

class TestSpinState:
    def test_z_measurement(self):
        result, collapsed_state = SPIN_UP.measureSpin('z')
        assert np.isclose(result, SpinState.HALF_HBAR)
        assert collapsed_state == SPIN_UP