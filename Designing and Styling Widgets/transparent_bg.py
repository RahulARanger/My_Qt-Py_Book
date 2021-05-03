from PySide2 import QtWidgets, QtCore, QtGui


class Test(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.check = QtWidgets.QPushButton(self)
        self.check.setText("check")
        self.check.move(100, 100)

    def paintEvent(self, event):
        # painter = QtGui.QPainter()
        #
        # painter.setBackgroundMode(QtCore.Qt.TransparentMode)
        # painter.drawRect(QtCore.QRect(self.x(), self.y(), self.width(), self.height()))
        pass

check = QtWidgets.QApplication([])
know = QtWidgets.QWidget()
know.setStyleSheet("background-color: orange;")
checking = Test(know)
checking.move(10, 10)
know.show()
check.exec_()

