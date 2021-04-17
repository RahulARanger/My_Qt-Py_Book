from PySide2 import QtWidgets, QtGui


class Test(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Checking")
        self.setToolTip("Testing")
        self.setStyleSheet("""QToolTip{  border: 2px solid darkkhaki;
    padding: 5px;
    border-radius: 3px;
    opacity: 200;}""")


check = QtWidgets.QApplication([])

print(check)
display = QtWidgets.QWidget()
display.setToolTip("This is plain")
mode = Test(display)
mode.move(100, 100)
display.show()
check.exec_()
