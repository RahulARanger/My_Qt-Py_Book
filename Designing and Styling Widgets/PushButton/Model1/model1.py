from PySide2 import QtWidgets, QtCore, QtGui


class Sample(QtWidgets.QProxyStyle):  # QtWidgets.QCommonStyle will
    # implement the same design irrespective of the platform
    def __init__(self):
        super().__init__()


class Test(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Model1")
        self.setStyle(Sample())


checking = QtWidgets.QApplication([])
check = QtWidgets.QWidget()
display = Test(check)
display.move(100, 100)
normal = QtWidgets.QPushButton(check)
normal.move(50, 20)
normal.setText("Normal")
check.show()
checking.exec_()
