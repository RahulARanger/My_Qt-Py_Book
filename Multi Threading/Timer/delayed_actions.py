from PySide2 import QtCore, QtWidgets


class Test(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.setText("wait for it")
        QtCore.QTimer.singleShot(3000, self.set_that)

    def set_that(self):
        self.setText("Booooooooooooooooooooooooo")  # displayed after 3 seconds


check = QtWidgets.QApplication([])
test = Test()
test.show()
check.exec_()
