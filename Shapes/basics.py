from PySide2 import QtWidgets, QtCore, QtGui


class test(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paintEvent(self, event):
        print(event)
        check_this = QtGui.QPainter(self)
        check_this.setPen(QtGui.QColor("orange"))
        check_this.drawRect(QtCore.QRect(10, 20, 100, 100))
        return super().paintEvent(event)


check = QtWidgets.QApplication([])
testing = test()
testing.show()
check.exec_()
