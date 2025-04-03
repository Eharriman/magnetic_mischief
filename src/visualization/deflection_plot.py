import matplotlib.pyplot as plt
import numpy as np
from IPython.core.pylabtools import figsize

from src.physics import Particle, Magnet, SPIN_UP, SPIN_DOWN


def plotDeflection(particles, magnet, steps=20, dt=0.1):
    fig, ax = plt.subplots(figsize=(10, 5))

    for particle in particles:
        trajectory = []
        for _ in range(steps):
            magnet.deflect(particle, dt)
            trajectory.append(particle.position.copy())
        trajectory = np.array(trajectory)
        ax.plot(trajectory[:,2], label=particle.spin_state)

    ax.set_title(f"Spin Deflection Plot (gradient={magnet.gradient})")
    ax.set_xlabel("Time")
    ax.set_ylabel(f"{magnet.axis.upper()}-Position")
    ax.legend()
    ax.grid(True)
    return fig
