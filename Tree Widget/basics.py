from PyQt5 import QtWidgets
# THis is the simple way to add the items into the QTreeWidget
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='QTreeWidget')
        self.tree=QtWidgets.QTreeWidget(self.window)
        self.tree.move(100,100)
        self.bt=QtWidgets.QPushButton(self.window,text='Insert',clicked=self.append)
        self.bt.move(100,50)
        self.window.show()
    def append(self):
        result=QtWidgets.QInputDialog.getText(self.window,'Enter some String Value','Enter a String to append it to the Table:')
        if not result[-1]:return None
        temp=QtWidgets.QTreeWidgetItem(self.tree)
        temp.setText(0,result[0])
        self.tree.addTopLevelItem(temp)
        
test().exec()
