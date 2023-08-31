from WeatherWindow import WeatherWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    screen = QMainWindow()
    ui = WeatherWindow(screen)
    screen.show()

    sys.exit(app.exec())
