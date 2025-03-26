from src.physics.spin_state import SpinState
from collections import Counter

state = SpinState([1,1,])
results = [state.measureSpin('z')[0] for i in range(1000)]

print("Measurement results:")
print(f"↑ (1): {results.count(1)} times")
print(f"↓ (-1): {results.count(-1)} times")
print(f"Ratio: {results.count(1)/len(results):.3f}")