from PyQt5 import QtWidgets

class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='Calculator')
        self.numbers=[QtWidgets.QPushButton(self.window,text='{}'.format(i)) for i in range(10)]
        self.symbols={i:QtWidgets.QPushButton(self.window,text='{}'.format(i)) for i in '=-+/*'}
        self.window.setLayout(QtWidgets.QGridLayout())
        self.set_layout()
        self.window.show()

    def set_layout(self):
        for i in range(1,10):
            self.window.layout().addWidget(self.numbers[i],(i-1)//3,(i-1)%3)
        
        self.window.layout().addWidget(self.symbols['*'],0,3)
        self.window.layout().addWidget(self.symbols['+'],1,3)
        self.window.layout().addWidget(self.symbols['-'],2,3)
        self.window.layout().addWidget(self.symbols['/'],3,3)
        self.window.layout().addWidget(self.symbols['='],3,2)

        self.window.layout().addWidget(self.numbers[0],3,0,1,2) # widget,row,column,rowspan and columnspan
        
test().exec()