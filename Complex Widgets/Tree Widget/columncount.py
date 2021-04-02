from PyQt5 import QtWidgets
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='Setting the Column Count')
        self.tree=QtWidgets.QTreeWidget(self.window)
        self.tree.setColumnCount(2) # sets the number of the COlumns
        self.tree.setHeaderLabels(['Index','Elements']) # for setting the headings of the columns
        self.tree.move(50,50)
        self.window.show()
test().exec()