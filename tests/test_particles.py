import numpy as np
from src.physics import Particle, SPIN_UP

def testmagneticMoment():
    particle = Particle(
        position=[0, 0, 0],
        velocity=[0, 0, 0],
        spin_state=SPIN_UP
    )
    expected_moment = np.array([0, 0, 1])  # g=2 * (hbar=1/2) = 1
    assert np.allclose(particle.magneticMoment(), expected_moment)