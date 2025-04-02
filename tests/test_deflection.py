import numpy as np
import matplotlib.pyplot as plt
from src.physics import Particle, Magnet, SPIN_UP, SPIN_DOWN

def test_zDeflection():
    magnet = Magnet(gradient=0.5, axis='z')

    particles = [Particle([0, 0, 0], [0, 0, 0], SPIN_UP), Particle([0, 0, 0], [0, 0, 0], SPIN_DOWN)]

    positions = {'up': [], 'down': []}

    for _ in range(20):
        for particle in particles:
            magnet.deflect(particle, dt=0.1)
            positions['up'].append(particles[0].position[2])
            positions['down'].append(particles[1].position[2])

    final_sep = positions['up'][-1] - positions['down'][-1]
    assert np.isclose(final_sep, 2.0, rtol=0.05)

    # Visualization
    plt.figure(figsize=(10, 6))
    plt.plot(positions['up'], label='|↑⟩', color='blue')
    plt.plot(positions['down'], label='|↓⟩', color='red')
    plt.title("Z-Axis Stern-Gerlach Deflection")
    plt.xlabel("Time steps (dt=0.1)")
    plt.ylabel("Z Position")
    plt.legend()
    plt.grid(True)
    plt.savefig('tests/output/z_deflection.png')
    plt.close()

def test_xDeflection():