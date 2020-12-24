# generally widgets in PyQt5 or PySide(2-6) resizes according to the size of the window (and it's results are not proper)

from PyQt5 import QtWidgets
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='Widget Sizing')
        self.window.show()
        self.layout=QtWidgets.QVBoxLayout()
        self.window.setLayout(self.layout)
        self.label=QtWidgets.QLabel(self.window,toolTip='Without Fixed Size',text='Without Fixed Size:')
        self.entry=QtWidgets.QLineEdit(self.window,toolTip='Entry',clearButtonEnabled=True)
        self.label2=QtWidgets.QLabel(self.window,toolTip='With Fixed Size',text='with Fixed Size:')
        self.entry2=QtWidgets.QLineEdit(self.window,toolTip='Entry',clearButtonEnabled=True)
        #! setFixedSize() doesn't take internal stucture of the widget into account so text might get damaged
        # * setFixedWidth() and setFixedHeight() also does this same job for width and height respectively
        self.entry2.setFixedSize(200,self.entry.height())
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.entry)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.entry2)
test().exec()