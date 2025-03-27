from .widgets import StateSelector, MeasurementDisplay
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.state_selector = StateSelector()
        self.result_display = MeasurementDisplay()

        # Connect signals (example: update display when state changes)
        self.state_selector.currentIndexChanged.connect(self._on_state_change)

        # Setup layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.state_selector)
        layout.addWidget(self.result_display)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def _on_state_change(self):
        """Demo: Update display when dropdown changes."""
        state = self.state_selector.getState()
        self.result_display.update_result(1, state)  # Fake outcome=1 for testing