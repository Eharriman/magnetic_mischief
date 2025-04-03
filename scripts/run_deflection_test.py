from src.visualization.deflection_plot import plotDeflection
from src.physics import Particle, Magnet, SPIN_UP, SPIN_DOWN

magnet = Magnet(gradient=0.5, axis='z')

particles = [Particle([0, 0, 0], [0, 0, 0], SPIN_UP), Particle([0, 0, 0], [0, 0, 0], SPIN_DOWN)]

fig = plotDeflection(particles, magnet, steps=30, dt=0.15)
fig.savefig('C:/Users/ethan/PycharmProjects/magnetic_mischief/tests/output/z_deflection_demo.png')
fig.show()
