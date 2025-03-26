from PyQt5.QtWidgets import QComboBox
from src.physics.spin_state import SpinState

class StateSelector(QComboBox):
    def __int__(self):
        super().__init__()
        self.addItems(["|↑⟩", "|↓⟩", "|→⟩"])

    def getState(selfself) -> SpinState:
        # Dropdown selection for state building
        text = self.currentText()
        if text == "|↑⟩":
            return SpinState([1, 0])
        elif text == "|→⟩":
            return SpinState([1, 1])
