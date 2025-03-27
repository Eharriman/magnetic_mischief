from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox, QLabel, QSlider
from src.physics.spin_state import SpinState

class StateSelector(QComboBox):
    def __int__(self):
        super().__init__()
        self.addItems([
            "|↑⟩ (Spin Up)",
            "|↓⟩ (Spin Down)",
            "|→⟩ (X Up)",
            "|←⟩ (X Down)"
        ])

    def getState(selfself) -> SpinState:
        """Convert GUI selection to a SpinState object."""
        return {
            0: SPIN_UP,
            1: SPIN_DOWN,
            2: SPIN_X_UP,
            3: SpinState([1/np.sqrt(2), -1/np.sqrt(2)])  # |←⟩
        }[self.currentIndex()]


class MeasurementDisplay(QLabel):
    def __init__(self):
        super().__init__("Results will appear here")
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("font-size: 16px;")

    def update_result(self, outcome: int, state: SpinState):
        arrow = "↑" if outcome == 1 else "↓"
        self.setText(
            f"Outcome: {arrow}\n"
            f"New State: {state}"
        )

class AnimationSpeedSlider(QSlider):
    def __init__(self):
        super().__init__(Qt.Horizontal)
        self.setRange(1, 10)
        self.setValue(5)
        self.setTickInterval(1)