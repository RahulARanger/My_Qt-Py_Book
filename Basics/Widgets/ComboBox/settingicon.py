from PyQt5 import QtWidgets,QtGui
import random
class Test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='ComboBox')
        self.cbox=QtWidgets.QComboBox(self.window,toolTip='ComboBox',
        editable=True,
        currentData=2,
        insertPolicy=QtWidgets.QComboBox.InsertAtTop)
        self.cbox.addItem('display','store this') # text to display, data to store
        self.cbox.addItem('b','oohoh')
        self.cbox.addItem('a','have to watch anime')
        self.cbox.insertItem(2,'custom','second pos') # pos,text,data to store
        for i in range(self.cbox.count()):self.cbox.setItemIcon(i,QtGui.QIcon(random.choice(["Basics\Widgets\ComboBox\ic_folder_black_48dp.png",
        "Basics\Widgets\ComboBox\ic_attachment_black_48dp.png"])))
        self.cbox.move(50,50)
        self.window.show()
Test().exec()