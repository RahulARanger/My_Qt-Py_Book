from PySide2 import QtWidgets, QtGui, QtCore


class Test(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pen = QtGui.QPen()
        self.brush = QtGui.QBrush()
        self.arrange()

    def arrange(self):
        self.pen.setStyle(QtCore.Qt.DotLine)
        self.pen.setWidth(6)
        self.pen.setCapStyle(QtCore.Qt.RoundCap)
        self.pen.setJoinStyle(QtCore.Qt.RoundJoin)
        self.pen.setBrush(QtGui.QColor("blue"))

        self.brush.setStyle(QtCore.Qt.Dense6Pattern)
        self.brush.setColor(QtGui.QColor("orange"))

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        # this has to be dynamically created and its values must be assigned dynamically (every time its called)

        painter.setBrush(self.brush)
        painter.setPen(self.pen)
        painter.drawEllipse(QtCore.QPoint(100, 100), 60, 60)  # 60 and 60 are b and a of ellipse

        # ellipse becomes circle when b == a


check = QtWidgets.QApplication([])
note = Test()
note.show()
check.exec_()
