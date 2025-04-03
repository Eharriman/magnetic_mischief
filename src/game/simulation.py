from src.physics import Particle, Magnet
import numpy as np

class ParticleSimulator:
    def __init__(self):
        self.particles = []
        self.magnets = []
        self.time = 0.0

    def addParticle(self, position, velocity, spin_state):
        self.particles.append(Particle(position, velocity, spin_state))

    def addMagnet(self, gradient, axis, length):
        self.magnets.append(Magnet(gradient, axis, length))

    def update(self, dt):
        for magnet in self.magnets:
            for particle in self.particles:
                magnet.deflect(particle, dt)
        self.time += dt
