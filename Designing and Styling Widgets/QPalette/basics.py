from PyQt5 import QtCore, QtGui, QtWidgets


class Test(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        modify = self.palette()
        modify.setColor(QtGui.QPalette.Window, QtGui.QColor("orange"))
        self.setPalette(modify)
        self.check = QtWidgets.QPushButton(self)
        self.check.setText("checking")
        self.check.move(10, 10)


note = QtWidgets.QApplication([])
check = Test()
check.show()
note.exec_()
