import sys
from PySide6 import QtWidgets,QtCore
from .editor import CMDEditor

class CMDED(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.editor=CMDEditor(self)
        self.setCentralWidget(self.editor)  
        self.setBaseSize(QtCore.QSize(600,600))
        self.setWindowTitle('CMD')
        
class CMD(QtWidgets.QApplication):
    def __init__(self):
        super().__init__(sys.argv)
    def start(self):
        self.Commandline=CMDED()
        self.Commandline.show()
        sys.exit(self.exec_())

