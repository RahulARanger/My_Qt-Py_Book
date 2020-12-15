from PyQt5 import QtWidgets
class Test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='Radio Buttons')
        self.radiobutton=QtWidgets.QRadioButton(self.window,toolTip='Radio Button',text='This is a Radio Button')
        self.window.show()
        self.radiobutton.show()
        self.radiobutton.setText('This is a Radio Button!') # for setting the text
        print(self.radiobutton.isChecked())
        # NOTE: we can also use shortcut keys as QPushButton
Test().exec()