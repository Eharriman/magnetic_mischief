from .widgets import StateSelector, MeasurementDisplay
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.state_selector = StateSelector()
        self.result_display = MeasurementDisplay()

        # Connect dropdown changes to update display
        self.state_selector.currentIndexChanged.connect(self._update_display)

        # Setup layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.state_selector)
        layout.addWidget(self.result_display)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Initialize display with first state
        self._update_display()

    def _update_display(self):
        # Display current state
        state = self.state_selector.getState()
        self.result_display.update_result(0, state)  # 0 = no measurement yet