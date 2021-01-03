from PyQt5 import QtWidgets
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='Repaint of the Label')
        self.bt=QtWidgets.QPushButton(self.window,text='Change Text',clicked=self.change)
        self.lb=QtWidgets.QLabel(self.window,text='Select Some Text')
        self.bt.move(100,50)
        self.lb.move(100,100)
        self.window.show()
    def change(self):
        result=QtWidgets.QInputDialog.getText(self.window,'Enter Some Text','Enter the Text for the label')
        if not result[-1]:return None
        self.lb.setText(result[0])
        self.lb.repaint() # doesnt adjust size but refreshes the widget
        self.lb.adjustSize() # resizes according to the contents of the label
test().exec()
