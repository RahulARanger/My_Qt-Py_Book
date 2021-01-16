from PyQt5 import QtWidgets,QtCore,QtGui
import os
class ScrollBarArea(QtWidgets.QScrollArea):
    def __init__(self,parent):
        super().__init__()
        self.setWidget(parent) # sets the frame or its children as the parent
        self.setWidgetResizable(True) # for making the scrollbar expand whenever the widget gets expanded
    def setthesize(self,parameter):
        pass #self.setFixedSize(parameter)

class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='ScrollArea')
        self.subwindow1=QtWidgets.QFrame(self.window)
        self.subwindow2=QtWidgets.QFrame(self.window)
        self.window.setLayout(QtWidgets.QHBoxLayout())
        self.foldericon=QtGui.QIcon(os.path.join(os.path.dirname(__file__),"folder.png"))
        self.setupthis()
        self.window.show()
    def setScrollBars(self):
        self.subscroll1=ScrollBarArea(self.subwindow1)
        self.subscroll1.setthesize(QtCore.QSize(200,600)) # for fixing the size of the scrollbar
        self.window.layout().addWidget(self.subscroll1)
        self.window.layout().addWidget(self.subwindow2)
        self.window.show()
    def setupthis(self):
        folders=os.listdir()*10
        print(len(folders))
        self.folders=[QtWidgets.QPushButton(self.subwindow1,text='{}'.format(i)) for i in folders]
        [i.setIcon(self.foldericon) for i in self.folders]
        self.subwindow1.setLayout(QtWidgets.QVBoxLayout())
        for i in range(len(folders)):
            layout=QtWidgets.QHBoxLayout()
            self.subwindow1.layout().addLayout(layout)
            layout.addWidget(self.folders[i])
        
        self.setScrollBars()
test().exec()
