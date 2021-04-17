from PySide2 import QtWidgets, QtGui


class Test(QtWidgets.QPushButton):
    def __init__(self):
        super().__init__()
        self.setText("Test")
        print(self.palette())  # this is the predefined palette



check = QtWidgets.QApplication([])
mode = Test()
mode.show()
check.exec_()
