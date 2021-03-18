from PyQt5 import QtWidgets, QtCore, QtGui


class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = QtWidgets.QWidget(windowTitle='QFileDialog')
        self.layout = QtWidgets.QHBoxLayout()
        self.window.setLayout(self.layout)
        self.select = QtWidgets.QPushButton(self.window, text='select any color', clicked=lambda x=True: print(
            QtWidgets.QColorDialog.getColor(QtGui.QColor('orange'), self.window, 'Select Any Color')))
        self.layout.addWidget(self.select)
        self.window.show()


test().exec()
