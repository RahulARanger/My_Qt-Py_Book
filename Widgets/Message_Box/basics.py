from PyQt5 import QtWidgets
# TODO: we are creating the messageboxes with the static functions
class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='QMessageBox')
        self.layout=QtWidgets.QHBoxLayout()
        self.window.setLayout(self.layout)
        # ? parent,title,information
        f1=lambda x=True:QtWidgets.QMessageBox.information(self.window,'info','This is a Information Message Box')
        f2=lambda x=True:QtWidgets.QMessageBox.question(self.window,'question','This is a Question Message Box')
        f3=lambda x=True:QtWidgets.QMessageBox.warning(self.window,'Warning','This is a Warning Message Box') # ? comes with the warning sound
        f4=lambda x=True:QtWidgets.QMessageBox.critical(self.window,'Critical','This is a Critical Message Box') # ? comes with the critical sound
        f5=lambda x=True:QtWidgets.QMessageBox.about(self.window,'About','This is the About Message Box')
        f6=lambda x=True:QtWidgets.QMessageBox.aboutQt(self.window,'About Qt')

        self.information=QtWidgets.QPushButton(self.window,text='Information',clicked=f1)
        self.question=QtWidgets.QPushButton(self.window,text='Question',clicked=f2)
        self.warning=QtWidgets.QPushButton(self.window,text='Warning',clicked=f3)
        self.critical=QtWidgets.QPushButton(self.window,text='Critical',clicked=f4)
        self.about=QtWidgets.QPushButton(self.window,text='About',clicked=f5)
        self.aboutqt=QtWidgets.QPushButton(self.window,text='About Qt',clicked=f6)
        self.layout.addWidget(self.information)
        self.layout.addWidget(self.question)
        self.layout.addWidget(self.warning)
        self.layout.addWidget(self.critical)
        self.layout.addWidget(self.about)
        self.layout.addWidget(self.aboutqt)
        self.window.show()
test().exec()