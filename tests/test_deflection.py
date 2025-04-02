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

def test_xDeflection():