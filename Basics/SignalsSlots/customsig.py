from PyQt5 import QtCore,QtWidgets
class CustomWidget(QtWidgets.QPushButton):
    def __init__(self,parent):
        super().__init__(parent)
        self.signal=QtCore.pyqtSignal(str) # arguments (as the types)
        self.__privates=['private1','private2','private3']
        self.clicked.connect(lambda x:self.check('From Own Class'))
    def check(self,msg):
        self.signal.emit(msg)
        print('msg:',msg,'privates:',self.__privates)
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='Custom Signals')
        self.bt=CustomWidget(self.window)
        self.layout=QtWidgets.QVBoxLayout()
        self.window.setLayout(self.layout)
        self.layout.addWidget(self.bt)
        self.bt2=QtWidgets.QPushButton(self.window,text='Push Me',clicked=lambda x:self.bt.signal('From Main Class'))
        self.layout.addWidget(self.bt)
        self.layout.addWidget(self.bt2)
        self.window.show()
test().exec()