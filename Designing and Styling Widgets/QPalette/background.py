from PySide2 import QtWidgets, QtGui


# Refer More about this here: https://doc.qt.io/qtforpython/PySide6/QtGui/QPalette.html

class Test(QtWidgets.QDial):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setRange(0, 100)
        print(self.palette())  # this is the predefined palette
        self.extracted = QtGui.QPalette()
        self.customize()

    def customize(self):
        self.setAutoFillBackground(True)  # this is mandatory

        # most of the widget's background except container widgets like Q Widget doesnt need Button
        self.extracted.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Button, QtGui.QColor("orange"))

        self.setPalette(self.extracted)


check = QtWidgets.QApplication([])
check.setStyle("fusion")  # first set the style to fusion (to maintain common styles)

display = QtWidgets.QWidget()

another = display.palette()
another.setColor(QtGui.QPalette.Window, QtGui.QColor("black"))
display.setPalette(another)

mode = Test(display)
mode.move(100, 100)
display.show()
# mode = Test()
# mode.show()
check.exec_()
