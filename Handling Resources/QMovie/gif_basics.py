from PySide2 import QtGui, QtWidgets, QtCore


class Testing(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QtWidgets.QVBoxLayout())
        self.gif = QtWidgets.QLabel(self)
        rem = QtGui.QMovie('REM.gif')

        self.gif.setMovie(rem)
        self.gif.movie().start()
        self.layout().addWidget(self.gif)


test = QtWidgets.QApplication([])
note = Testing()
note.show()
test.exec_()
