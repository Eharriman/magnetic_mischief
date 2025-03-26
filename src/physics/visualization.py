import numpy as np
import matplotlib.pyplot as plt
from spin_state import SpinState

def visualize_block_sphere(state: SpinState):
    bloch_sphere = plt.figure()
    axis = bloch_sphere.add_subplot(111, projection='3d')
    x, y, z = state.bloch_coordinates()
    axis.quiver(0, 0, 0, x, y, z, color='r')
    axis.set_title(f"State: {state}")
    plt.show()

state1 = SpinState([1,1])
state2 = SpinState([1,0])
visualize_block_sphere(state2)