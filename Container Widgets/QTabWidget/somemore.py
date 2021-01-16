from PyQt5 import QtWidgets

class SampleWidget(QtWidgets.QWidget):
    def __init__(self,parent,number):
        super().__init__(parent)
        self.label=QtWidgets.QLabel(self,text=str(number))
        self.label.move(10,10)
    
class TabWindow(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QTabWidget()
        self.window.show()
        self.setThings()
        self.showThings()
        
        TabWindow.exec()
    def setThings(self):
        self.window.setTabsClosable(True)
        self.window.currentChanged.connect(self.tab_changed)
        self.window.tabCloseRequested.connect(self.close_tab)
        self.window.tabBarDoubleClicked.connect(self.doThis)
        self.window.tabBarClicked.connect(self.doThisToo)
    def doThis(self,args):
        print('YOu have Double clicked the tabbar',args)
    def doThisToo(self,args):
        print("You have single clicked the Tab Bar",args)
    
    def close_tab(self,index):
        if self.window.count()==1:
            print('You cant close the last tab')
        else:
            self.window.removeTab(index)

    def tab_changed(self,*args):
        print('You Have Changed the Tab. to: {}'.format(args))
    def showThings(self):
        for i in range(6):
            self.window.addTab(SampleWidget(self.window,i),str(i))
TabWindow()