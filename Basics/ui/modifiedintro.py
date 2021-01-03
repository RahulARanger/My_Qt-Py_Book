import intro
from PyQt5 import QtWidgets
class ModifiedForm(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget()
        self.object_=intro.Ui_Form()
        self.object_.setupUi(self.window)
        self.setconnections()
        self.window.show()
    def setconnections(self):
        self.object_.login.clicked.connect(self.checkdetails)
    def checkdetails(self):
        if self.object_.username.text()!='username' or self.object_.password.text()!='password':
            print('incorrect')
        else:
            print('correct')
ModifiedForm().exec()