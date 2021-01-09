from .quickview import QuickImageView
from PyQt5 import QtWidgets,QtCore,QtGui
class Directory(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        #self.__main=QtWidgets.QFileDialog.getOpenFileName(self,'Open File',QtCore.QDir.homePath(),'Image Files (*.jpeg)')
        
    
class HomeImageViewer(QtWidgets.QTabWidget):

    def __init__(self,parent=None):
        super().__init__(parent,movable=True)
        self.homedirectory=Directory()
        self.decidetabs()

    def decidetabs(self):
        self.addTab(QtWidgets.QWidget(),'Image')
        self.addTab(QtWidgets.QWidget(),QtGui.QIcon('QtRWidgets\\ImageViewer\\Resources\\Icons\\settings.png'),'Settings')
        self.addTab(self.homedirectory,'Directory')
        self.addTab(QtWidgets.QWidget(),'Details')

if __name__=='__main__':
    app=QtWidgets.QApplication([])
    a=HomeImageViewer()
    a.show()
    app.exec()