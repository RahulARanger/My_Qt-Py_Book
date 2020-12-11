from PyQt5 import QtWidgets,QtGui,QtCore
import sys
test=QtWidgets.QApplication(sys.argv)
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__(windowTitle='basic template')
a=MainWindow()
a.show() 
test.exec()

