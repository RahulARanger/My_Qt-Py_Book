from PyQt5 import QtWidgets
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = QtWidgets.QWidget(windowTitle='Strechable Layouts ')
        # ! only for box layouts
        self.layout = QtWidgets.QHBoxLayout()
        self.layout = QtWidgets.QHBoxLayout()
        self.layout = QtWidgets.QHBoxLayout()
        self.window.setLayout(self.layout)
        self.button1=QtWidgets.QPushButton(self.window,text='1',toolTip='PushButton1')
        self.button2=QtWidgets.QPushButton(self.window,text='2',toolTip='PushButton1')
        self.button3=QtWidgets.QPushButton(self.window,text='3',toolTip='PushButton1')
        self.button4=QtWidgets.QPushButton(self.window,text='4',toolTip='PushButton1')
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2,5)
        self.layout.addWidget(self.button3,2)
        self.layout.addWidget(self.button4,3)
        self.window.show()
test().exec()