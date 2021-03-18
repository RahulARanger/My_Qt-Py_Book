from PyQt5 import QtWidgets,QtGui
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='Enable Disable')
        self.toggle=QtWidgets.QToolButton(self.window,text='Hello',clicked=self.change) # when icon is used the text disappears in the toolbutton
        self.lab=QtWidgets.QLabel(self.window,text='Disabled')
        self.state=False
        self.toggle.move(100,100)
        self.lab.move(100,200)
        self.window.show()
        self.change()
    def change(self):
        self.state=not(self.state)
        if self.state:
            self.toggle.setIcon(QtGui.QIcon("Widgets\Widgets\ToolButton\enable.png"))
            self.lab.setDisabled(False)
            self.lab.setText('Enabled Now')
        else:
            self.toggle.setIcon(QtGui.QIcon("Widgets\Widgets\ToolButton\disable.png"))
            self.lab.setText('Disabled')
            self.lab.setDisabled(True)
        self.lab.repaint()
        self.lab.adjustSize()
        
test().exec()