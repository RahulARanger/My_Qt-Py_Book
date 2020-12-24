from PyQt5 import QtWidgets
import datetime
class Test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='Vertical Box Layout')
        self.layout=QtWidgets.QVBoxLayout()
        self.window.setLayout(self.layout)
        self.name=QtWidgets.QLineEdit(self.window,toolTip='Name Entry',placeholderText='Enter Your Name: ',clearButtonEnabled=True)
        self.age=QtWidgets.QSpinBox(self.window,maximum=30,minimum=18,prefix='Age: ')
        self.dob=QtWidgets.QDateEdit(self.window,calendarPopup=True)
        self.layout.addWidget(self.name)
        self.layout.addWidget(self.age)
        self.layout.addWidget(self.dob)
        self.window.show()
Test().exec()
        