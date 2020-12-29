from PyQt5 import QtWidgets
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='Connecting Signals')
        self.layout=QtWidgets.QVBoxLayout()
        self.window.setLayout(self.layout)
        self.bt=QtWidgets.QPushButton(self.window,text='Push Me',toolTip='Button')
        self.entry=QtWidgets.QLineEdit(self.window,clearButtonEnabled=True)
        self.layout.addWidget(self.entry)
        self.layout.addWidget(self.bt)
        # self.entry.returnPressed.connect(lambda :self.bt.clicked()) ! This raises an error
        self.bt.clicked.connect(lambda x:self.entry.setText('Contents Saved Successfully'))
        self.window.show()

test().exec()