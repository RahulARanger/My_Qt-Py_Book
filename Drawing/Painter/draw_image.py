from PyQt5 import QtWidgets, QtCore, QtGui
import pathlib


class Test(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.test = str(pathlib.Path(__file__).parent / "test.jpg")
