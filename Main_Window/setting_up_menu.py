from PyQt5 import QtWidgets,QtGui
import os

class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='Setting Up Menu')
        self.mainwindow=QtWidgets.QMainWindow()
        self.mainwindow.setCentralWidget(self.window)
        self.setupMenu()
        self.mainwindow.show()
    def setupMenu(self):
        self.menu=self.mainwindow.menuBar() # * can also be created QtWidgets.QAction()
        menu=QtWidgets.QMenu('File',self.mainwindow) # name, parent is self.mainwindow or any QWidget
        
        menu.setIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__),'file.svg'))) # xt will e replaced by the icon
        menu.addAction('Check')
        submenu=QtWidgets.QMenu('TestingThis',self.mainwindow)
        submenu.addAction('Test1')
        submenu.addAction('Test2')
        storethisbefore=submenu.addAction('Test3')
        print(type(storethisbefore))
        menu.addMenu(submenu)        
        menu.addAction('Tools',self.calledbytools)
        menu.addSeparator()
        exitaction=QtWidgets.QAction(QtGui.QIcon(os.path.join(os.path.dirname(__file__),'log-out.svg')),'Exit',self.mainwindow) # explict way to create the actions
        exitaction.triggered.connect(self.mainwindow.close)
        menu.addAction(exitaction)
        wht=self.menu.addMenu(menu)
        print(type(wht))
        menu2=self.menu.addMenu("Next") # returns the  QMenu Object
        print(type(menu2))
        print(self.mainwindow.actions())
    def calledbytools(self,*args,**kwargs):
        print('Hello',args,kwargs)
test().exec()
        