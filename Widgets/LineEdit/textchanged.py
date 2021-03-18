from PyQt5 import QtWidgets
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='Text Changed Signal of the LineEdit')
        self.layout=QtWidgets.QVBoxLayout()
        self.window.setLayout(self.layout)
        self.entry=QtWidgets.QLineEdit(self.window,toolTip='Entry',clearButtonEnabled=True)
        self.entry.textChanged.connect(lambda x:self.note(x))
        self.entry2=QtWidgets.QLineEdit(self.window,toolTip='Changes made',readOnly=True)
        self.layout.addWidget(self.entry)
        self.layout.addWidget(self.entry2)
        self.window.show()
    def note(self,string):
        self.entry2.setText(string)
        print(string)
test().exec()