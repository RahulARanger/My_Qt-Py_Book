from PyQt5 import QtWidgets, QtGui


class test(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        print("bye")
        return super().closeEvent(a0)


testing = QtWidgets.QApplication([])
store = test()
store.show()
testing.exec()
