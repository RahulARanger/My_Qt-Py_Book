from PyQt5 import QtWidgets
class Test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='Horizontal Box layout')
        self.layout=QtWidgets.QHBoxLayout()
        self.window.setLayout(self.layout)
        self.entry=QtWidgets.QLineEdit(self.window,toolTip='Entry',placeholderText='Enter Something: ',clearButtonEnabled=True)
        self.submit=QtWidgets.QPushButton(self.window,toolTip='Submit',text='Submit')
        self.layout.addStretch()
        self.layout.addWidget(self.entry)
        self.layout.addWidget(self.submit)
        self.layout.addStretch()
        self.window.show()
Test().exec()
