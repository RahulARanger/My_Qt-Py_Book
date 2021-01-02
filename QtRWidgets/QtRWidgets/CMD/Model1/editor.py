from PySide6 import QtWidgets,QtCore,QtGui,QtUiTools
editor,qtwidgeteditor=QtUiTools.loadUiType('QtRWidgets\CMD\Model1\editor.ui')
import code
import threading
import sys
from queue import Queue
class Editor(qtwidgeteditor,editor):
    def __init__(self,size=QtCore.QSize(300,300)):        
        super().__init__()
        self.pipe=Queue()        
        #self.checkpoint=(sys.stdin,sys.stdout,sys.stderr)
        #
        self.prestart()
        self.setBaseSize(size)
        self.connectevents()
        self.connected=False
        #print(self.connected)
        self.poststart()  
        
         
        print('op')
    def connect(self,connectit=True):
        if not connectit:
            # respond when closing this app
            print('bye')
            # disconnect the thread and close the app
        if self.connected:
            print('Already Connected')
        else:
            self.connected=True
            print('G')
            code.interact(local=locals())
    def readline(self):
        return self.pipe.get()
    def write(self,string):
        print('*')
        self.cmdeditor.setText(string)
    def connectevents(self):
        self.cmdeditor.textChanged.connect(self.check)
    def check(self):
        self.pipe.push(self.cmdeditor.text())
    def flush(self):pass
    def prestart(self):
        self.setupUi(self)
    def poststart(self):
        self.show()

if __name__=='__main__':
    a=QtWidgets.QApplication([])
    obj=Editor()
    a.exec_()