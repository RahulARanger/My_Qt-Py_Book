from PySide6 import QtWidgets

#  Refer this for more info https://doc.qt.io/qtforpython/PySide6/QtWidgets/QTabWidget.html
class TabWidget(QtWidgets.QWidget):
    def __init__(self,parent):
        super().__init__(parent)
        self.tabs=[QtWidgets.QWidget(toolTip=str(i)) for i in range(66)] # each has it own
        for i in self.tabs:
            test=QtWidgets.QHBoxLayout()
            i.setLayout(test)
            test.addWidget(QtWidgets.QPushButton(i,text='Testing Button, Object id: {}'.format(i),toolTip='Testing Button'))
        self.tabwindow=QtWidgets.QTabWidget(self,
        movable=True, # you can drag the tabs to reorder it (default is False)
        tabBarAutoHide=True, #()
        tabPosition=QtWidgets.QTabWidget.West, # default is North,
        tabShape=QtWidgets.QTabWidget.Triangular, # (default is Rounded)
        usesScrollButtons=True
        )
        self.layout=QtWidgets.QVBoxLayout()
        self.tabwindow.setLayout(self.layout)
        for i in range(len(self.tabs)):self.tabwindow.addTab(self.tabs[i],str(i))
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='TabWidget')
        self.tabwindow=TabWidget(self.window)
        self.window.show()
        self.layout=QtWidgets.QHBoxLayout()
        self.window.setLayout(self.layout)
        self.layout.addWidget(self.tabwindow)
test().exec_() # This is line makers one of the major difference between of the Pyside and Pyqt5 (small right)
