from PySide2 import QtWidgets, QtCore, QtGui


class Test(QtWidgets.QTextEdit):
    pass


sample = QtWidgets.QApplication([])


if __name__ == "__main__":
    test = Test()
    test.show()
    sample.exec_()
