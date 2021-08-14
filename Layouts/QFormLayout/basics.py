from PySide2 import QtWidgets, QtCore, QtGui


class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = QtWidgets.QWidget()
        self.window.setLayout(QtWidgets.QFormLayout())
        self.firstname, self.lastname = [QtWidgets.QLineEdit(self.window, placeholderText='{}'.format(i)) for i in
                                         ['Enter your First Name', 'Enter your Last Name']]
        self.DOB = QtWidgets.QDateTimeEdit(self.window,
                                           calendarPopup=True,
                                           )
        self.submit = QtWidgets.QPushButton(self.window, text="Submit")
        self.window.layout().addRow("First Name: ", self.firstname)
        self.window.layout().addRow("Last Name: ", self.lastname)
        self.window.layout().addRow("DOB:", self.DOB)
        self.window.layout().addRow("", self.submit)
        self.window.layout().setRowWrapPolicy(
            QtWidgets.QFormLayout.WrapAllRows)  # there are lot of other options too check documentation
        self.window.show()


test().exec_()
