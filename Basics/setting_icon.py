from PyQt5 import QtWidgets
import sys
class Iconwindow(QtWidgets.QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.window=QtWidgets.QWidget(windowTitle='Icon Window',toopTip='check this')
a=Iconwindow()
a.exec()