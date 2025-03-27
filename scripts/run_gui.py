import sys
from PyQt5.QtWidgets import QApplication
from src.gui.main_window import MainWindow  # Absolute import

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Test Spin Measurement")
    window.resize(600, 400)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()