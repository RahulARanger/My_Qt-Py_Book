from PyQt5 import QtWidgets,QtGui
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='Button Group')
        self.display=QtWidgets.QLabel(self.window,text='This is just a line of text')
        self.colorGroup=QtWidgets.QButtonGroup()
        self.display.setStyleSheet('color:orange')
        self.orange=QtWidgets.QRadioButton(self.window,text='orange',toggled=self.change,checked=True)
        self.orange.setStyleSheet('color:orange')
        self.red=QtWidgets.QRadioButton(self.window,text='red',toggled=self.change)
        self.red.setStyleSheet('color:red')
        self.yellow=QtWidgets.QRadioButton(self.window,text='yellow',toggled=self.change)
        self.yellow.setStyleSheet('color:yellow')
        self.colorGroup.addButton(self.orange,id=1)
        self.colorGroup.addButton(self.red,id=2)
        self.colorGroup.addButton(self.yellow,id=3) # radio buttons without any group acts unison so it's better to group them
        print(self.colorGroup.buttons())
        self.fontGroup=QtWidgets.QGroupBox() # ! avoid using the parent
        self.small,self.medium,self.large=[QtWidgets.QRadioButton(self.window,text=i,toggled=self.doresize) for i in ['Small (6)','Medium (9)', 'Large (20)']]
        self.display.move(100,100)
        self.orange.move(105,120)
        self.red.move(105,140)
        self.yellow.move(105,160)
        self.small.move(105,180)
        self.medium.move(105,210)
        self.large.move(105,240)
        self.actual=self.display.font()
        self.window.show()
    def change(self):
        print(self.sender().text())
        self.display.setStyleSheet('color:'+self.sender().text())
    def doresize(self):
        text=self.sender().text()
        if '6' in text:self.display.setFont(QtGui.QFont(self.actual.family(),6,self.actual.weight(),self.actual.italic()))
        elif '9' in text:self.display.setFont(QtGui.QFont(self.actual.family(),9,self.actual.weight(),self.actual.italic()))
        elif  '20' in text:self.display.setFont(QtGui.QFont(self.actual.family(),20,self.actual.weight(),self.actual.italic()))
        self.display.repaint()
        self.display.adjustSize()
test().exec()