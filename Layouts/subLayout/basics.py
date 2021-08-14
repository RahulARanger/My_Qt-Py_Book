from PySide2 import QtWidgets


# THis has the same woking of the pack() in Tkinter
class Test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = QtWidgets.QWidget(windowTitle='SubLayouts')
        self.layout = QtWidgets.QVBoxLayout()  # main layout is Vertically Aligned Box
        self.window.setLayout(self.layout)
        self.line1 = QtWidgets.QHBoxLayout()  # sublayout are horizontally aligned boxes
        self.line2 = QtWidgets.QHBoxLayout()
        self.line3 = QtWidgets.QHBoxLayout()
        self.line4 = QtWidgets.QHBoxLayout()
        self.layout.addLayout(self.line1)
        self.layout.addLayout(self.line2)
        self.layout.addLayout(self.line3)
        self.layout.addLayout(self.line4)  # you can do this at the later part
        self.name = QtWidgets.QLabel(self.window, text='Name: ', margin=6, toolTip='name')
        self.nentry = QtWidgets.QLineEdit(self.window, placeholderText='Enter Your Name: ', toolTip='Name Entry')
        self.age = QtWidgets.QLabel(self.window, text='Age: ', margin=6, toolTip='Age')
        self.nage = QtWidgets.QSpinBox(self.window, toolTip='Age Spinbox', suffix=' years', maximum=30, minimum=18)
        self.dob = QtWidgets.QLabel(self.window, text='Date Of Birth: ', margin=6, toolTip='DOB')
        self.edob = QtWidgets.QDateEdit(self.window, calendarPopup=True, toolTip='Date of Birth')
        self.submit = QtWidgets.QPushButton(self.window, text='Submit', toolTip='Submit')
        self.submit.clicked.connect(self.display_info)
        self.line1.addWidget(self.name)
        self.line1.addWidget(self.nentry)
        self.line2.addWidget(self.age)
        self.line2.addWidget(self.nage)
        self.line3.addWidget(self.dob)  # place them according the desired Lines
        self.line3.addWidget(self.edob)
        self.line4.addWidget(self.submit)
        self.window.show()

    def display_info(self):
        print(f"""
{69 * "*"}
Name: {self.nentry.text()}
Age: {self.nage.text()}
DOB: {self.edob.date()}
{69 * "*"}
        """)

Test().exec_()
