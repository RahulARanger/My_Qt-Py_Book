from .tabwindow import HomeImageViewer,QuickImageView
import os
from PyQt5 import QtWidgets,QtCore,QtGui

class MainImageViewer(QtWidgets.QMainWindow):
    def __init__(self,quickview=True):
        super().__init__()
        self.__QUICKVIEW=quickview
        self.__setMainWindow()
        self.__setStatusBar()
        self.__setMenu()

    def __getattr__(self,index):
        if index=='mode':return self.__QUICKVIEW

    def __setMainWindow(self):
        self.__MainWindow=QtWidgets.QWidget(self)
        self.__MainWindow.setLayout(QtWidgets.QStackedLayout())
        self.__MainWindow.layout().addWidget(QuickImageView(self)) 
        self.__MainWindow.layout().addWidget(HomeImageViewer(self))
        self.setStatusTip('Welcome to ImageViewer')
        self.__MainWindow.layout().setCurrentIndex(0 if self.mode else 1)
        self.setCentralWidget(self.__MainWindow)

    def __setMenu(self):
        pass

    def __setStatusBar(self):
        pass

class ImageViewer(QtWidgets.QApplication):
    def __init__(self,*args):
        super().__init__([])
        self.main=MainImageViewer()
        self.main.show()
        self.exec()



