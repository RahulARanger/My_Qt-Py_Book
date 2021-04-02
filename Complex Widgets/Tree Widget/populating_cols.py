from PyQt5 import QtWidgets
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='Setting the Column Count')
        self.tree=QtWidgets.QTreeWidget(self.window)
        self.tree.setColumnCount(2) 
        self.tree.setHeaderLabels(['Index','Elements']) 
        self.container=['Hello','There','Hi','Rem Rem Rem']
        self.insertItems()
        self.tree.move(50,50)
        self.window.show()
    def insertItems(self):
        for i in range(len(self.container)):
            temp=QtWidgets.QTreeWidgetItem(self.tree,[str(i),self.container[i]])            
            self.tree.addTopLevelItem(temp)
    
test().exec()