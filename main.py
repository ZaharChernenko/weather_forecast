from ui_interface import Ui_MainWindow
from PyQt5 import QtWidgets

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    screen = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(screen)
    screen.show()

    sys.exit(app.exec())
