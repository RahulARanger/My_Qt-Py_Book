from PyQt5 import QtWidgets,QtCore,QtGui       

class Defaults(QtWidgets.QWidget):
    def __init__(self):
        self.setLayout(QtWidgets.QVBoxLayout())
        
class More(QtWidgets.QTabWidget):

    def __init__(self,details,parent):
        super().__init__(parent,movable=True)
        self.__decidetabs()

    def __decidetabs(self):
        self.addTab(QtWidgets.QWidget(),'Settings')
        self.addTab(QtWidgets.QWidget(),'Defaults')

