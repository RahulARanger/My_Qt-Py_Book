from PySide2 import QtWidgets, QtCore, QtGui
import pathlib


class Test(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.test = str(pathlib.Path(__file__).parent / "test.jpg")


test = QtWidgets.QApplication([])
checking = Test()
checking.show()
test.exec_()
