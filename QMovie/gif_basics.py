from PyQt5 import QtGui, QtWidgets


class Testing(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QtWidgets.QVBoxLayout())
        self.gif = QtWidgets.QLabel(self)
        self.gif.setMovie(QtGui.QMovie('REM.gif'))
        self.gif.movie().start()
        self.layout().addWidget(self.gif)


test = QtWidgets.QApplication([])
note = Testing()
note.show()
test.exec()
