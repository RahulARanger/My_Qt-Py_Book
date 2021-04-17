from PySide2 import QtCore, QtGui, QtWidgets


class Board(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pen = QtGui.QPen()
        self.points = []
        self.draw = True

        self.arrange()

    def arrange(self):
        self.pen.setColor(QtGui.QColor("orange"))
        self.pen.setWidth(20)

    def paintEvent(self, event):
        print(self.points)
        painter = QtGui.QPainter(self)
        painter.setPen(self.pen)
        painter.drawPoints(self.points)

    def mouseDoubleClickEvent(self, event):
        self.draw = False

        if event.pos() in self.points:
            self.points.remove(event.pos())
        self.update()
        return super().mouseDoubleClickEvent(event)

    def mousePressEvent(self, event):
        if not self.draw:
            self.draw = True
            return super().mousePressEvent(event)

        if event.pos() not in self.points:
            self.points.append(event.pos())
        self.update()
        return super().mousePressEvent(event)


test = QtWidgets.QApplication([])
testing = Board()
testing.show()
test.exec_()
