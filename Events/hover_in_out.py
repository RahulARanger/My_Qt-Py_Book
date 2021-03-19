from PyQt5 import QtWidgets, QtCore, QtGui


class Sample(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    def enterEvent(self, a0: QtCore.QEvent) -> None:
        print("you came inside")
        # sorry for being horny
        return super().enterEvent(a0)

    def leaveEvent(self, a0: QtGui.QCloseEvent) -> None:
        print("you came out")
        return super().leaveEvent(a0)


class Test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.testing = Sample()
        self.testing.show()


testing = Test()
testing.exec()
