from PyQt5 import QtWidgets, QtGui


# Return Type will be that of QtGui.QFont() and the refer this docs:
# https://doc.qt.io/qtforpython/PySide6/QtGui/QFont.html

class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = QtWidgets.QWidget(windowTitle='QFileDialog')
        self.layout = QtWidgets.QHBoxLayout()
        self.window.setLayout(self.layout)

        def f1(*args):
            result = QtWidgets.QFontDialog.getFont(QtGui.QFont('Arial', 18), self.window,
                                                   'Select any Font for the Button')
            if result[-1]:
                self.bt.setFont(result[0])

        self.bt = QtWidgets.QPushButton(self.window, text='Select Font', clicked=f1)
        self.layout.addWidget(self.bt)
        self.window.show()


test().exec()
