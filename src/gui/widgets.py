# src/gui/widgets.py
from PyQt5.QtWidgets import QComboBox, QLabel, QSlider
from PyQt5.QtCore import Qt
from src.physics.spin_state import SpinState
import numpy as np


class StateSelector(QComboBox):
    def __init__(self):
        super().__init__()
        self.addItems([
            "|↑⟩ (Spin Up)",
            "|↓⟩ (Spin Down)",
            "|→⟩ (X Up)",
            "|←⟩ (X Down)"
        ])

    def getState(self) -> SpinState:
        # drop down selection -> spin state
        return {
            0: SpinState([1, 0]),  # |↑⟩
            1: SpinState([0, 1]),  # |↓⟩
            2: SpinState([1 / np.sqrt(2), 1 / np.sqrt(2)]),  # |→⟩
            3: SpinState([1 / np.sqrt(2), -1 / np.sqrt(2)])  # |←⟩
        }[self.currentIndex()]


class MeasurementDisplay(QLabel):
    def __init__(self):
        super().__init__("Results will appear here")
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
            font-size: 16px;
            font-weight: bold;
            padding: 10px;
        """)

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