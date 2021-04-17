from PySide2 import QtWidgets, QtCore, QtGui


class Shape(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.brush = QtGui.QBrush()  # for inside
        self.pen = QtGui.QPen()  # for outline
        self.arrange()

    def arrange(self):
        self.brush.setStyle(QtCore.Qt.Dense1Pattern)
        self.brush.setColor(QtGui.QColor("orange"))

        self.pen.setColor(QtGui.QColor("#0078D7"))
        self.pen.setJoinStyle(QtCore.Qt.MiterJoin)
        self.pen.setWidth(6)
        self.pen.setCapStyle(QtCore.Qt.RoundCap)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setBrush(self.brush)
        painter.setPen(self.pen)

        painter.drawRect(QtCore.QRect(0, 0, self.width(), self.height()))


test = QtWidgets.QApplication([])
check = Shape()
check.show()
test.exec_()
