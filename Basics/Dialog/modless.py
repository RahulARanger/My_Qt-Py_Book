from PyQt5 import QtWidgets,QtCore,QtGui

class Dialog(QtWidgets.QDialog): # !(also subclass of QtWidgets.QWidget)
    def __init__(self,parent=None):
        super().__init__(parent) # parent can also be given just to be placed above that
        self.layout=QtWidgets.QVBoxLayout()
        self.labelshow=QtWidgets.QLabel(self,text='This Text an be made Visible/InVisible')
        self.more=QtWidgets.QPushButton(self,text='more',clicked=self.togglethis)
        self.ok=QtWidgets.QPushButton(self,text='ok',clicked=self.accept)
        self.more.setWhatsThis('Toggles the visiblilty of the labels content') # ? press that '?' and then click the more button then u can see what it does
        self.cancel=QtWidgets.QPushButton(self,text='cancel',clicked=self.reject)
        self.setLayout(self.layout)
        self.state=True
        self.layout.addWidget(self.labelshow)
        self.layout.addWidget(self.more)
        self.layout.addWidget(self.ok)
        self.layout.addWidget(self.cancel)
    def togglethis(self):
        self.state=not(self.state)
        self.labelshow.setVisible(self.state)

class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.app=Dialog() # * modless dialog exists without any parent window
        print(self.app.show()) # doesnt return any value other than None
test().exec()