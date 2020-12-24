from PyQt5 import QtWidgets
class Test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window=QtWidgets.QWidget(windowTitle='Tool Button')
        self.toolbutton=QtWidgets.QToolButton(self.window,toolTip='QToolButton',text='Lol')
        self.toolbutton.show()
        self.window.show()
        self.toolbutton.setAutoRaise(True)
Test().exec()