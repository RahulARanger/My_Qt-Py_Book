from PyQt5 import QtWidgets
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='Return Pressed Signal')
        self.count=0
        self.layout=QtWidgets.QVBoxLayout()
        self.window.setLayout(self.layout)
        self.entry=QtWidgets.QLineEdit(self.window,toolTip='Entry',clearButtonEnabled=True)
        self.label=QtWidgets.QLabel(self.window,text='Return Pressed: {}'.format(self.count))
        self.entry.returnPressed.connect(self.slot)
        self.layout.addWidget(self.entry)
        self.layout.addWidget(self.label)
        self.window.show()
    def slot(self):
        self.count+=1
        self.label.setText('Return Pressed: {}'.format(self.count))
test().exec()