from PyQt5 import QtWidgets,QtCore

class EmbedMePls(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='File Dialog')
        self.dialog=QtWidgets.QFileDialog(self.window)
        self.dialog.setWindowFlags(QtCore.Qt.Widget)
        self.dialog.move(0,0)
        self.window.show()
EmbedMePls().exec()