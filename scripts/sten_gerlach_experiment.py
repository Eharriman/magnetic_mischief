from src.physics import Particle, Magnet, SPIN_UP, SPIN_DOWN

magnet = Magnet(gradient=0.5, axis='z')

particles = [Particle([0,0,0], [0,0,1], SPIN_UP), Particle([0,0,0], [0,0,1], SPIN_DOWN)]

