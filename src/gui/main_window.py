from .widgets import StateSelector, MeasurementDisplay, MeasurementButton
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.state_selector = StateSelector()
        self.result_display = MeasurementDisplay()
        self.measure_button = MeasurementButton()

        # Connect dropdown changes to update display
        self.state_selector.currentIndexChanged.connect(self._update_display)
        self.measure_button.clicked.connect(self._run_measurement)

        # Setup layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.state_selector)
        layout.addWidget(self.result_display)
        layout.addWidget(self.measure_button)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Initialize display with first state
        self._update_display()
        self.setWindowTitle("Quantum Spin Simulator")
        self.resize(400, 300)

    def _update_display(self):
        # Display current state
        state = self.state_selector.getState()
        self.result_display.update_result(0, state)  # 0 = no measurement yet

    def _run_measurement(self):
        # Perform spin measurement
        state = self.state_selector.getState()
        outcome, new_state = state.measureSpin('z')  # Use your physics!
        self.result_display.update_result(outcome, new_state)